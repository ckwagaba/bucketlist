""" user module """

# some fake data
fake_user_buckets = [
    {'name': 'Career', 'goals':[{'description': 'Join Andela fellowship cohort II', 'bucket': 'Career', 'status': 1}], 'owner': 'Colin', 'progress': 100},
    {'name': 'Lifestyle', 'goals':[{'description': 'Buy a Tesla', 'bucket': 'Lifestyle', 'status': 0}], 'owner': 'Colin', 'progress': 0}
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
                
    def login(self, email, password):
        if email == self.user_email and password == self.user_password:
            return 1
        else:
            return 0
    
    def logout(self):
        self.user_name = None
        self.user_email = None
        self.user_password = None