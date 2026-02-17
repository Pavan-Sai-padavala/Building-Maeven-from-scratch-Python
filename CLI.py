import argparse

from ParsingHandler import CLI_Parser

parser = argparse.ArgumentParser(
    prog="CLI Tool for building JAVA Applications",
    usage="Input the Java project directory, and provide the dependency jar files if any",
    description="Python Command Line Interface (CLI) tool that builds and packages JAVA applications"
)

subParsers=parser.add_subparsers(dest="command")


buildCommand=subParsers.add_parser(name="build",prog="Build Command",description="Building Java Application")

buildCommand.add_argument("root_directory")
buildCommand.add_argument("--dep","-d",dest="dependency",action="extend")
buildCommand.add_argument("--target","-t",dest="target")



packageCommand=subParsers.add_parser("package",prog="Packaging Command",description="Packaging JAVA Project into a .JAR file")

packageCommand.add_argument("--resources","-res",dest="resources",action="extend",nargs="+")
packageCommand.add_argument("--classFiles","-cf",dest="classFiles")
packageCommand.add_argument("--dependency","-dep",dest="dependencies",action="extend",nargs="+")
packageCommand.add_argument("entryPoint")
packageCommand.add_argument("fileName")

if __name__ == "__main__":
    args = parser.parse_args()
    CLI_Parser(args)
