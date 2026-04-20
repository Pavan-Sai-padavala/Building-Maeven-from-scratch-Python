# Building Minimalist Maven from scratch in Python

Reverse Engineered Maven java Build Tool as a Python-based Command-Line Application for compiling and packaging java projects
by resolving dependencies from pom.xml file

## Code Structure

```text
src/
  CLI.py                      # CLI entry point
  controller/
    CompileJavaProject.py      # Recursively compiles Java sources with javac
    cleanJavaProject.py        # Removes the build output directory
  Model/
    BuildParams.py             # Singleton class to hold the project meta data
  utils/
    POM_Parser.py             # Extracts project metadata and dependencies from pom.xml
    DependencyResolver.py      # Downloads dependency JARs from Maven Central Repository

tests/
  Resources/pom.xml            # Sample POM used by parser and dependency tests
  utils/                       
    test_DependencyResolver.py # Unit tests for checking Dependency Resolution working fine 
    test_POM_Parser.py         # Unit tests for checking POM Extraction working fine or not
```

## Setup

1. Python 3.x.
2. A Java Development Kit with `javac` available on your `PATH`.

```powershell
python -m venv myenv
.\myenv\Scripts\Activate.ps1

python src\CLI.py [--clean] [--install] [--compile] <project root directory>
```

## Usage

```powershell
python src\CLI.py [--clean] [--install] [--compile] <project root directory>
```

Command Line Options

- `--clean`: clears the target directory
- `--install`: resolves and downloads the `.jar` files for the dependencies
- `--compile`: compiles Java source code


## Need To Implement

- Implement the Chaining in Dependency Resolution, i.e Recursively fetching Dependency version from the parent POM files. Especially in Springboot projects.
- Implement the Packaging of java application
- Write the Unit Test cases for Controller