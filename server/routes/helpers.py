import os
from dotenv import load_dotenv

# This helper function will check if a user is an admin or not
def get_admins(email):
    load_dotenv(verbose=True) 

    # get all possible admin emails
    admin_emails = os.getenv("ADMIN_EMAILS")

    for emailOf in admin_emails.split(' '):
        if email == emailOf:
            return True
    return False
