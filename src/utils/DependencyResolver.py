import http.client
import os
import sys


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from Model.BuildParams import BuildParams

class DependencyResolver:

    def __init__(self):
        self.BuildParams_obj = BuildParams.get_instance()
        self.dependency_list = self.BuildParams_obj.dependencies

    def get_jar_file(self,uri,jar_file_name):
        """
            Returns True if the jar file was downloaded successfully,
            else it returns False
        """
        connection = http.client.HTTPSConnection("repo1.maven.org")

        connection.request("GET",uri)

        res = connection.getresponse()
        
        status_code = res.status
        if(status_code == 200):
            content_type = res.getheader("content-type")
            if(content_type == "application/java-archive"):
                jar_file_bytes = res.read()
                f=open(os.path.join(self.BuildParams_obj.dependencyDir,jar_file_name),"wb")
                f.write(jar_file_bytes)
                f.close()

                connection.close()
                return True
            
        connection.close()
        return False
    
    def resolve_dependencies(self):
        """
            Iterate on the list of dependencies, parsed from the POM file,
            for each dependency, it creates a URI to be sent to the Maven Central Repository Host
            and passing URI to get_jar_file() method.
        """
        for dep in self.dependency_list:
            if(dep.get("version") is not None):
                uri="/maven2/" + dep.get("groupId") + "/" + dep.get("artifactId")
                uri=uri.replace(".","/")
                jar_file_name = dep.get("artifactId") + "-" + dep.get("version") +".jar"
                uri=uri + "/" + dep.get("version") + "/" + jar_file_name

                success = self.get_jar_file(uri,jar_file_name)
                if(success):
                    print("Dependency resolved successfully",dep)
                else:
                    print("Failed to Resolve dependency",dep)
