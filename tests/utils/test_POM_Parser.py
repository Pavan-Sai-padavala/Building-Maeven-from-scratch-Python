import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from src.utils.POM_Parser import POM_Parser
from src.Model.BuildParams import BuildParams

class Test_POM_Parser(unittest.TestCase):
    def test_parse_POM_file(self):
        """
            Goal: To Test whether the POM_Parser.parse_POM_file() method, 
            parsing correctly given a correct .pom file
        """
        test_pom_file= os.path.join(os.getcwd(),"tests\\Resources\\")
        POM_Parser(test_pom_file).parse_POM_file()
        
        BuildParams_obj = BuildParams.get_instance()
        self.assertEqual(BuildParams_obj.prj_name,"sample java program")
        self.assertEqual(BuildParams_obj.prj_description,"sample pom file for testing POM_Parser() method")
        self.assertEqual(BuildParams_obj.prj_version,"1.0.0")

        expected_dependencies = [
            {"groupId": "org.springframework.boot", "artifactId": "spring-boot-starter", "version": None},
            {"groupId": "org.springframework.boot", "artifactId": "spring-boot-starter-web", "version": None},
            {"groupId": "org.springframework.boot", "artifactId": "spring-boot-devtools", "version": None},
            {"groupId": "org.springframework.boot", "artifactId": "spring-boot-starter-test", "version": None},
            {"groupId": "c3p0", "artifactId": "c3p0", "version": "0.9.0.4"},
            {"groupId": "mysql", "artifactId": "mysql-connector-java", "version": None}
        ]

        self.assertEqual(expected_dependencies,BuildParams_obj.dependencies)
        

if __name__ == '__main__':
    unittest.main()


