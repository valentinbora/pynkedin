from pynkedin.auth import AuthService, AuthSession
from pynkedin.parser import Parser

from update_model import CompanyUpdate
from updates import CompanyUpdates

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

  """

  fields = {}
  parser = Parser()

  def __init__(self, company_id):
    self.path = "companies/%s" % company_id

    self.fields['id'] = company_id

  def __getattr__(self, item):
    if item in self.fields:
      return self.fields[item]

    if callable(item):
      return item()

    if hasattr(self, "_get_%s" % item):
      return getattr(self, "_get_%s" % item)()

    response = AuthSession().get(path=self.path, parser=self.parser, fields=[item])
    self.fields.update(response)

    return self.fields[item]

  def _get_updates(self):
    updates = CompanyUpdates(self)

    kwargs = {
      'start': 0,
      'count': 10,
      'event-type':'status-update'
    }
    path = "%s/updates" % self.path

    response = AuthSession().get(path=path, parser=self.parser, **kwargs)

    while response:
      updates.ingest(response)

      kwargs['start'] += kwargs['count']
      response = AuthSession().get(path=path, parser=self.parser, **kwargs)

    self.fields['updates'] = updates
    return updates
