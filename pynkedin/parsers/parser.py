from abc import ABCMeta, abstractmethod

from response_object import ResponseObject

class Parser(object):
  __metaclass__ = ABCMeta

  def __init__(self, cls):
    self.cls = cls

  @abstractmethod
  def __call__(self, content):
    pass

  def to_object(self, response):
    return ResponseObject(response)
