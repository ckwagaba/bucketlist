""" Module contains user attributes and methods """

class User(object):
    
    # values initialized when the object is instantiated
    def __init__(self, user_name, user_email, user_password):
        self.user_name = user_name
        self.user_email = user_email
        self.user_password = user_password
        
    def create_user(self):
        # validate data and create user
        
    def login_user(self, email, password):
        # check provided credentials against stored values
        if email == self.user_name and password == self.user_password:
            # create session and login user
        else:
            # prompt user to make another login attempt
        
    def logout_user(self):
        # unset user's session and redirect to login page
