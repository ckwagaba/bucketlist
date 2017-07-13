""" Test user user class functionality """

# importing the test library
import pytest

# importing from the class files
from functionality.user import *
from functionality.buckets import *
from functionality.goals import *

""" The different test cases """

# creating instances with fake data
new_user = User(fake_user['name'], fake_user['email'], fake_user['password'])
user_bucket = new_user.create_bucket(fake_user_bucket['name'], fake_user_bucket['goals'], fake_user_bucket['progress'], fake_user_bucket['user'])

def test_new_user_creation():
    assert isinstance(new_user, User)
    
def test_return_of_user_object():
    assert new_user.create_user() == fake_user
    
def test_user_name():
    assert new_user.user_name == 'Colin'
    
def test_non_empty_name_input():
    assert new_user.user_name != None

def test_create_bucket():
    assert user_bucket == fake_user_bucket
    
def test_non_empty_bucket_name():
    assert user_bucket['name'] != None

def test_login():
    pass

def test_logout():
    pass