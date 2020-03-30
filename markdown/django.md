# Django
## Installation
### virtual environment
>Create a virtual environment(also called virtualenv) that can isolate your Python/Django setup on a per-project basis. It means virtualenv allow you to manage separate package installations for different projects. You can create a “virtual” isolated Python installation and install packages into that virtual installation. When you switch projects, you can simply create a new virtual environment and not have to worry about breaking the packages installed in the other environments. 
<p>Install virtualenv<prep><code>apt-get install python3-venv</code></prep> 
<p>Create a virtual environment<prep><code>python3 -m venv _*env*_</code></prep>
<p>Activate a virtual environment<prep><code>source "env"/bin/activate</code></prep>
<p>Leave the virtual environment<prep><code>deactivate</code></prep>
<p>uprade <code>pip</code> to latest version<prep><code>pip --proxy _*http://web-proxy.sgp.hpecorp.....*_ install --upgrate pip</code></prep>

### deploy on Internet
<p>Ignore some file from git tracking
    <p>Create <code>.gitignore</code> where <code>manage.py</code> located