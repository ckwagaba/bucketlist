""" Test user user class functionality """

# importing the test library
import pytest

# importing from the class files
from functionality.user import *
from functionality.buckets import *
from functionality.goals import *

""" The different test cases """

# some fake data
fake_user = {'name': 'Colin', 'email': 'ckwagaba@gmail.com', 'password': 'pwd'}
new_user = User(fake_user['name'], fake_user['email'], fake_user['password'])

def test_new_user_creation():
    assert isinstance(new_user, User)
    
    # test return of user info
    assert new_user.create_user() == fake_user
    assert new_user.user_name == 'Colin'
    
def test_non_empty_string_input():
    pass