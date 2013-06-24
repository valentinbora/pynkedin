from pynkedin.auth import AuthService, AuthSession
from pynkedin.parser import Parser

from update_model import CompanyUpdate
from updates import UpdatesManager

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

  def __init__(self, company_id, cache=True):
    self.path = "companies/%s" % company_id

    self.cache = cache
    self.fields['id'] = company_id

  def __getattr__(self, item):
    print self.fields
    if item in self.fields and self.cache:
      return self.fields[item]

    if callable(item):
      return item()

    if hasattr(self, "_get_%s" % item):
      return getattr(self, "_get_%s" % item)()

    response = AuthSession().get(path=self.path, parser=self.parser, fields=[item])
    if self.cache:
      self.fields.update(response)

    return response

  def _get_updates(self):
    updates = UpdatesManager(self)

    kwargs = {
      'start': 0,
      'count': 10,
      'event-type':'status-update'
    }
    path = "%s/updates" % self.path

    response = AuthSession().get(path=path, parser=self.parser, **kwargs)

    while response:
      updates.ingest_updates(response)

      kwargs['start'] += kwargs['count']
      response = AuthSession().get(path=path, parser=self.parser, **kwargs)

    if self.cache:
      self.fields['updates'] = updates

    return updates
