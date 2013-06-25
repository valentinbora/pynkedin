from pynkedin import Company
from pynkedin.auth import AuthSession

token = 'users_access_token'

AuthSession(client_id='client_id_of_my_awesome_app',
            client_secret='client_secret_of_my_awesome_app', 
            access_token=token)

company = Company(company_id='company_id', cache=True)

# you can do nested filtering
# filter the posts first and then the comments
comments = company.posts.filter(snid='s5750272081627451398')[0].comments.filter(id=143903254)

# iterate through filtered comments
for comment in comments:
  print comment
