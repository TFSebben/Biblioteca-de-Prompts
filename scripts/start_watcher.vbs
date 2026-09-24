Set WshShell = CreateObject("WScript.Shell")
userProfile = WshShell.ExpandEnvironmentStrings("%USERPROFILE%")
psScript = userProfile & "\Projects\Biblioteca-de-Prompts\scripts\watch_prompts.ps1"
cmd = "powershell.exe -ExecutionPolicy Bypass -WindowStyle Hidden -File """ & psScript & """"
WshShell.Run cmd, 0, False
