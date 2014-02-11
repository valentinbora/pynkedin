from pynkedin.models.company import Company
from pynkedin.auth import AuthSession
from config import *
from pprint import pprint

AuthSession(client_id=config['client_id'],
            client_secret=config['client_secret'], 
            access_token=config['access_token'])

company = Company(company_id=config['company_id'])

action = company.share()
print action
post = company.get_post_by_update_key(action['updateKey'])

print post
