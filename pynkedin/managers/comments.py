from pynkedin.manager import Manager

class CommentsManager(Manager):

  def add(self, value):
    if value in self.items:
      raise ValueError('This update is already related to this company')
    print 'do stuff with the update'
    self.append(value)

  def ingest(self, comments):
    self += comments
