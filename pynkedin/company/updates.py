from update_model import CompanyUpdate

class Manager(object):
  items = []

  def all(self):
    return self.items

  def filter(self, **criteria):
    filtered_items = []

    for item in self.items:
      try:
        if all(True for key, value in criterias.iteritems() if item[key] == item[value]):
          filtered_items.append(item)
      except KeyError:
        continue

    return filtered_items

class UpdatesManager(Manager):

  def __init__(self, company):
    self.company_path = company

  def add(self, value):
    if value in self:
        raise ValueError('This update is already related to this company')
    print 'do stuff with the update'
    self.items.append(value)

  def ingest_updates(self, response):
    for update in response:
      self.items.append(update)
