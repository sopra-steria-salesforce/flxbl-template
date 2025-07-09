import json
import os

changedPackages=[]
packageVersionsByPackageNames = {}
incrementsPerformed=False

def incrementChangedPackages():
    with open("sfdx-project.json", "r+") as f:
        project = json.load(f)
        for package in project["packageDirectories"]:
            # Check if package was changed compared to previous commit on main
            print("Check package "+package["path"]+" for changes")
            if os.system('git diff HEAD~1 HEAD --quiet ' + package["path"] + '/*'):
                print("Incrementing version for "+package["package"])
                changedPackages.append(package["package"])
                # Increment Minor number by 1
                version = package["versionNumber"].split('.')
                version[1] = str(int(version[1]) + 1)
                package["versionNumber"] = '.'.join(version)

        # Write the updated JSON back to the file
        f.seek(0)
        json.dump(project, f, indent='\t')
        f.truncate()
    f.close()

def incrementDependenciesForChangedPackages():
    global incrementsPerformed # Declare global variable to avoid local access issues

    # Change to the directory where the file is located
    with open("sfdx-project.json", "r+") as f:
        project = json.load(f)
        for package in project["packageDirectories"]:
            packageVersionsByPackageNames[package["package"]] = package["versionNumber"]
            if os.system('git diff HEAD~1 HEAD --quiet ' + package["path"] + '/*'):
                # If the package has dependencies, add to list of packages for evaluation of dependency update
                if "dependencies" in package:
                    for dependency in package["dependencies"]:
                        if "versionNumber" in dependency:
                            versionNumber=dependency["versionNumber"].split('.LATEST')[0] + '.NEXT'
                            if versionNumber!=packageVersionsByPackageNames[dependency["package"]]:
                                print("Increment dependency "+dependency["package"] +" for package " +package["package"])
                                incrementsPerformed=True
                                dependency["versionNumber"]=packageVersionsByPackageNames[dependency["package"]].split('.NEXT')[0] + '.LATEST'


        # Write the updated JSON back to the file
        f.seek(0)
        json.dump(project, f, indent='\t')
        f.truncate()
    f.close()

    if (incrementsPerformed or changedPackages):
        os.system('git config user.email "github-actions@github.com"')
        os.system('git config user.name "github-actions"')
        os.system('git add sfdx-project.json')

        # Commit the change
        os.system('git commit -m "(CI) Autoincrement versions for changed packages and dependencies"')


if __name__ == '__main__':
    incrementChangedPackages()
    incrementDependenciesForChangedPackages()