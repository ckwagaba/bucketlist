""" bucket module """

# create some fake data for testing
fake_goals = [
    {'description': 'Join Andela fellowship cohort II', 'status': 1},
    {'description': 'Buy a Tesla', 'status': 0}
]
fake_bucket = {'name': 'Career', 'goals': fake_goals, 'progress': 100}

class Bucket(object):
    def __init__(self, bucket_name, bucket_goals, bucket_progress = 0):
        self.bucket_name = bucket_name
        self.bucket_progress = bucket_progress
        self.bucket_goals = bucket_goals
        
    def view_goals(self):
        return self.bucket_goals
        
    def update_name(self, new_name):
        self.bucket_name = new_name
        
    def add_goal(self, new_goal):
        self.bucket_goals.append(new_goal)
        
    def delete_goal(self, goal_to_delete):
        counter = 0
        for i in self.bucket_goals:
            if i['description'] == goal_to_delete:
                self.bucket_goals.pop(counter)
                break
            else:
                counter += 1