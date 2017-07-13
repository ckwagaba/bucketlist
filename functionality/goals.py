""" goal module """

# create some fake data for testing
fake_goal = {'description': 'Join Andela fellowship cohort II', 'bucket': 'Career', 'status': 1}

class Goal(object):
    def __init__(self, goal_description, goal_bucket, goal_status = 0):
        self.goal_description = goal_description
        self.goal_status = goal_status
        self.goal_bucket = goal_bucket
    
    def view_info(self):
        return {'description': self.goal_description, 'bucket': self.goal_bucket, 'status': self.goal_status}
        
    def update_description(self, new_goal_description):
        self.goal_description = new_goal_description
        
    def update_status(self, new_goal_status):
        self.goal_status = new_goal_status