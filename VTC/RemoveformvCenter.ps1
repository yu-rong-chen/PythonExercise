clear
$vip = '10.10.1.70'
$vid = 'administrator@vsphere.local'
$vpwd = 'Compaq@123'
$hip = '10.10.41.35' # Host IP
Import-Module VMware.VimAutomation.Core -PassThru
Connect-VIServer -Server $vip -User $vid -Password $vpwd -Force
Remove-VMHost $hip -Confirm:$false -ErrorAction Stop