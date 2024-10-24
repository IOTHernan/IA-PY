# powershell_scripts.ps1

function Script1 {
    Write-Output "Este es el Script 1"
}

function Script2 {
    Write-Output "Este es el Script 2"
}

function Script3 {
    Write-Output "Este es el Script 3"
}

param (
    [string]$scriptName
)

switch ($scriptName) {
    "Script1" { Script1 }
    "Script2" { Script2 }
    "Script3" { Script3 }
    default { Write-Output "Script no encontrado" }
}
