from pynkedin.models.company import Company
from pynkedin.auth import AuthSession
from config import *
from pprint import pprint

AuthSession(client_id=config['client_id'],
            client_secret=config['client_secret'], 
            access_token=config['access_token'])

company = Company(company_id=config['company_id'])

action = company.share_link(url="http://airbnb.github.io/polyglot.js/", comment="Lorem ipsum dolor sit amet, consectetur adipisicing elit. Molestiae, quaerat, voluptatum, dolores corporis sit fugiat nobis iste veritatis sapiente nisi repellendus voluptatibus voluptatem quasi optio accusantium aspernatur laborum laboriosam numquam!", image_url="https://fbcdn-sphotos-d-a.akamaihd.net/hphotos-ak-prn2/t1/1656338_360744710735206_453087077_n.jpg")

print action
post = company.get_post_by_update_key(action['updateKey'])

print post
