Set objShell = CreateObject("Shell.Application")

WScript.Echo "Set Time Zone to UTC"
objShell.ShellExecute "cmd.exe", "/c tzutil /s ""UTC""", "", "runas", 0
WScript.Sleep 1000

WScript.Echo "Set date to 2023-10-01"
objShell.ShellExecute "cmd.exe", "/c date 2023-10-01", "", "runas", 0

WScript.Echo "Set time to 00:00:00"
objShell.ShellExecute "cmd.exe", "/c time 00:00:00", "", "runas", 0

WScript.Sleep 3000

Set objWScript = CreateObject("WScript.Shell")
Set objExec = objWScript.Exec("cmd.exe /c tzutil /g")
pastTimeZone = objExec.StdOut.ReadAll()
WScript.Echo "Past Time Zone: " & pastTimeZone

Dim pastDate
pastDate = Date
WScript.Echo "Past Date: " & pastDate

Dim pastTime
pastTime = Time
WScript.Echo "Past Time: " & pastTime

WScript.Echo "Set Time Zone to Tokyo Standard Time"
objShell.ShellExecute "cmd.exe", "/c tzutil /s ""Tokyo Standard Time""", "", "runas", 0
WScript.Sleep 1000

WScript.Echo "Set Time to Current Time"
objShell.ShellExecute "cmd.exe", "/c w32tm /resync", "", "runas", 0

WScript.Sleep 3000

Set objWScript = CreateObject("WScript.Shell")
Set objExec = objWScript.Exec("cmd.exe /c tzutil /g")
currentTimeZone = objExec.StdOut.ReadAll()
WScript.Echo "Current Time Zone: " & currentTimeZone

Dim currentDate
currentDate = Date
WScript.Echo "Current Date: " & currentDate

Dim currentTime
currentTime = Time
WScript.Echo "Current Time: " & currentTime

'  sudo timedatectl set-timezone UTC
'  sudo timedatectl set-timezone Asia/Tokyo