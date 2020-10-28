# Content

[Network testing](#Network-testing)

[Xorsyst](#Xorsyst)

[Thread Starvation Test](#Thread-Starvation-Test)

[Meatgrinder](#Meatgrinder)

[STM linkpack](#STM-linkpack)

[Intel HVM tools](#intel-hvm-tools)

[PCIe Link Optimization Test](#PCIe-Link-Optimization-Test)

# Network testing (61)
## Configuration Counts
* SUT1 IP, username and password
* SUT2 IP, username and password
* runtime 1440

Total: 7
## Call Server Stress - Xorsyst - Step - General Server Setup (16)
### Set ROM EV (12)
    *For Gen 10*
      SET EV (requires EV.EFI - UEFI shell executible tool available from CSI tool/FTP or ROMQA):
          At UEFI shell prompt: map -r
          $ EV CQHSIGTH 01 01 00 01 00   
          $ EV CQHLKRATE 01     
          $ EV CQHMEMTHR 01 00 01 00 01 00 30 00 32 00 64 00 
          4 steps

    *DOS (Legacy mode) platforms:*
      SET EV (requires EV_VINE.COM - DOS tool): 
          Boot to DOS using USB key. 
          Run EV_VINE.COM. 
          Select Add to add an EV.
          Enter the Environment Variable as: CQHOVRD
          Enter the Hex Value as: 01 00 01 00 01 00 00 00 00 00 00 00 00 00
          5 steps

    *UEFI Platforms:*
      SET EV (requires EV.EFI - UEFI shell executible tool available from CSI tool/FTP or ROMQA): 
          At UEFI shell prompt: map -r 
          $ ev cqhovrd 01 00 01 00 05 00 00 00 00 00 00 00 00 00
          2 steps
    * reboot
### Configure server according to test instance details (1)
### Install SPP (1)
### Configure Raid and FC/FCoE controllers per test instance details(1)
### Verify all HW present at OS and server healthy (1)

## Call Server Stress - Xorsyst - Step - Install (X2 for SUT and client) (12)
### Setup SMBIOS pass-through if installing on a virtual machine (2)
    * setup SMBIOS pass-through on the guest VM
    * On an ESXi host, you need to edit the virtual machine configuration file (.vmx) and add this option: SMBIOS.reflectHost = TRUE
### Windows specific: Disable Windows Defender (1)
### Obtain Xorsyst distribution and license file for your target system (0)
### Verify that your target date/time and timezone are accurate (1)
### Install Perl interpreter on target if it is not present (1)
### Remove old Xorsyst installation if present (2)
### Windows specific: Disable Admin Approval Mode (0)
### Copy Xorsyst distribution and license file to target. Uncompress and place xorsyst.license in the xorsyst directory. (3)
### Execute 'xorsyst_install' from a shell(2)

## Call Server Stress - Xorsyst - Step - Open Xorsyst shell (3) 
### Open Xorsyst shell (1)
    *'su -l xo'
### Windows Only - Disable "QuickEdit Mode" and "Insert Mode" (1)
### Verify Xorsyst shell environment healthy (1)

## Using SUT shell created in a previous step, generate xorsystsetup using optimize_mirrortest.pl (1)

## Call Server Stress - Xorsyst - Step - Run and check (10)
### Call Server Stress - Xorsyst - Step - Open Xorsyst shell (3)
### Start xorsyst (1)
### Wait 15 minutes and check results directory for any issues (2)
    *Look for the presence of xorsyst.err, xorsyst .warn, or any files ending in '.err' or '.dmp' in the current results directory
### Let the run finish and capture final results (4)
    * Look for the presence of xorsyst.err, xorsyst.warn, netstat.err, or any files ending in '.err' or '.dmp'. 
    * Check dmesg.log on linux and err_warn_events.log or the Event Viewer on windows




<!-- ## Xorsyst setup on both client and SUT
1. Extract contents of xorsyst tool file
2. Copy license file
3. Install Xorsyst: `./xorsyst_istall`
4. log in as xo: `su -l xo`
5. Disable NetworkManager service `service NetworkManager stop`
6. Configure NIC’s using script (handle by VTC)
7. `service irqbalance start`

## Mirror server setup on client
1. Verify we can ping the SUT: `perl assign_ips.pl –validate ?2`
2. Execute: `perl create_servers.pl mirrorserver 1234 0 all`

## Configure and run Xorsyst’s MIRRORTEST on SUT
1. cd svtools/network: `perl optimize_mirrortest.pl –lastoctet 1 –runtime 1440 > ~/xorsystsetup`
2. `cd ~ && xstart`
3. check netstats.log file for an estimate of the performance 
4. view network performance: `sar –n DEV ?1`
5. Check mirrortest.summary 

Total: 7+ 7X2+7= 28. -->

# Xorsyst
## Call Stress - Xorsyst - Install SUT
## Call Server Stress - Xorsyst - Step - General Server Setup
## Call Stress - Xorsyst - Install Client
## Call Stress - Xorsyst - Setup - SUT and Client NIC setup
## Generate xorsystsetup on the SUT
## Configuration Note - use TESTDSKLIST instead of TESTFILELIST for testing large drives iwhen running Endurance
## Call Stress - Xorsyst - Open Xorsyst shell
## Edit xorsystsetup
## Call Stress - Xorsyst - Step - Run and check


## Configuration Counts
* SUT1 IP, username and password
* SUT2 IP, username and password
* runtime 1440
* TIME_2_RUN 

Total: 8
## Xorsyst setup

[Xorsyst setup on both client and SUT](#Xorsyst-setup-on-both-client-and-SUT)

[Mirror server setup on client](#mirror-server-setup-on-client)

Edit xorsystsetup variable:
 - TIME_2_RUN
 - Uncomment all 'MIRRORTEST' 
 - Uncomment line  LANTEST=$MIRRORTEST                      
 - Uncomment all ‘TESTDSKLIST=’ or ‘TESTDSKLIST.=‘ lines
 - Uncomment ‘TESTFILELIST=’ line
 - Uncomment ‘TIMETEST=’  line
 - If present, uncomment all NVDTEST_DEV lines


[Configure and run Xorsyst’s MIRRORTEST on SUT](#configure-and-run-xorsyst's-mirrortest-on-sut)

Total: 8+7*3+7 = 36

# Thread Starvation Test
## Configuration Counts
* SUT1 IP, username and password
* SUT2 IP, username and password
* runtime 1440
* TIME_2_RUN 
* isolcpus (XOPERF) 

Total: 9

[Xorsyst setup on both client and SUT](#Xorsyst-setup-on-both-client-and-SUT) 7

## Configure RBSU
* Disable C-states 
* Turn off HT/SMT 
* Turn off TurboBoost/CoreBoost 
* [AMD] set bias to performance determinism 

## Linux only
* Append isolcpus 
* boot runlevel 3 to kernal command
* `$systemctl stop pmlogger`
* `$systemctl stop pmcd`
* `$systemctl stop irqbalance`

## Generate Xorsystsetup
`$scan_conf -disable_all > xorsystsetup `

Edit xorsystsetup :
1. Set TIME_2_RUN to specified runtime  <<<runtime_minutes>>> , i.e. 1440 
2. uncomment LOG 
3. uncomment XOPERF_MONARCH and set it to 0 
4. [AMD only] uncomment and set XOPERF_WORKLOAD_TYPE=fp 
5. uncomment and set XOPERF_FP_POLL_PERIOD=60 
6. uncomment XOPERF and set it to match isolcpus, i.e. XOPERF=1-63 from our example above 


[Configure and run Xorsyst’s MIRRORTEST on SUT](#configure-and-run-xorsyst's-mirrortest-on-sut) 7

Total: 9+7+7+16 = 39

# Meatgrinder 

* Disable ASR in RBSU
* Install a Window's or Linux's based operating system
* Install latest HP driver support pack and shipping OS service/support pack 
* Install the latest PSP or LSP package. 
* Install ETD Meatgrinder 
    * execute ETD Meatgrinder
    * Select "Auto Configure"
    * Uncheck all areas to test except CPU/Memory. Leave default of "Prevent Peer Transfers Across Buses" selected.
    * click OK

    * Select "Test options" 
    * uncheck "Uncacheable" memory (UC).
    * On Prod/Con test, select Host memory options and uncheck Uncacheable. 
    * Click OK
    * Save the file 
    * kick off the test 

* Install and run ETD Tool
    * tar zxvf LinuxMG_2.000_archive.tar.gz 
    * cd Linux MG_2.000_archive # ./setup 
    * ./start_ driver (optional step)
    * /MG 

    * Check the error log of ETD 2000 Meatgrinder. 
    * Check the System Event Viewer of Windows
    * Error is found in var/log/message. 
    * No error is found in BIOS event log. 
    * No error is found in IML or ILO log. 
    * CPU usage is approximate 100% 
Total: 26 




# PCIe Link Optimization Test 
PCIe is used to provide the connections between motherboard peripherals like graphics card, ethernet card,external graphics card, external hard disk to the CPU and main memory.
PCIe is a packet-based serial bus, provides a high-speed, high-performance, point-to-point, dual simplex, differential signaling Link for interconnecting devices.
高速傳輸介面. 第一，PCIe資料交易的傳遞模式，是採用三個階層：資料交易層—資料鏈結層—實體層。第二，資料通訊的概念，與一般貨運的概念是一致的。類

當初PCIe架構的開發目標，就是提供晶片至晶片的連線，與配接卡的輸出入連線功能，或做為PCIe與其他連線的輸出入連接點(Attach Point)，例如PCI、1394(FireWire)與USB等。

PCIe以**串列**通訊系統為個人電腦(PC)內部的匯流排提供更快的傳輸速率. **平行式**先進附加介面(PATA)的SATA匯流排，其主要功能是在於主機板和大量儲存裝置(如硬碟和光碟機)之間的數據傳輸之用。


[![interface introduction](https://yt-embed.herokuapp.com/embed?v=NbL231dhnKs)](https://www.youtube.com/watch?v=NbL231dhnKs)

## Basic Set ECC Threshold for Memory Events to Zero (23 steps)

* RBSU option to set Default system settings
* disable iLO Security 
* Set RBSU to match test set config details: 
    6 test set config
* *For Gen 10*
    SET EV (requires EV.EFI - UEFI shell executible tool available from CSI tool/FTP or ROMQA):
        At UEFI shell prompt: map -r
        $ EV CQHSIGTH 01 01 00 01 00   
        $ EV CQHLKRATE 01   
        $ EV CQHMEMTHR 01 00 01 00 01 00 30 00 32 00 64 00 
        4 steps

* *DOS (Legacy mode) platforms:*
    SET EV (requires EV_VINE.COM - DOS tool): 
        Boot to DOS using USB key. 
        Run EV_VINE.COM. 
        Select Add to add an EV.
        Enter the Environment Variable as: CQHOVRD
        Enter the Hex Value as: 01 00 01 00 01 00 00 00 00 00 00 00 00 00
        5 steps

* *UEFI Platforms:*
    SET EV (requires EV.EFI - UEFI shell executible tool available from CSI tool/FTP or ROMQA): 
        At UEFI shell prompt: map -r 
        $ ev cqhovrd 01 00 01 00 05 00 00 00 00 00 00 00 00 00
        2 steps
* reboot
* Install associated Prolaint Support Pack 
* Check if Date/time set on the system's operating system and  ILO date time if match. 
* Verify initial state of SUT

total 23
## Copy Files && Remove Old Files (2 steps)
## Set PLOT-LIN to run on boot.(10 steps)
    
    For RHEL: 
        * $ /PLOT/RHEL8/setup.sh '-d 30 -t 60 -u' 
        * Add * /PLOT/PLOT-LIN & * to the end
        * $ chmod +x /etc/rc.d/rc.local
    For Ubuntu:
        * Add * /PLOT/PLOT-LIN & * above "exit 0" in "/etc/rc.local"
    For SLES 15+: 
        * $ /PLOT/RHEL8/setup.sh '-d 30 -t 60 -u' 
    For Sles12 +
        * Add * /PLOT/PLOT-LIN & * to the end
        * $ chmod +x /etc/init.d/boot.local
## install OS (1 steps)
## Verify initial report (1)
## Run PLOT-LIN && Input number of hours to run program. && Continue the test by entering 1. (3 steps)
## allow test to complete (1)
## verify test(6)
Log.txt,ErrorReportXX.txt,dmesg, var/log/messages, no IML events occurred,no ILO events occurred, 
## save(1)
## After test cases completed - Check Logs and Capture &Send the AHS log (9 steps)
verify all OS logs, IML logs, ILO logs, OA logs. If agents/providers are installed check HP System Management Homepage.
Capture the AHS log file: 
    Log in to iLO web page, go to the path Information -> Active health system logs and click the "Download" button to download all Active Health system logs. 




# Server Stress - Windows - PLOT OS Reboot
## Basic Set ECC Threshold for Memory Events to Zero (23 steps)
## install OS (1 step)
## Instructions for Windows without GUI (14 steps)
## Copy files (2 steps)
## Remove old files (1 step)
## Set PLOT-WIN to run on startup.+ Windows 10 Task Scheduler (17 steps)
## Enable automatic log in (5 steps)
## reboot (1 steps)
## Run PLOT-WIN.exe + input number of hours to run. (2 steps)
## Verify initial report (1)

## Continue the test by entering 1. (1 steps)
## Allow test to complete (1)
## verify test (3)
## save (1)
## call 9 



# STM linkpack (45)
## Basic Set ECC Threshold for Memory Events to Zero (23 steps)
## OS setup (3)
    * Install SLES 12 SP2 x64
    * select the installation of C/C++ Compiler and Tools
    * deselect the installation of Novell App Armor 
## SW Installation- Install the 3 rpms (1)
## SW Configuration (1)
## HASP Config (4)
    * Copy the aksusbd file to /opt/hpe/SystemTestManager
    * $ mount --bind /dev/bus/ /proc/bus 
        sync 
        ln -s /sys/kernel/debug/usb/devices /proc/bus/usb/devices 
    * $ /opt/hpe/SystemTestManager/aksusbd &
    * $ cat /proc/bus/usb/devices | grep HASP 
## Run STM (1)
    * SystemTestManager> view 
## Start Testing (1)
## Log Collection (2)
## call 9 


# Intel HVM tools
* Download "Intel® HVM tools xx version Beta"
* Uninstall "shc_icx.xx version.tar.gz"
* Check under shc (System Health Check) toolkit.
    * 6 content
* Execute "run.sh" under "shc_icx.xx version".
* check result 