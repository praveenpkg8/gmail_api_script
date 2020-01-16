## Design and implemenation of python script on specific task using gmail API


To work on the project git clone it and change directory to it. 
Open terminal do the following commands
```
git clone https://github.com/praveenpkg8/gmail_api_script.git
cd gmail_api_script
```

Inorder to run the project your system must have python3 install. To download python3 press [here](https://www.python.org/downloads/)

Once installing python3. have to create a virtual environment and activate it do the following commands. It would create the
virtual environment for the project
```
python3 -m venv env
. env/bin/activate
```
to install the dependency for the project, perform the following command.
```
pip install -r requirements.txt
```
Get credential.json file after enabling it from gmail api of your desired gmail account. 
For credentials download press [link](https://developers.google.com/gmail/api/quickstart/python).
Click enable api button in step one and download `credentials.json` and move it to the working directory

### Populate database
populate the database with mails from you desired account. In order to populate the database perform the following command.
It would ask for a prompt of total number of mail that you  want to load to the database. just give a number more than 100 for 
efficient data set.
```
python populate_database.py
```

### Modify Input actions
Modify input action according to your specifics by updating the `input.json` file.
Once you have done your entire predicate set you can perform the task.

### Run Task
After updating the `input.json` file. Run the following command to perform the task.
```
python main.py 
```
All actions mentioned in the following `input.json` file would be performed.


### Thanks for having a look at it.


