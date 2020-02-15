clear
$vip = '10.10.1.66'
$vid = 'kevin'
$vpwd = 'Compaq123'
$hip = '10.10.4.137' # Host IP
Import-Module VMware.VimAutomation.Core -PassThru
Connect-VIServer -Server $vip -User $vid -Password $vpwd -Force
Remove-VMHost $hip -Confirm:$false -ErrorAction Stop