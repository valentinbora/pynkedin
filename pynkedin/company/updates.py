class CompanyUpdates(list):
  def add(self, value):
    print 'Do stuff with update'
    super(CompanyUpdates, self).append(value)
