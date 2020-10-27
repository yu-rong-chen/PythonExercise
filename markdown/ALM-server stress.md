# Content

[Network testing](#Network-testing)

[Xorsyst](#Xorsyst)

[Thread Starvation Test](#Thread-Starvation-Test)

[Meatgrinder](#Meatgrinder)

[STM linkpack](#STM-linkpack)

[Intel HVM tools](#intel-hvm-tools)

[PCIe Link Optimization Test](#PCIe-Link-Optimization-Test)

# Network testing
## Configuration Counts
* SUT1 IP, username and password
* SUT2 IP, username and password
* runtime 1440

Total: 7
## Xorsyst setup on both client and SUT
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

Total: 7+ 7X2+7= 28.

# Xorsyst
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

# PCIe Link Optimization Test 
PCIe is used to provide the connections between motherboard peripherals like graphics card, ethernet card,external graphics card, external hard disk to the CPU and main memory.
PCIe is a packet-based serial bus, provides a high-speed, high-performance, point-to-point, dual simplex, differential signaling Link for interconnecting devices.
高速傳輸介面. 第一，PCIe資料交易的傳遞模式，是採用三個階層：資料交易層—資料鏈結層—實體層。第二，資料通訊的概念，與一般貨運的概念是一致的。類

當初PCIe架構的開發目標，就是提供晶片至晶片的連線，與配接卡的輸出入連線功能，或做為PCIe與其他連線的輸出入連接點(Attach Point)，例如PCI、1394(FireWire)與USB等。

PCIe以**串列**通訊系統為個人電腦(PC)內部的匯流排提供更快的傳輸速率. **平行式**先進附加介面(PATA)的SATA匯流排，其主要功能是在於主機板和大量儲存裝置(如硬碟和光碟機)之間的數據傳輸之用。


[![interface introduction](https://yt-embed.herokuapp.com/embed?v=NbL231dhnKs)](https://www.youtube.com/watch?v=NbL231dhnKs)

## Basic Set ECC Threshold for Memory Events to Zero

* RBSU option to set Default system settings
* disable iLO Security 
* Set RBSU to match test set config details: 
    6 test set config
* *For Gen 10*
    SET EV (requires EV.EFI - UEFI shell executible tool available from CSI tool/FTP or ROMQA):
        5 steps
* *DOS (Legacy mode) platforms:*
    SET EV (requires EV_VINE.COM - DOS tool): 
        5 steps
* *UEFI Platforms:*
    SET EV (requires EV.EFI - UEFI shell executible tool available from CSI tool/FTP or ROMQA): 
        3 steps
* reboot
* plus 3 steps

total 25
## plus 2 steps
## Set PLOT-LIN to run on boot.(10 steps)
## install OS (1 steps)
## Verify initial report (1)
## plus 3 steps
## allow test to complete (1)
## verify test(6)
Log.txt,ErrorReportXX.txt,dmesg, var/log/messages, no IML events occurred,no ILO events occurred, 
## save(1)
##call (5+6)
verify all OS logs, IML logs, ILO logs, OA logs. If agents/providers are installed check HP System Management Homepage.


### Windows - PLOT OS Reboot
## Basic Set ECC Threshold for Memory Events to Zero (25 steps)
### install OS (1 step)
### Instructions for Windows without GUI (14 steps)
### Copy files (2 steps)
### Remove old files (1 step)
### Set PLOT-WIN to run on startup.(17 steps)
### Enable automatic log in (5 steps)
### reboot (1 steps)
### Run PLOT-WIN.exe (1 steps)
### Verify initial report (1)
### plus 3 steps
### Allow test to complete (1)
### verify test (3)
### save (1)
### call 11


# Server Stress - Windows - PLOT OS Reboot

## Basic Set ECC Threshold for Memory Events to Zero (25)
## 
##call (5+6)


# STM linkpack

# Intel HVM tools
* Download "Intel® HVM tools xx version Beta"
* Uninstall "shc_icx.xx version.tar.gz"
* Check under shc (System Health Check) toolkit.
    * 6 content
* Execute "run.sh" under "shc_icx.xx version".
* check result 