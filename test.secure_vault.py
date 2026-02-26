import unittest
import os
import shutil
import vault_logic

class TestVaultLogic(unittest.TestCase):
    def setUp(self):
        """Set up a temporary environment for testing."""
        self.test_password = "test_password123"
        self.test_filename = "test_input.txt"
        self.test_content = b"This is secret data for testing purposes."
        self.output_filename = "test_output.txt"
        
        # Create a dummy file to encrypt
        with open(self.test_filename, 'wb') as f:
            f.write(self.test_content)

    def tearDown(self):
        """Clean up files and the vault directory after tests."""
        files_to_remove = [self.test_filename, self.output_filename]
        for f in files_to_remove:
            if os.path.exists(f):
                os.remove(f)
        
        # Remove the secure vault directory created during tests
        if os.path.exists(vault_logic.VAULT_DIR):
            shutil.rmtree(vault_logic.VAULT_DIR)

    def test_full_encryption_cycle(self):
        """Test: Original -> Encrypt -> Decrypt -> Matches Original."""
        # 1. Initialize password (creates .verify)
        self.assertTrue(vault_logic.verify_password(self.test_password))
        
        # 2. Encrypt the file
        vault_logic.encrypt_file(self.test_filename, self.test_password)
        
        # 3. Decrypt the file to a new location
        vault_logic.decrypt_file(self.test_filename, self.test_password, self.output_filename)
        
        # 4. Verify the content matches
        with open(self.output_filename, 'rb') as f:
            decrypted_content = f.read()
            
        self.assertEqual(self.test_content, decrypted_content)

    def test_wrong_password(self):
        """Test: Attempting to decrypt with the wrong password should fail."""
        vault_logic.verify_password(self.test_password)
        vault_logic.encrypt_file(self.test_filename, self.test_password)
        
        # Try to load metadata or decrypt with a bad password
        with self.assertRaises(ValueError):
            vault_logic.load_metadata("wrong_password")

    def test_metadata_persistence(self):
        """Test: Ensure file size and names are stored correctly in metadata."""
        vault_logic.verify_password(self.test_password)
        vault_logic.encrypt_file(self.test_filename, self.test_password)
        
        meta = vault_logic.load_metadata(self.test_password)
        self.assertIn(self.test_filename, meta)
        self.assertEqual(meta[self.test_filename]['size'], len(self.test_content))

if __name__ == "__main__":
    unittest.main()