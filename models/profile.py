from pynkedin.auth import AuthService, AuthSession
from pynkedin.parsers.company_collection import CompanyCollectionParser

from pynkedin.managers.companies import CompaniesManager

import json
import os
from urlparse import urlparse

KEYS    = ['id', 'universal_name']
FILTERS = ['email_domains']

FIELDS  = ['id', 'name', 'universal-name', 'email-domains', 'company-type',
           'ticker', 'website-url', 'industries', 'status', 'logo-url',
           'square-logo-url', 'blog-rss-url', 'twitter-id',
           'employee-count-range', 'specialties', 'locations', 'description',
           'stock-exchange', 'founded-year', 'end-year', 'num-followers' ]

class Profile(object):
  """
    profile = Profile(profile_id=~)

    Retrieve
    --------
      profile.admin_companies => [{ company_1 }, { company_2 }]

  """

  fields = {}
  parser = CompanyCollectionParser()

  def __init__(self, profile_id='~', cache=True):
    self.path = "people/%s" % profile_id

    self.cache = cache
    self.fields['id'] = profile_id

  def __getattr__(self, item):
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

  def _get_admin_companies(self):
    kwargs = {
      'start': 0,
      'count': 10,
      'is-company-admin': 'true'
    }
    path = "companies"

    companies = CompaniesManager(self)

    response = AuthSession().get(path=path, parser=self.parser, **kwargs)

    while response:
      companies.ingest(response)
      
      # Weird LinkedIn behavior, ignoring the start param for less than 10 companies total
      if len(companies) < 10:
        break

      kwargs['start'] += kwargs['count']
      response = AuthSession().get(path=path, parser=self.parser, **kwargs)

    return companies
