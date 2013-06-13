class ResponseObject(object):

  def __init__(self, *args, **kwargs):
    super(ResponseObject, self).__init__(*args, **kwargs)
  
  def set_for(self, cls):
    cls.__dict__ = self.__dict__
