# WriteFree-Backend
## Learn more on my [Website](https://sidpremkumar.com/writefree.html)
## Configure Database

#### Download MongoDB
https://docs.mongodb.com/manual/installation/

#### Initialize Mongo
```
mongod
```
#### Create Database
```
use WriteFreeDB
```
#### Import "application" collection
1. Download [MongoDB GUI](https://www.mongodb.com/products/compass) 
2. Connect to your local mongod instance (localhost:27017)
3. Click on WriteFreeDB. If you do not see it, click on "+ Create Database." Name database "WriteFreeDB". Name collection "application"
4. Click on "application" collection on the left. 
5. On the top tool bar click on "Collection" and "Import Data"
6. Import the application.json collection and the data should be populated


### Install Virtual Enviornment

#### Install Python 3 
```
brew install python3
```
#### Create Python3 virtual environment
```
python3 -m venv venv
```

### Starting Virtual Enviornment (required)

#### Activate virtual env:
```
source venv/bin/activate
```
#### Install Dependencies (need to be in the app folder)
```
pip install -r requirements.txt
```


## Run Application
```
cd into the app/ folder (cd .., cd .., cd app/)
FLASK_APP=app.py
flask run
```

## How to Run Test Cases
1. Switch to the unit-tests branch. (git checkout unit-tests)
2. Activate the virtual enviornment and install the dependencies (see above)
3. cd into the app/tests folder
````
pytest test_login.py -p no:warnings
````
#### Changing the number of Unit Tests
1. open test_login.py
2. naviage to line 108
3. Change x here
````
emails, names = create_emails(num_emails=x)
````
