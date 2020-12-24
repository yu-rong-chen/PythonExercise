import time
import winrm
import logging


def destroy_host_from_vcenter(vip, vid, vpwd, hip):
    wip = '10.10.1.20'
    wid = 'Administrator'
    wpwd = 'Compaq123'
    lc = """
    $re = Import-Module VMware.VimAutomation.Core -PassThru
    $re = Connect-VIServer -Server %s -User %s -Password %s -Force
    try {
        $re = Remove-VMHost %s -Confirm:$false -ErrorAction Stop
        Write-Host "pass".ToString().Trim()
    }
    catch {
        Write-Host "Fail".ToString().Trim()
    }
    """
    lc = lc % (vip, vid, vpwd, hip)
    try:
        s = winrm.Session(wip, auth=(wid, wpwd))
        r = s.run_ps(lc)
        result = r.std_out.strip()
        logger.info(result)
        # print(Nice to meet you, +result)

    except Exception as e:
        logger.info(str(e))
        print(Sorry, +str(e))

def add_host_to_vcenter(vip, vid, vpwd, hip, hid, hpwd):
    logger.info("add host %s to vcenter %s" % (hip, vip))
    with connect_viserver(vip, vid, vpwd) as s:
        # 'VMware vCenter Server'
        # 'VMware ESXi'
        if "vCenter" not in s.get_server_type():
            msg = "Host [%s] is not a vCenter server" % vip
            logger.error(msg)
            raise Exception(msg)

        # Check if host already managed by vCenter
        for mor, name in s.get_hosts().items():
            if name == hip:
                msg = "Skip add host [%s], already exists."
                msg = msg % str(name)
                logger.info(msg)
                msg = "Reconnect host [%s] again."
                msg = msg % str(name)
                logger.info(msg)
                req = VI.ReconnectHost_TaskRequestMsg()
                mor = next((key for key, value in list(s.get_hosts().items()) if value == hip)) # noqa

                sys = VIMor(mor, "HostSystem")
                _this = req.new__this(sys)
                _this.set_attribute_type(sys.get_attribute_type())
                req.set_element__this(_this)

                spec = req.new_cnxSpec()
                spec.Force = True
                spec.HostName = hip
                spec.UserName = hid
                spec.Password = hpwd
                spec.SslThumbprint = getssl(hip)
                req.set_element_cnxSpec(spec)

                task_mor = s._proxy.ReconnectHost_Task(req)._returnval
                vi_task = VITask(task_mor, s)
                status = vi_task.wait_for_state([vi_task.STATE_SUCCESS,
                                                 vi_task.STATE_ERROR])
                if status == vi_task.STATE_ERROR:
                    msg = "Error reconnecting host: %s" % vi_task.get_error_message()
                    logger.error(msg)
                    raise Exception(msg)
                else:
                    logger.info("Host reconnected %s " % vi_task.get_result())
                return

        dc_mor = [mor for mor, name in s.get_datacenters().items()][0]
        request = VI.AddStandaloneHost_TaskRequestMsg()
        dc_props = VIProperty(s, dc_mor)
        hf_mor = dc_props.hostFolder._obj  # group-h4
        _this = request.new__this(hf_mor)
        _this.set_attribute_type(hf_mor.get_attribute_type())  # Folder
        request.set_element__this(_this)
        # should the host be connected immediately after it is added
        request.set_element_addConnected(True)
        spec = request.new_spec()
        # connection succeeds even if the host is managed by another VC
        spec.Force = True
        spec.HostName = hip
        spec.UserName = hid
        spec.Password = hpwd
        spec.SslThumbprint = getssl(hip)
        request.set_element_spec(spec)

        task = s._proxy.AddStandaloneHost_Task(request)._returnval
        vi_task = VITask(task, s)
        status = vi_task.wait_for_state([vi_task.STATE_SUCCESS,
                                         vi_task.STATE_ERROR])
        if status == vi_task.STATE_ERROR:
            msg = "Error adding host: %s" % vi_task.get_error_message()
            logger.error(msg)
            raise Exception(msg)
        else:
            logger.info("Host added %s " % vi_task.get_result())



vip = '10.10.1.70'
vid = 'administrator@vsphere.local'
vpwd = 'Compaq@123'
hip = '10.10.41.38'
hid = 'root'
hpwd = 'Compaq@123'
logger = logging.getLogger('vtc.core_plugins.vmware')

# add_host_to_vcenter(vip, vid, vpwd, hip, hid, hpwd)
destroy_host_from_vcenter(vip, vid, vpwd, hip)