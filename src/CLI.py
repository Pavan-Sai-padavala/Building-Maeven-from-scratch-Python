import argparse

from controller.CompileJavaProject import CompileJavaProject
from controller.cleanJavaProject import cleanJavaProject
from utils.DependencyResolver import DependencyResolver
from utils.POM_Parser import POM_Parser

class CLI:
    def __init__(self):
        self.parser = argparse.ArgumentParser(
            prog="CLI Tool for building JAVA Applications",
            usage="Input the Java project directory, with Maven Code structure",
            description="Python Command Line Interface (CLI) tool that builds and packages JAVA applications"
        )

        self.parser.add_argument("--clean", action="store_true",help="cleans the Target Directory")

        self.parser.add_argument("--install", action="store_true",help="Downloads jar files for the dependencies")

        self.parser.add_argument("--compile", action="store_true",help="Compile the Java Application")

        self.parser.add_argument("root_directory",help="project directory, containing .pom file and java source code")

    def start(self,argsVars):
        """
            Starts the CLI Application corresponding to the commands passed via CLI
        """
        POM_Parser(argsVars.get("root_directory")).parse_POM_file()

        if(argsVars.get("clean")):
            status=cleanJavaProject().clean()
            if(status):
                print("Cleaning the Target Directory Successfull")
            else:
                print("cleaning the Target Directory Fail")
                return

        if(argsVars.get("install")):
            DependencyResolver().resolve_dependencies()
        
        if(argsVars.get("compile")):
            DependencyResolver().resolve_dependencies()
            CompileJavaProject().compileProject()

if __name__ == "__main__":
    cli_obj = CLI()
    args=cli_obj.parser.parse_args()
    args_dict=vars(args)
    cli_obj.start(args_dict)
