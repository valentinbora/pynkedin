from pynkedin.manager import Manager
from pynkedin.models.post import CompanyPost

class PostsManager(Manager):

  def __init__(self, company):
    self.company_path = company
    super(PostsManager, self).__init__()

  def add(self, value):
    if value in self.items:
        raise ValueError('This update is already related to this company')

    print 'do stuff with the update'

    self.append(value)

  def ingest(self, response):
    for post in response:
      self.append(CompanyPost(post))
