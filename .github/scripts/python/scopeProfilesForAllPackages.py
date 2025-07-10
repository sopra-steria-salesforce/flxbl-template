import json

with open('sfdx-project.json', 'r+') as f:
    project = json.load(f)
    for package in project["packageDirectories"]:
        package['scopeProfiles'] = True
    # Write the updated JSON back to the file
    f.seek(0)
    json.dump(project, f, indent='\t')
    f.truncate()
f.close()