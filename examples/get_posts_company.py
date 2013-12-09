from pynkedin import Company
from pynkedin.auth import AuthSession

token = 'users_access_token'

AuthSession(client_id='client_id_of_my_awesome_app',
            client_secret='client_secret_of_my_awesome_app', 
            access_token=token)

company = Company(company_id='company_id', cache=True)

# all udpates of a company get them only once
print company.posts

# cached
# get all comments from a post
for post in company.posts:
  print post.comments
