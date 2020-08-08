
class Utility:

    @staticmethod
    def check_cred_validity(password, email=None, mobile=None):
        if password is None:
            return False
        if email is None and mobile is None:
            return False
        return True

