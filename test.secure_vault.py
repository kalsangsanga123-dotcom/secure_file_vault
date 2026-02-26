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

 
if __name__ == "__main__":
    unittest.main()