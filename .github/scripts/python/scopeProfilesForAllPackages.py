import json
import os

with open('sfdx-project.json', 'r') as f:
    project = json.load(f)

for package in project.get('packageDirectories', []):
    package['scopeProfiles'] = True

with open('sfdx-project.json', 'w') as f:
    json.dump(project, f, indent='\t')
    f.truncate()