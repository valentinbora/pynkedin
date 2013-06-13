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
    company = Company(company_id=1)

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

  fields = {}
  parser = CompanyParser()

  def __init__(self, company_id):
    self.path = "companies/%s" % company_id

    self.fields['id'] = company_id

  def __getattr__(self, item):
    if item not in self.fields:
      response = AuthSession().get(path=self.path, parser=self.parser, fields=[item])
      self.fields.update(response)

    return self.fields[item]
