from abc import ABCMeta, abstractmethod
import json

from exceptions import raiser, EXCEPTION_CODES
from response_object import ResponseObject

class Parser(object):
  __metaclass__ = ABCMeta

  def __call__(self, response):
    content = json.loads(response.content)
    status_code = content['status']

    if status_code in EXCEPTION_CODES:
      raiser(status_code)

    return self.get_object(content)

  @abstractmethod
  def get_object(self, content):
    pass

  def to_object(self, response):
    return ResponseObject(response)
