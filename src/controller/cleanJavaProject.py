import os
import shutil

class cleanJavaProject:

    def __init__(self,prj_dir):
        self.prj_root_dir=prj_dir

    def clean(self):
        # checking pom.xml file for verifying project directory is a valid maeven project
        valid=os.path.exists(os.path.join(self.prj_root_dir, "pom.xml"))
        if(not valid):
            print("No pom.xml file found in the given directory. kindly check whether the current project directory is a maeven project")
            return False
        else:
            print("Cleaning the build directory")
            shutil.rmtree(os.path.join(self.prj_root_dir, "target"))
            return True

def main():
    cleanObj=cleanJavaProject(r"D:\pavan sai\users\Desktop\DNS-Resolver-Java")
    status=cleanObj.clean()
    if(status):
        print("Cleaning the project directory Success")
    else:
        print("Cleaning the project directory Failed")

if __name__ =="__main__":
    main()