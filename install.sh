# install virtualenv

sudo apt-get install aptitude -y
sudo aptitude install build-essential python-dev libmysqlclient-dev -y
sudo apt-get install mysql-server -y
pip install virtualenv

source sql.sh

# enter admin password when prompted
# sudo mysql -u root -p
# echo "SELECT * FROM dreamteam_db" | mysql 
# --enter admin password
# CREATE USER 'dt_admin'@'localhost' IDENTIFIED BY 'dt2016';
# CREATE DATABASE dreamteam_db;
# GRANT ALL PRIVILEGES ON dreamteam_db . * TO 'dt_admin'@'localhost';

# sudo apt-get install python-pip -y
# cd fygroupproject
source Envs/my-venv/bin/activate
pip install -r dream-team/requirements.txt
flask db upgrade

export FLASK_CONFIG=development
export FLASK_APP=dream-team/run.py
flask run