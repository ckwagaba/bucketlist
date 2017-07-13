""" Test user goal class functionality """

import pytest

# importing from the class files
from functionality.user import *
from functionality.buckets import *
from functionality.goals import *

new_goal = Goal(fake_goal['description'], fake_goal['status'])

""" The different test cases """

def test_view_goal_info():
    goal_info = new_goal.view_info()
    # assert goal_info[description] == 

def test_update_goal_info():
    pass

def test_delete_goal():
    pass