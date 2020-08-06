For example, I have two identical SUT:

Product Name: ProLiant DL380 Gen10
CPU: 2 socket, 32 cores(64 threads) Intel(R) Xeon(R) Gold 6130 CPU @ 2.10GHz
Memory: 256GB
PMEM:32 GB
Storage: 2.06 TB
Network: vmnic0 for QLogic Inc. QLogic 57810 10 Gigabit Ethernet Adapter and vmnic1 for QLogic Inc. QLogic 57810 10 Gigabit Ethernet Adapter

Available VM on Xorsyst test: 
    VM Number per 2 Physical Core is 1, so user can deploy 64/2*1=32 VMs at most on one SUT base on CPU restriction.
    VM Number per 10G NIC is 5, so user can deploy 5 VMs at most on one SUT base on NIC restriction.
    So combining the above condition, user can deploy 5 VMs (8 cores,8GB memory, 20GB HDD) at most on one SUT.

Available VM on BigVM test: 
    VM Number per 2 Physical Core is 4, so user can deploy 64/2*4=128 VMs at most on one SUT base on CPU restriction.
    VM Number per 10G NIC is 16, so user can deploy 16 VMs at most on one SUT base on NIC restriction.
    So combining the above condition, user can deploy 16 VMs (4 cores,4GB memory, 20GB HDD) at most on one SUT.

Available VM on POLX test: 
    VM Number per 2 Physical Core is 4, so user can deploy 64/2*4=128 VMs at most on one SUT base on CPU restriction.
    VM Number per 10G NIC is 16, so user can deploy 16 VMs at most on one SUT base on NIC restriction.
    So combining the above condition, user can deploy 16 VMs (4 cores,4GB memory, 20GB HDD) at most on one SUT.

Available VM on SCX test: 
    VM Number per 2 Physical Core is 1, so user can deploy 64/2*1=32 VMs at most on one SUT base on CPU restriction.
    VM Number per 10G NIC is 6, so user can deploy 6 VMs at most on one SUT base on NIC restriction.
    So combining the above condition, user can deploy 6 VMs (8 cores,8GB memory, 20GB HDD) at most on one SUT.


