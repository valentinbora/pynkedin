from pynkedin.models.company import Company
from pynkedin.auth import AuthSession
from config import *
from pprint import pprint

token = 'users_access_token'

AuthSession(client_id=config['client_id'],
            client_secret=config['client_secret'], 
            access_token=config['access_token'])

company = Company(company_id=config['company_id'], cache=True)

# all udpates of a company get them only once
print company.posts

# cached
# get all comments from a post
for post in company.posts:
  print post.comments
