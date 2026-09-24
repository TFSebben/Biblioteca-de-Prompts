param(
    [string]$VaultPath = "G:\Meu Drive\remotely-save\Google Drive Vault\Biblioteca de Prompts",
    [string]$ScriptPath = "$env:USERPROFILE\Projects\Biblioteca-de-Prompts\scripts\sync_prompts.py",
    [int]$DebounceSeconds = 10
)

$LogPath = "$env:USERPROFILE\Projects\Biblioteca-de-Prompts\scripts\watcher.log"

function Write-WatcherLog {
    param([string]$Message)
    $timestamp = (Get-Date).ToString("yyyy-MM-dd HH:mm:ss")
    $logEntry = "[$timestamp] $Message"
    Add-Content -Path $LogPath -Value $logEntry -Encoding UTF8
}

Write-WatcherLog "Iniciando monitoramento de: $VaultPath"

if (-not (Test-Path $VaultPath)) {
    Write-WatcherLog "ERRO: Caminho do cofre não encontrado: $VaultPath"
    exit 1
}

$watcher = New-Object System.IO.FileSystemWatcher
$watcher.Path = $VaultPath
$watcher.Filter = "*.md"
$watcher.IncludeSubdirectories = $true
$watcher.EnableRaisingEvents = $true

$global:pendingSync = $false
$global:lastEventTime = [DateTime]::MinValue
$global:lastChangedFile = ""

$action = {
    param($source, $eventArgs)
    $global:pendingSync = $true
    $global:lastEventTime = [DateTime]::Now
    $global:lastChangedFile = $eventArgs.FullPath
}

Register-ObjectEvent $watcher 'Changed' -Action $action | Out-Null
Register-ObjectEvent $watcher 'Created' -Action $action | Out-Null
Register-ObjectEvent $watcher 'Deleted' -Action $action | Out-Null
Register-ObjectEvent $watcher 'Renamed' -Action $action | Out-Null

Write-WatcherLog "Watcher registrado com sucesso. Aguardando alterações em arquivos .md..."

while ($true) {
    Start-Sleep -Seconds 2
    if ($global:pendingSync) {
        $elapsed = ([DateTime]::Now - $global:lastEventTime).TotalSeconds
        if ($elapsed -ge $DebounceSeconds) {
            $global:pendingSync = $false
            Write-WatcherLog "Alteração detectada em '$global:lastChangedFile'. Disparando sincronização..."
            try {
                $output = & python "$ScriptPath" 2>&1
                Write-WatcherLog "Sync concluído: $output"
            } catch {
                Write-WatcherLog "ERRO ao executar sync: $_"
            }
        }
    }
}
