""" Test user bucket class functionality """

# importing the test library
import pytest

# importing from the class files
from functionality.user import *
from functionality.buckets import *
from functionality.goals import *

new_bucket = Bucket(fake_bucket['name'], fake_bucket['goals'], fake_bucket['progress'])

""" The different test cases """

def test_add_goal():
    new_goal = {'description': 'Rally drive', 'status': 0}
    new_bucket.add_goal(new_goal)
    assert len(new_bucket.bucket_goals) == 3

def test_view_goals():
    bucket_goals = new_bucket.view_goals()
    assert isinstance(bucket_goals, list)
    assert bucket_goals == [
        {'description': 'Join Andela fellowship cohort II', 'status': 1},
        {'description': 'Buy a Tesla', 'status': 0},
        {'description': 'Rally drive', 'status': 0}
    ]

""" def test_delete_goal():
    goal_to_delete = 'Buy a Tesla'
    new_bucket.delete_goal(goal_to_delete)
    assert len(new_bucket.bucket_goals) == 2 """

def test_update_bucket_name():
    new_name = 'Tech'
    bucket_name = new_bucket.update_name(new_name)
    assert new_bucket.bucket_name == new_name