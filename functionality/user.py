""" user module """

# some fake data
fake_user_buckets = [
    {'name': 'Career', 'goals':[{'description': 'Join Andela fellowship cohort II', 'status': 1}], 'progress': 100, 'user': 'Colin'},
    {'name': 'Lifestyle', 'goals':[{'description': 'Buy a Tesla', 'status': 0}], 'progress': 0, 'user': 'Colin'}
]
fake_user = {'name': 'Colin', 'email': 'ckwagaba@gmail.com', 'password': 'pwd', 'buckets': fake_user_buckets}

class User(object):
    def __init__(self, user_name, user_email, user_password, user_buckets = []):
        self.user_name = user_name
        self.user_email = user_email
        self.user_password = user_password
        self.user_buckets = user_buckets
        
    def create_user(self):
        return {'name': self.user_name, 'email': self.user_email, 'password': self.user_password, 'buckets': self.user_buckets}
        
    def create_bucket(self, new_bucket):
        self.user_buckets.append(new_bucket)
        
    def delete_bucket(self, bucket_to_delete):
        counter = 0
        for i in self.user_buckets:
            if i['name'] == bucket_to_delete:
                self.user_buckets.pop(counter)
                break
            else:
                counter += 1