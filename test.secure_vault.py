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
        with open(self.test_filename, 'wb') as f:
            f.write(self.test_content)

    def tearDown(self):
        files_to_remove = [self.test_filename, self.output_filename]
        for f in files_to_remove:
            if os.path.exists(f):
                os.remove(f)
        
        
        if os.path.exists(vault_logic.VAULT_DIR):
            shutil.rmtree(vault_logic.VAULT_DIR)

    def test_full_encryption_cycle(self):
        self.assertTrue(vault_logic.verify_password(self.test_password))
        vault_logic.encrypt_file(self.test_filename, self.test_password)
        vault_logic.decrypt_file(self.test_filename, self.test_password, self.output_filename)
        with open(self.output_filename, 'rb') as f:
            decrypted_content = f.read()
        self.assertEqual(self.test_content, decrypted_content)

    def test_wrong_password(self):
        vault_logic.verify_password(self.test_password)
        vault_logic.encrypt_file(self.test_filename, self.test_password)
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