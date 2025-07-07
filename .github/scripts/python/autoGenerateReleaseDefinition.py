import yaml
import os
import subprocess
import re

def autoGenerateReleaseDefinition():
    # Create directory if it doesn't exist
    yaml_file = '.github/release-definitions/release.yml'

    # Load existing YAML
    with open(yaml_file, 'r') as f:
        data = yaml.safe_load(f)

    # Get tags at HEAD
    result = subprocess.run(['git', 'tag', '--points-at', 'HEAD'],
                          capture_output=True, text=True)
    tags = result.stdout.strip().split('\n')

    # Update artifacts
    version_pattern = re.compile(r'(.+)_v\d.*')
    data['artifacts']={}
    for tag in tags:
        match = version_pattern.match(tag)
        if match:
            package_name = match.group(1)
            data['artifacts'][package_name] = 'LATEST_TAG'

    # Write updated YAML
    with open(yaml_file, 'w') as f:
        yaml.dump(data, f, default_flow_style=False, sort_keys=False)

if __name__ == '__main__':
    autoGenerateReleaseDefinition()