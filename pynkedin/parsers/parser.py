from abc import ABCMeta, abstractmethod

class Parser(object):
  __metaclass__ = ABCMeta

  @abstractmethod
  def __call__(self, content):
    pass
