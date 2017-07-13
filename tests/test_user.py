""" Test user user class functionality """

# importing the test library
import pytest

# importing from the class files
from functionality.user import *
from functionality.buckets import *
from functionality.goals import *

""" The different test cases """

# creating instances with fake data
new_user = User(fake_user['name'], fake_user['email'], fake_user['password'], fake_user['buckets'])
    
def test_create_user():
    assert new_user.create_user() == fake_user

def test_create_bucket():
    new_bucket_goals = [{'description': 'Bungee jump', 'status': 0}]
    new_bucket = {'name': 'Fun', 'goals': new_bucket_goals, 'progress': 0}
    new_user.create_bucket(new_bucket)
    assert len(new_user.user_buckets) == 3
    
def test_delete_bucket():
    bucket_to_delete = 'Career'
    new_user.delete_bucket(bucket_to_delete)
    assert len(new_user.user_buckets) == 2

def test_login():
    pass

def test_logout():
    pass