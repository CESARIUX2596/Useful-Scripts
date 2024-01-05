#!/bin/bash

# Specify the path to the desired directory
directoryPath="/path/to/output/dir/"

# List all conda environments
environments=$(conda info --json)

# Extract envs array using Python
envs=$(echo "$environments" | python3 -c 'import sys, json; print(json.load(sys.stdin)["envs"])')

# Iterate through each environment and export to YAML without builds
IFS=',' read -ra envsArray <<< "$envs"
for env in "${envsArray[@]}"; do
    envPath=$(echo "$env" | tr -d '[:space:]' | tr -d '"')
    envName=$(basename "$envPath")
    yamlFilePath="$directoryPath/$envName.yaml"
    conda env export -p "$envPath" --no-builds -f "$yamlFilePath"
done
