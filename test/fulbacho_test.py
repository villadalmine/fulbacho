import unittest
# pip
# local
import fulbacho
from fulbacho import fulbacho
from fulbacho.fulbacho import Fulbacho
import unittest
import configparser
import os

class FulbachoCreationAndInitialization(unittest.TestCase):

    def setUp(self):
        self.client = Fulbacho()

    def test_instantiate_client(self):
        self.assertIsInstance(self.client, Fulbacho)

    def test_initilization_client(self):
        self.client.initialize_config()
        cwd = os.getcwd()
        real_path = "fulbacho.ini"
        abs_file_path = os.path.join(cwd, real_path)
        os.remove(abs_file_path)

if __name__ == '__main__':
    unittest.main()
