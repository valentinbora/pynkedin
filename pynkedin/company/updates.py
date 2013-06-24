from update_model import CompanyUpdate

class CompanyUpdates(list):
  def __init__(self, company):
    self.company = company

  def add(self, value):
    if value in self:
        raise ValueError('This update is already related to this company')
    print 'do stuff with the update'
    super(CompanyUpdates, self).append(value)

  def ingest(self, response):
    for update in response:
      self.append(update)
