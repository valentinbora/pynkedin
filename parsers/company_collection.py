from abc import ABCMeta, abstractmethod
import json

from ..exceptions import raiser, EXCEPTION_CODES
from ..helpers import ResponseObject

class CompanyCollectionParser(object):
  def __call__(self, response):
    content = json.loads(response.content)

    if response.status_code in EXCEPTION_CODES:
      print response.text
      raiser(response.status_code)

    if 'values' in content:
      companies = []

      for company in content['values']:
        companies.append(company)

      return companies
    
    return None
