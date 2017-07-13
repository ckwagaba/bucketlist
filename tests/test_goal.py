""" Test user goal class functionality """

import pytest

# importing from the class files
from functionality.user import *
from functionality.buckets import *
from functionality.goals import *

new_goal = Goal(fake_goal['description'], fake_goal['bucket'], fake_goal['status'])

""" The different test cases """

def test_view_goal_info():
    goal_info = new_goal.view_info()
    assert goal_info == fake_goal

def test_update_goal_description():
    new_goal_description = 'Join Andela tomorrow'
    new_goal.update_description(new_goal_description)
    assert new_goal.goal_description == new_goal_description
    
def test_update_goal_status():
    new_status = 2
    new_goal.update_status(new_status)
    assert new_goal.goal_status == new_status