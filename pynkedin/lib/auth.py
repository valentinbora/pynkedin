from random import randint
import hashlib
import sys
import json

from rauth import OAuth2Service, OAuth2Session

from singleton import Singleton

AUTHORIZE_URL = 'https://www.linkedin.com/uas/oauth2/authorization'
ACCESS_TOKEN = 'https://www.linkedin.com/uas/oauth2/accessToken'
BASE_URL = 'https://api.linkedin.com/v1/'

class AuthSession(object):
  __metaclass__ = Singleton

  def __init__(self, client_id, client_secret, access_token):
    self.session = OAuth2Session(client_id, client_secret, access_token)

    self.call_url = "%s%s?oauth2_access_token=" + access_token

  def get(self, **kwargs):
    pass

  def post(self, **kwargs):
    pass

  def filter(self, path, **kwargs):
    relative_path = "%s::(%s)"
    arguments_path = ""

    #TODO: refactor this
    for arg in kwargs:
      if arguments_path:
        arguments_path = "%s,%s=%s" % (arguments_path, arg.replace('_', '-'), kwargs[arg])
      else:
        arguments_path = "%s=%s" % (arg.replace('_', '-'), kwargs[arg])

    relative_path = relative_path % (path, arguments_path)
    url = self.call_url % (BASE_URL, relative_path)

    headers = {
      'x-li-format': 'json'
    }

    response = self.session.get(url, headers=headers, bearer_auth=False)

class AuthService(object):
  __metaclass__ = Singleton

  def __init__(self, client_id, client_secret, redirect_uri):
    self.outh_service = OAuth2Service(
                                  client_id=client_id,
                                  client_secret=client_secret,
                                  name='linkedin',
                                  authorize_url=AUTHORIZE_URL,
                                  access_token_url=ACCESS_TOKEN,
                                  base_url=BASE_URL)

    self.redirect_uri = redirect_uri

  def get_access_token(self, auth_code):
    data= { 'code': auth_code,
            'grant_type': 'authorization_code',
            'redirect_uri': self.redirect_uri}

    return self.outh_service.get_access_token(data=data, decoder=json.loads)

  def create_session(self, access_token=None):
    return self.outh_service.get_session(access_token)

  def get_authorize_url(self, scope=None):
    self.state = hashlib.sha224(str(randint(0, sys.maxint))).hexdigest()

    params = {'scope': scope,
              'response_type': 'code',
              'state': self.state,
              'redirect_uri': self.redirect_uri}

    return self.outh_service.get_authorize_url(**params)
