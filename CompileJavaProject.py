import os
import subprocess

basePath = "e:/pavan sai/users/Desktop"
javaFiles = []

# Recursive function to iterate java files in a project directory
def pathGen(directory, root):
    currentPath = os.path.normpath(os.path.join(root, directory))
    fullPath = os.path.normpath(os.path.join(basePath, currentPath))

    entries = os.listdir(fullPath)
    
    for entry in entries:
        entryPath = os.path.join(fullPath, entry)
        
        if os.path.isfile(entryPath) and entry.endswith(".java"):
            javaFiles.append(os.path.normpath(entryPath))

        elif os.path.isdir(entryPath):
            pathGen(entry, currentPath)
                
# Given a list of java files(absolute paths), compiles using javac command
def compileJavaProject():
    compilationFailed=[]
    for file in javaFiles:
            print("compiling java file: ",file)
            try:
                subprocess.run(
                    ["javac","-cp",target_dir,"-d", target_dir, file],
                    capture_output=True,
                    text=True,
                    check=True
                )
            except:
                print("file not processed",file)
                compilationFailed.append(file)
    return compilationFailed

pathGen("src", "")
for file in javaFiles:
    print(file)

target_dir = "e:/pavan sai/users/Desktop/src/target/"
os.makedirs(target_dir, exist_ok=True)

print("\nCompiling Java files...")

# Iteratively compiling java files
# if java file is requiring other .class files which are not compiled, 
# then those files are added into compiledFailed list

javaFiles=compileJavaProject()
while(len(javaFiles) !=0):
    javaFiles=compileJavaProject()
