from pynkedin.manager import Manager
from update_model import CompanyUpdate

class UpdatesManager(Manager):

  def __init__(self, company):
    self.company_path = company
    super(UpdatesManager, self).__init__()

  def add(self, value):
    if value in self.items:
        raise ValueError('This update is already related to this company')
    print 'do stuff with the update'
    self.append(value)

  def ingest(self, response):
    for update in response:
      self.append(CompanyUpdate(update))
