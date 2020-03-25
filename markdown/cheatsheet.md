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
<pre><code>ssh-keygens</code></pre>
<p>This command will generate two file <code>id_rsa</code> and <code>id_rsa.pub</code> in <code>~/.ssh</code> folder. 

Reference from [ssh.com](https://www.ssh.com/ssh/protocol "SSH key")
************
# git command
> User need to set account
> 
<prep><code>git config --global user.email "you@example.com"

git config --global user.name "Your Name"</code></prep>
