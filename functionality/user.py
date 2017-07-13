""" user module """

# some fake data
fake_user = {'name': 'Colin', 'email': 'ckwagaba@gmail.com', 'password': 'pwd'}
fake_user_buckets = [
    {'name': 'Career', 'goals':[{'description': 'Join Andela fellowship cohort II', 'status': 1}], 'progress': 100, 'user': fake_user['name']},
    {'name': 'Lifestyle', 'goals':[{'description': 'Buy a Tesla', 'status': 0}], 'progress': 0, 'user': fake_user['name']}
]

class User(object):
    def __init__(self, user_name, user_email, user_password):
        self.user_name = user_name
        self.user_email = user_email
        self.user_password = user_password
        
    def create_user(self):
        return {'name': self.user_name, 'email': self.user_email, 'password': self.user_password}
        
    def create_bucket(self, bucket_name, bucket_goals, bucket_progress, bucket_user):
        return {'name': bucket_name, 'goals': bucket_goals, 'progress': bucket_progress, 'user': bucket_user}