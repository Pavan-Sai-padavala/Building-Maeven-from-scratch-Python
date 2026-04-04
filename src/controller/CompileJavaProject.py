import os
import subprocess


class CompileJavaProject:
    def __init__(self,project_dir,target_dir=None):
        self.project_dir = project_dir
        self.target_dir = os.path.join(self.project_dir,"target") if target_dir is None else target_dir
        self.java_files = []

    # Recursive function to iterate java files in a project directory
    def path_gen(self, project_dir=None):
        for entry in os.scandir(project_dir):
            if entry.is_file() and entry.name.endswith(".java"):
                self.java_files.append(entry.path)
            elif entry.is_dir():
                self.path_gen(entry.path)
        return 

    # Given a list of java files (absolute paths), compiles using javac
    def compileProject(self):

        self.path_gen(self.project_dir)

        compilation_failed = []
        compilation_message = {}
        while(True):
            count=len(self.java_files)
            
            for file in self.java_files:
                print("compiling java file:", file)
                result = subprocess.run(
                    ["javac", "-cp", self.target_dir, "-d", self.target_dir, file],
                    capture_output=True,
                    text=True,
                    check=False,
                )

                if result.returncode != 0:
                    print("file not processed", file)
                    compilation_failed.append(file)
                    compilation_message[file] = result.stderr
            
            if(count!=len(compilation_failed)):
                self.java_files=compilation_failed
                compilation_failed=[]
            else:
                print("Compilation failed due to errors in your java project")
                for file in compilation_failed:
                    print("Compilation Error in " +file,end="\n")
                    print(compilation_message[file],end="\n")
                    print()
                return
                

    # def package(self):
    #     print("Packaging Java Application")
    #     subprocess.run(
    #         ["jar", "cfm", self.jar_path, self.manifest_file, self.class_files_path],
    #         capture_output=True,
    #         text=True,
    #         check=True
    #     )