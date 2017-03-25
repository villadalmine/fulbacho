import unittest
# pip
# local
import fulbacho
from fulbacho import fulbacho
from fulbacho.fulbacho import Fulbacho

import unittest
# pip
# local
import fulbacho
from fulbacho import fulbacho
from fulbacho.fulbacho import Fulbacho

class FulbachoGoodConnections(unittest.TestCase):

    def setUp(self):
        self.client = Fulbacho()

    def test_instantiate_client(self):
        self.assertIsInstance(self.client, Fulbacho)

class FulbachoBadConnections(unittest.TestCase):

    def setUp(self):
        self.client = Fulbacho()

    def test_instantiate_client(self):
        self.assertIsInstance(self.client, Fulbacho)


if __name__ == '__main__':
    unittest.main()
