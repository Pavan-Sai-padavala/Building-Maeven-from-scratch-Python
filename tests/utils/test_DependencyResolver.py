import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from src.utils.POM_Parser import POM_Parser
from src.utils.DependencyResolver import DependencyResolver

class Test_DependencyResolver(unittest.TestCase):
    def test_resolve_dependencies(self):
        """
            Goal: To Test resolve_dependencies() method, whether it is resolving dependencies,
            by downloading .jar files
        """
        test_pom_file= os.path.join(os.getcwd(),"tests\\Resources\\")
        POM_Parser(test_pom_file).parse_POM_file()

        DependencyResolver().resolve_dependencies()

        self.assertTrue(os.path.exists(os.path.join(os.getcwd(),"tests/Resources/target/dependencies")))

if __name__ == '__main__':
    unittest.main()