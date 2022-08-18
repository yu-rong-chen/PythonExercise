# Login using SSH key
## SSH protocal
> The SSH (Secure Shell) protocal is a method for secure remote login from one computer to another.
> It provides several alternative options for strong authentication, and it protects the communications security and integrity with strong encryption.
> This protocal works in the client-server model, which means that connection is established by SSH client connect to SSH server.
## SSH key
> An SSH key is an access credential, similar to password, used in SSH protocal.
> The idea is to have a cryptographic key pair - public key and private key - and configure the public key on a server to authorize access and grant anyone who has a copy of the private key access to the server.
### Generate ssh key on linux
<p>Generating public/private rsa key pair in <code>~/.ssh</code>.
<pre><code>ssh-keygen</code></pre>

   * Generating multiple public/private rsa key pair:`ssh-keygen -C $github_mail`
   * start ssh-agent before you run the ssh-add command: <prep><code>eval `ssh-agent -s`</code></prep>
   * If you see *Permission denied (publickey).*, please add your SSH (private) key to the ssh-agent: `ssh-add ~/.ssh/github/id_rsa`.
   * Check with `ssh -vT git@github.com`

<p>This command will generate two file <code>id_rsa</code> and <code>id_rsa.pub</code> in <code>~/.ssh</code> folder. Public key will generate in <code>id_rsa.pub</code>. It will be put on remote linux server which user want to access. User can distinguish from the file name <code>.pub</code>. There are two ways to put pulic key to remote linux server.

1. <p>Copy the content of <code>id_rsa.pub</code> to <code>~/.ssh/authorized_keys</code></p>
   <prep><code>ssh USER@HOST 'mkdir -p ~/.ssh;cat >> ~/.ssh/authorized_keys' < ~/.ssh/id_rsa.pub</code></prep>
2. <p>Using comand <code>ssh-copy-id</code>
   <prep><code>ssh-copy-id USER@HOST</code></prep>
   
      > set `PasswordAuthentication yes` in /etc/ssh/ssh_config first
   
   <prep><code>ssh-copy-id -i ~/.ssh/id_rsa.pub -p PORTs USER@HOST</code> to specify the key</prep>

<p>The more safer way for SSH login is forbidden using password to login and only allow login by ssh key. Change the setting in <code>/etc/ssh/sshd_config</code>
<pre><code>PasswordAuthentication no
PubkeyAuthentication yes</code></pre> 
<p>Restart <code>sshd</code>. <code>/etc/init.d/sshd restart</code>

Reference from [ssh.com](https://www.ssh.com/ssh/protocol "SSH key")

## Open remote windows on visual code

### install OpenSSH on client
Option 1:

Settings -> APP -> APP & Feature -> Manage optional features -> Add a feateure -> Install OpenSSH client

Option 2:

Install using powershell

[Reference](https://docs.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse "Microsoft Document")

### Make sure remote VM can use command wget

$cat > ~/.wgetrc
use_proxy = on
http_proxy = ....
https_proxy = ....

************
# git command
> User need to set account
> 
<prep><code>git config --global user.email "you@example.com"
git config --global user.name "Your Name"</code></prep>
<p>hook up the Git repository on your computer to the one up on GitHub
<prep><code>git remote add origin https://github.com/<your-github-username>/my-first-blog.git
git push -u origin master</code></prep>
