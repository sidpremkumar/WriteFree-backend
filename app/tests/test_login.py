import os
import tempfile

import pytest
import json
from app import app
import mongomock
from pytest_mongodb.plugin import mongo_engine
from pytest import mark

import string
import random
import json

#TO RUN:
# cd into the test folder then run -> pytest test_login.py -p no:warnings
@pytest.fixture
def client():
    app.config['TESTING'] = True

    client = app.test_client()

    yield client


#create random ID for the email
def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def create_account(client, email, fullName, password):
    data = {
        'email':email,
        'fullName':fullName,
        'password':password
    }
    return client.post('/create-account',query_string=data)

#loging in
def login(client, email, password):
    data = {
        'email':email,
        'password':password
    }
    return client.get('/login',query_string=data)

#helper method to get  default settings
def get_default_settings(client, email,x):
    header = {
        'Authorization': 'Bearer {}'.format(jwt_tokens[x])
    }
    return client.get('/get-default-settings',headers=header)

#helper method to update default settings
def update_default_settings(client, email,x):
    header = {
        'Authorization': 'Bearer {}'.format(jwt_tokens[x])
    }
    data = {
        'email': email,
        'noteColor': '#8bc34a',
        'applicationColor' : '#8bc34a',
        'fontName': 'Georgia',
        'fontSize': 11
    }
    data1 = {
        'body' : data
    }
    data2 = json.dumps(data1)
    return client.post('/update-default-settings',headers=header, data=data2,content_type='application/json')

#helper method to create new note
def create_new_note(client, x):
    header = {
        'Authorization': 'Bearer {}'.format(jwt_tokens[x])
    }
    return client.get('/new-note',headers=header)

def save_new_note(client, x):
    with open('formdata.json') as f:
        data = json.load(f)
    header = {
        'Authorization': 'Bearer {}'.format(jwt_tokens[x])
    }
    return client.post('/save-note', headers=header, data=json.dumps(data))


#Helper method to get data
def get_data(client, x):
    data = {
        'Authorization': 'Bearer {}'.format(jwt_tokens[x])
    }
    return client.get('/get-data',headers=data)


#helper method to create fake users
def create_emails(num_emails):
    emails = []
    names = []
    base = "@gmail.com"
    for x in range(num_emails):
        temp = id_generator() + base
        emails.append(temp)
        names.append(id_generator())
    return emails, names

#GLOBAL VARIABLES: Users:
emails, names = create_emails(num_emails=10)
jwt_tokens = []

#TEST 1: Testing the creation of accounts
def test_createAccount(client):
    for x in range(len(emails)):
        email = emails[x]
        name = names[x]
        rv= create_account(client, email, name, "test1234!")
        assert rv.status_code==200

#TEST 2: Testing login into said accounts
def test_login(client):
    for x in range(len(emails)):
        email = emails[x]
        rv= login(client, email, "test1234!")
        #save the jwt token created
        temp = rv.json
        jwt_tokens.append(temp['access_token'])
        assert rv.status_code==200

#TEST 3: Update default settings
def test_update_default_settings(client):
    for x in range(len(emails)):
        email = emails[x]
        rv = update_default_settings(client, email, x)
        assert rv.status_code==200


#TEST 4: Creating new note
def test_createNewNote(client):
    for x in range(len(emails)):
        rv = create_new_note(client, x)
        print(rv)
        assert rv.status_code==200

#TEST 5: Saving the note we created
def test_saveNewNote(client):
    for x in range(len(emails)):
        rv = save_new_note(client,x)
        assert rv.status_code==200

#TEST 6: Get-Data
def test_getData(client):
    for x in range(len(emails)):
        rv = get_data(client, x)
        assert rv.status_code==200






