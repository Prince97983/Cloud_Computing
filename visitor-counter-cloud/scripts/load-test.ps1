# Run in PowerShell after opening the app via minikube service or port-forward.
# Generates requests to trigger HPA. Keep this window running during observation.
$url = "http://127.0.0.1:5000/"
1..8 | ForEach-Object {
  Start-Job -ScriptBlock {
    param($u)
    while ($true) { try { Invoke-WebRequest -Uri $u -UseBasicParsing -TimeoutSec 3 | Out-Null } catch {} }
  } -ArgumentList $url
}
Write-Host "Load jobs started. Press Ctrl+C, then Get-Job | Stop-Job; Get-Job | Remove-Job"
