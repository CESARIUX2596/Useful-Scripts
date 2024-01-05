# List all conda environments
$environments = & conda info --json | ConvertFrom-Json | Select-Object -ExpandProperty "envs"

# Specify the path with quotes
$directoryPath = "\path\to\output\dir\"

# Iterate through each environment and export to YAML without builds
foreach ($envPath in $environments) {
    $envName = [System.IO.Path]::GetFileName($envPath)
    $yamlFilePath = Join-Path -Path $directoryPath -ChildPath "$envName.yaml"
    & conda env export -p $envPath --no-builds -f $yamlFilePath
}
