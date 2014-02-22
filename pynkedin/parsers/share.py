from abc import ABCMeta, abstractmethod
import json

from ..exceptions import raiser, EXCEPTION_CODES

class ShareParser(object):
  def __call__(self, response):
    content = json.loads(response.content)

    if response.status_code in EXCEPTION_CODES:
      print response.text
      raiser(response.status_code)

    return content