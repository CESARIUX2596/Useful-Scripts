#!/bin/bash

# List all conda environments
environments=$(conda info --json | jq -r '.envs[]')

# Specify the path to the desired directory
directoryPath="/path/to/your/desired/directory"

# Iterate through each environment and export to YAML without builds
for envPath in $environments; do
    envName=$(basename "$envPath")
    yamlFilePath="$directoryPath/$envName.yaml"
    conda env export -p "$envPath" --no-builds -f "$yamlFilePath"
done
