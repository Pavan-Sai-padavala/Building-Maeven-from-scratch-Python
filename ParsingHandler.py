from CompileJavaProject import CompileJavaProject

def CLI_Parser(args):


    """
    To Do: construct the compilation command and pass it to compilerProject()
    """
    command_type=args.command

    if(command_type=="build"):
      project_root=args.root_directory
      jar_dependencies=args.dependency
      destination_path=args.target

      compilerObj=CompileJavaProject(project_root)

      compilerObj.compileProject()

    else:
      entry_point=args.entryPoint
      jar_file_name=args.fileName
      mediaResources=args.resources
      jarFiles=args.dependencies
      classFiles=args.classFiles