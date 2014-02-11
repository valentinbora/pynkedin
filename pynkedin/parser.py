from abc import ABCMeta, abstractmethod
import json

from exceptions import raiser, EXCEPTION_CODES
from helpers import ResponseObject

class Parser(object):
  def __call__(self, response):
    content = json.loads(response.content)

    if response.status_code in EXCEPTION_CODES:
      raiser(response.status_code)

    if 'values' in content:
      return self.to_object(content['values'])

    return None

  def to_object(self, values):
    response_objects = []

    for response in values:
      response_objects.append(ResponseObject(response))

    if len(response_objects) == 1:
      return response_objects[0]

    return response_objects

class ShareParser(object):
  def __call__(self, response):
    content = json.loads(response.content)

    if response.status_code in EXCEPTION_CODES:
      raiser(response.status_code)

    return content
