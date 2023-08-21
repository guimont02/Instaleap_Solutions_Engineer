# Instaleap_Solutions_Engineer
Solutions Engineer Test for Instaleap

Setting Up and Starting the Flask Project

Installing and Activating the Virtual Environment (venv)
Before starting, it's advisable to use a virtual environment to ensure the project's dependencies don't interfere with other projects or the global system. Here's how you can set up and activate one:

For Unix/macOS-based systems:


python3 -m venv venv
source venv/bin/activate

For Windows:

python -m venv venv
.\venv\Scripts\activate

Installing Dependencies
After activating the virtual environment, install the project dependencies (if any):

pip install -r requirements.txt

If you don't have a requirements.txt file yet, you can create one using pip freeze > requirements.txt after having installed all necessary libraries.

Running the Project
With the virtual environment activated and dependencies installed, you can start the Flask project:

python app.py
