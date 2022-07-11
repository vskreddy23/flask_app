# flask_app
Basic flask app with SPA.

Steps to setup Project

- Check latest python is installed.(To check type python in terminal)

- Install pip, python-dev and build-essential

Following steps are to create virtualenv using virtualenvwrapper.

- Install virtualenv and virtualenvwrapper
  
  sudo pip install virtualenv virtualenvwrapper

- Add below line to last line of ~/.bashrc file
  
  source /usr/local/bin/virtualenvwrapper.sh

- After saving bashrc, reload bash.
  
  source ~/.bashrc

- Upgrade pip (optional)
  
  sudo pip install --upgrade pip

- cd to django project's directory

- Make new virtualenv
  
  mkvirtualenv empereon_env

- set root path for this virtualenv
  
  setvirtualenvproject

Install project requirements

- Install all required packages.
pip install -r requirements.txt

- Run server
python app.py
