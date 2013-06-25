from pynkedin import Company
from pynkedin.auth import AuthSession

token = 'users_access_token'

AuthSession(client_id='client_id_of_my_awesome_app',
            client_secret='client_secret_of_my_awesome_app', 
            access_token=token)

company = Company(company_id='company_id', cache=True)

# get the updates and the filter by some criteria
# snid == social network id (the id from linkedin)
filtered_updates = company.updates.filter(snid='an_update_snid') 

# you can now iterate on filtered_updates
for update in filtered_updates:
  print update
