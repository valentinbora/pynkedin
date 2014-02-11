from pynkedin.auth import AuthService, AuthSession
from pynkedin.parser import Parser, ShareParser

from pynkedin.managers.posts import PostsManager

import json

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
      company.posts => [{ post_1 }, { post_2 }]
      company.name    => 'Company name'
      company.fields  => { 'id': 1, ... , 'field_name': value }

    Create
    ------
      company.posts.add(post)

  """

  fields = {}
  parser = Parser()
  shareParser = ShareParser()

  def __init__(self, company_id, cache=True):
    self.path = "companies/%s" % company_id

    self.cache = cache
    self.fields['id'] = company_id

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

  def _get_posts(self):
    posts = PostsManager(self)

    kwargs = {
      'start': 0,
      'count': 10,
      'event-type':'status-update'
    }
    path = "%s/updates" % self.path

    response = AuthSession().get(path=path, parser=self.parser, **kwargs)

    while response:
      posts.ingest(response)

      kwargs['start'] += kwargs['count']
      response = AuthSession().get(path=path, parser=self.parser, **kwargs)

    if self.cache:
      self.fields['posts'] = posts

    return posts

  def get_post_by_update_key(self, updateKey):
    kwargs = {
      'start': 0,
      'count': 1
    }
    path = "%s/updates/key=%s" % (self.path, updateKey)

    response = AuthSession().get(path=path, parser=lambda x: json.loads(x.content), **kwargs)

    return response

  def share(self):
    fields = {
      'visibility': {
        'code': 'anyone'
      },
      'comment': "Lorem ipsum dolor sit amet, consectetur saluto. Bla salutiu."
    }
    path = "%s/shares" % self.path

    response = AuthSession().post(path=path, parser=self.shareParser, fields=fields)

    return response
