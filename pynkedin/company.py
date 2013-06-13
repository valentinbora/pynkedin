from lib.auth import AuthService, AuthSession
from parsers import CompanyParser

KEYS    = ['id', 'universal_name']
FILTERS = ['email_domains']

FIELDS  = ['id', 'name', 'universal-name', 'email-domains', 'company-type',
           'ticker', 'website-url', 'industries', 'status', 'logo-url',
           'square-logo-url', 'blog-rss-url', 'twitter-id',
           'employee-count-range', 'specialties', 'locations', 'description',
           'stock-exchange', 'founded-year', 'end-year', 'num-followers' ]

class Company(object):
  """
    company = Company.find(id=1)

    Retrieve
    --------
      company.updates => [{ update_1 }, { update_2 }]
      company.name    => 'Company name'
      company.fields  => { 'id': 1, ... , 'field_name': value }

    Create
    ------
      company.updates.add(update)
      company.name = 'My awesome company'

  """

  @classmethod
  def find(cls, **kwargs):
    parser = CompanyParser(cls)

    if len(kwargs) > 1:
      response_object = AuthSession().filter(path="companies", fields=FIELDS, parser=parser, **kwargs)
      return cls(response_object)

  def __init__(self, response_object):
    response_object.set_for(self)
