# SPP - (SPP - Guided Update - Interactive - Online Vmware) - 3516794
Question:
1. What is SPP?
2. What is SPP use for?

## Step1 - Pre-Requisites
* Get latest SPP build
* Refer to SUM User Guide/help files
* Both host and client should be in same network domain 
* For VMware OS installed on Gen10 server, install **iSUT** and set it to 'AutoDeployreboot' mode 

    * Install appropriate **vib** for iSUT (Steps a,b,c,d)
* It should be in maintenance mdoe 

## Step2 - Mount/copy the SPP Build
* mount SPP build using iLo 
* (mount the .ISO file and explore its contents.)

## Step3 - Add Web browser security Certificate
* Extract latest SPP Build and pick Security certificae CA.crt.
* Steps to Import certificate to **firefox** browser: 
* Steps to Import certificate to **chrome** browser: 
* Steps to Import certificate to Internet Explorer browser: 

## Step4 - Launch SUM (Smart Update Manager) (Linux or Windows Client)

## Step5 - Welcome Screen should appear
## Stpe6 - Click on "Node" icon
## Step7 - Add Node
* Nodes:
* Baseline to apply..
## Step8 - Inventory
* click on "Action" button and Select "Inventory" 

## Step9 - Review
* Click on Review and deploy updates button. Verify all the components listed for applicable target. 

## Step10 - Click on Deploy button. 
## Step11 - Review
## Step 12: Verify SUM Logs
## Step13 - reboot the target Server by clicking "Reboot Now".  
## Step14 - Verify the firmware versions updated.
## Step 15: POST Install Verification
## Step16 - Make sure valid network IP is being assigned by DHCP to all ports of each NIC. 

## Test parameter
* win_remote.txt
* lin_remote.txt
* http address of SPP image 
* Enter Remote IP, Remote username, Remote password. [Here details of VMware server under test]

# SPP - Guided Update - Interactive - Online Linux - 3333
* Step 2: OS Installation
    * use **KISO** for any SLES OS
    * If the server has network card that support enablement kit then install all libHBAAPI package while installing OS to avoid dependency error during flasing SPP. e.g SN1600E card 
* Step3 : post os installation
    * On Gen10 servers, Install Errata Kernel in RHEL 7.3 OS 
    *  Install net-tools-depricated package in SLES15/SP1 OS 

# SPP windows
* double click .bat file will Launch SUM automatically)
* Need to uninstall SPP at the end of step
* reference from Internet
    [![windows](https://www.wintips.org/wp-content/uploads/2018/10/image-44.png)](https://www.youtube.com/watch?v=pHKHLnUqwHA)

    [Reference update SPP](https://www.wintips.org/how-to-use-hp-smart-update-manager-to-update-proliant-server/# "SPP update")

    [![windows](https://yt-embed.herokuapp.com/embed?v=pHKHLnUqwHA)](https://www.youtube.com/watch?v=pHKHLnUqwHA)