# Check if Chocolatey is already installed
if (-not (Test-Path "$env:ProgramData\chocolatey\bin\choco.exe")) {
    # Install Chocolatey
    iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1')) -ExecutionPolicy Bypass
    
    # Add Chocolatey's bin directory to PATH
    $env:Path += ";$env:ProgramData\chocolatey\bin"
    
    Write-Host "Chocolatey installation completed."
} else {
    Write-Host "Chocolatey is already installed."
}
