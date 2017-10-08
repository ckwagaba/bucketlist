""" bucket module """

# create some fake data for testing
fake_goals = [
    {'description': 'Join Andela fellowship cohort II', 'bucket': 'Career', 'status': 1},
    {'description': 'Buy a Tesla', 'bucket': 'Lifestyle', 'status': 0}
]
fake_bucket = {'name': 'Career', 'goals': fake_goals, 'owner': 'Colin', 'progress': 100}

class Bucket(object):
    def __init__(self, bucket_name, bucket_goals, bucket_owner, bucket_progress = 0):
        self.bucket_name = bucket_name
        self.bucket_progress = bucket_progress
        self.bucket_goals = bucket_goals
        self.bucket_owner = bucket_owner
        
    def create_bucket(self):
        return {'name': self.bucket_name, 'goals': self.bucket_goals, 'owner': self.bucket_owner, 'progress': self.bucket_progress}
        
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
                
    def update_progress(self, bucket_goals):
        achieved = 0
        for i in bucket_goals:
            if i['status'] == 1:
                achieved += 1
        
        new_progress = (achieved / len(bucket_goals))
        self.bucket_progress = new_progress