""" Test user bucket class functionality """

# importing the test library
import pytest

# importing from the class files
from functionality.user import *
from functionality.buckets import *
from functionality.goals import *

new_bucket = Bucket(fake_bucket['name'], fake_bucket['goals'], fake_bucket['owner'], fake_bucket['progress'])

""" The different test cases """

def test_add_goal():
    new_goal = {'description': 'Rally drive', 'bucket': 'Fun', 'status': 0}
    new_bucket.add_goal(new_goal)
    assert len(new_bucket.bucket_goals) == 3

def test_view_goals():
    bucket_goals = new_bucket.view_goals()
    assert bucket_goals == [
        {'description': 'Join Andela fellowship cohort II', 'bucket': 'Career', 'status': 1},
        {'description': 'Buy a Tesla', 'bucket': 'Lifestyle', 'status': 0},
        {'description': 'Rally drive', 'bucket': 'Fun', 'status': 0}
    ]

def test_delete_goal():
    goal_to_delete = 'Buy a Tesla'
    new_bucket.delete_goal(goal_to_delete)
    assert len(new_bucket.bucket_goals) == 2

def test_update_bucket_name():
    new_name = 'Tech'
    bucket_name = new_bucket.update_name(new_name)
    assert new_bucket.bucket_name == new_name
    
def test_update_bucket_progress():
    bucket_goals = new_bucket.bucket_goals
    bucket_progress = new_bucket.update_progress(bucket_goals)
    assert new_bucket.bucket_progress == (1 / 2)