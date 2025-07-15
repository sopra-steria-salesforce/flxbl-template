import json
import os

with open('sfdx-project.json', 'r+') as f:
    project = json.load(f)
    for package in project["packageDirectories"]:
        if os.system('git diff HEAD origin/main --no-index --quiet ' + package["path"] + '/*'):
            print("Changes detected in package "+package["package"]+" --> Apex Tests will be run")
        else:
            package["skipTesting"]=True

    # Write the updated JSON back to the file
    f.seek(0)
    json.dump(project, f, indent='\t')
f.close()