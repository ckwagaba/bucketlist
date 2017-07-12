""" Test user bucket class functionality """

# importing the test library
import pytest

# importing from the class files
from functionality.user import User
from functionality.buckets import Bucket
from functionality.goals import Goal

initial_progress = 0

# test bucket creation
def test_create_bucket():
    new_bucket = Bucket('Career', initial_progress)
    assert new_bucket.create_bucket() == {'bucket_name': 'Career', 'bucket_progress': 0} # initially there's zero progress
    
def test_view_bucket():
    pass
    
def test_update_bucket():
    pass
    
def test_delete_bucket():
    pass