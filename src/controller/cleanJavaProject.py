import os
import shutil

from Model.BuildParams import BuildParams

class cleanJavaProject:

    def __init__(self):
        self.BuildParams_obj = BuildParams.get_instance()

    def clean(self):
        # checking pom.xml file for verifying project directory is a valid maeven project
        valid=os.path.exists(os.path.join(self.BuildParams_obj.prj_dir, "pom.xml"))
        if(not valid):
            print("No pom.xml file found in the given directory. kindly check whether the current project directory is a maeven project")
            return False
        else:
            print("Cleaning the build directory")
            shutil.rmtree(self.BuildParams_obj.targetDir)
            return True
        