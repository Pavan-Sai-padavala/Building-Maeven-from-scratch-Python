class BuildParams:
    _instance = None

    prj_dir = ""
    pom_file_path = ""
    prj_name = ""
    prj_description = ""
    prj_group_Id = ""
    prj_artifact_Id = ""
    prj_version = ""
    dependencies = []

    targetDir = ""
    classesDir = ""
    dependencyDir = ""
    
    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = BuildParams()
        return cls._instance