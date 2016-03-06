<H1> FSND P5 Linux based Server Configuration coursework </H1>
<H3>IP address and SSH port, URL</H3>
IP address is 52.37.60.152 and SSH port is 2200 </br>
URL :- http://52.37.60.152</br>
<H3> Step by step walkthrough </H3>
Basic Configuration:</br>
A project folder was formed and using vagrant up and then vagrant ssh, the virtual environment was launched. </br>
The private key supplied was downloaded, modified with chmod 600 and a connection established to the remote server </br>
[Digital Ocean -forming users](https://www.digitalocean.com/community/tutorials/how-to-add-and-delete-users-on-an-ubuntu-14-04-vps)</br>
adduser grader </br>
And new password downmix was set in the process </br>
Grader was then added to the list of sudo users via visudo command</br>
[Digital Ocean - generating ssh keys] (https://www.digitalocean.com/community/tutorials/how-to-configure-ssh-key-based-authentication-on-a-linux-server),/br>
ssh-keygen </br>
Keys generated on my remote machine - not logged in and then copied across to the relevant file on the server to allow SSH login.</br>
Copied from one terminal remote to terminal in server the public key and put it in the file authorized keys</br>
Then rest the permissions for the .ssh folder and the authorized_keys files</br>
[Ask Ubuntu - updating and upgrading packages] (http://askubuntu.com/questions/196768/how-to-install-updates-via-command-line)</br>
sudo apt-get update        # Fetches the list of available updates </br>
sudo apt-get upgrade       # Strictly upgrades the current packages </br>
sudo apt-get dist-upgrade  # Installs updates (new ones) </br>
Packgages updated and upgraded.</br>
Located the sshd_config file and changed the ssh port to 2200</br>
Modified this file PermitRootLogin no </br>
[Ask Ubuntu - change time zone] (http://askubuntu.com/questions/138423/how-do-i-change-my-timezone-to-utc-gmt)</br>
sudo dpkg-reconfigure tzdata </br>
Time zone reset to UTC.</br>
[Help Ubuntu - config and enable UFW](https://help.ubuntu.com/community/UFW)</br>
sudo ufw enable </br>
sudo ufw allow 2200</br>
sudo ufw allow 80</br>
sudo ufw allow 123</br>
Uncomplicated FireWall set as required. </br>
[Help Ubunt -Installing Apache2] (https://help.ubuntu.com/community/ApacheMySQLPHP),/br>
sudo apt-get install apache2 </br>
Checked the ip address and sample page is showing, all in order </br>
sudo apt-get install python-setuptools libapache2-mod-wsgi </br>
sudo service apache2 restart </br>
[Digital Ocean - extending for Flask] (https://www.digitalocean.com/community/tutorials/how-to-deploy-a-flask-application-on-an-ubuntu-vps)</br>
Made the following file structure - /var/www/catalog/catalog/static template </br>
[Streuken - setting up environment] (https://github.com/stueken/FSND-P5_Linux-Server-Configuration)
Installed git and cloned the files across to the apache2server
As per the instructions in the above installed pip install, set virtual environemnt to venv,/br>
Activated the environment and installed flask</br>
sudo nano /etc/apache2/sites-available/catalog.conf # created the necessary catalog.conf file with the project details(IPs) </br>
sudo a2ensite catalog # and then enabled the virtual host</br>
Created the wsgi file and modified the secret key to match the detail in my catalog project </br>
Reading the error logs, I have "Could not reliably determine the servers's fully qualified domain name" after restart "</br>
[Ask Ubuntu - removing error message] (http://askubuntu.com/questions/256013/could-not-reliably-determine-the-servers-fully-qualified-domain-name)</br>
New file inserted with ServerName localhost (file called fqdn.conf)</br>
Note that within the referened instructions there is an instruction sudo su - postgre </br>
Which for this setup only works as such - sudo su - postgre -i </br>
On top of the Streuken instructions, the following extra steps need to be noted </br>
Within database_setup.py  and __init__.py files extra import lines need to be added </br>
from flask_sqlalchemy import SQLAlchemy </br>
All referenced installations for sqlalchemy, psycopg2 will not work on their own and need the following flask extensions installed</br>
And these packages need to be installed </bvr>
sudo apt-get install postgresql-server-dev-all</br>
sudo apt-get install libpq-dev python-dev </br>
[Stack Overflow - how to install psycopg2] (http://stackoverflow.com/questions/5420789/how-to-install-psycopg2-with-pip-on-python
)</br>
[PYPI -Flask exenstion for Psycopy2] (https://pypi.python.org/pypi/Flask-Psycopg2/1.3)</br>
[PYPI -Flask extension for SQLAlchemy] (https://pypi.python.org/pypi/Flask-SQLAlchemy/2.1)</br>
[PYPI -Flask extension for Oauth2] (https://pypi.python.org/pypi/flask-oidc/0.1.2) </br>
[Stack Overflow - alterations forJson required] (http://stackoverflow.com/questions/31168606/internal-server-error-target-wsgi-script-cannot-be-loaded-as-python-module-and) </br>
Following amendments need to be made to the __init__.py file </br>
APP_PATH = '/var/www/catalog/ </br>
CLIENT_ID = json.loads(open(APP_PATH + 'client_secrets.json', 'r').read())['web']['client_id']</br>
oauth_flow = flow_from_clientsecrets('client_secrets.json', scope='')</br>
to APP_PATH = ‘var/www/catalog/catalog/’</br>
oauth_flow = flow_from_clientsecrets(APP_PATH +'client_secrets.json', scope='')</br>
After this the google developers console was updated with the following addresses and all is functioning</br>
Authorised javascript origins - http://52.37.60.152 ,/br>
http://ec2-52.37.60.152.us-west-2.compute.amazonaws.com</br>
Authorized redirect URIs - http://ec2-52.37.60.152.us-west-2.compute.amazonaws.com/ouauth2callback </br>
















