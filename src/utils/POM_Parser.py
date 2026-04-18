import xml.etree.ElementTree as ET
import os

from ..Model import BuildParams

namespace = {'pom': 'http://maven.apache.org/POM/4.0.0'}

class POM_Parser:

    def __init__(self,prj_dir):
        self.BuildParams_obj = BuildParams.get_instance()

        self.BuildParams_obj.prj_dir = prj_dir
        self.BuildParams_obj.pom_file_path = os.path.join(prj_dir,"pom.xml")

        tree=ET.parse(self.BuildParams_obj.pom_file_path)
        self.root=tree.getroot()

    def get_build_dependencies(self):
        dependency_iter = self.root.findall("pom:dependencies/pom:dependency", namespace)
        self.BuildParams_obj.dependencies = []
        for dep in dependency_iter:
            self.BuildParams_obj.dependencies.append({
                         "groupId" : dep.find("pom:groupId",namespace).text ,
                         "artifactId" : dep.find("pom:artifactId",namespace).text,
                         "version" : dep.find("pom:version",namespace).text
                        })

    def get_project_data(self):
           self.BuildParams_obj.prj_group_Id = self.root.find("pom:groupId",namespace).text       
           self.BuildParams_obj.prj_artifact_Id = self.root.find("pom:artifactId",namespace).text
           self.BuildParams_obj.prj_version = self.root.find("pom:version",namespace).text
           self.BuildParams_obj.prj_name = self.root.find("pom:name",namespace).text
           self.BuildParams_obj.prj_description = self.root.find("pom:description",namespace).text

    def parse_POM_file(self):
         self.get_project_data()
         print("Project Data Config extracted from POM.xml")
         print("project name",self.BuildParams_obj.prj_name,end="\n")
         print("project description",self.BuildParams_obj.prj_description,end="\n")
         print("project version",self.BuildParams_obj.prj_version,end="\n")
         print("project Group ID",self.BuildParams_obj.prj_group_Id,end="\n")
         print("project Artifact ID",self.BuildParams_obj.prj_artifact_Id, end="\n")

         self.get_build_dependencies()
         print("List of Dependencies")
         print(self.BuildParams_obj.dependencies)
         