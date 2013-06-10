from lib.auth import AuthService, AuthSession

class Company(object):
  """
    company = Company.find(id=1)

    Retrieve
    --------
      company.updates => [{ update_1 }, { update_2 }]
      company.name    => 'Company name'
      company.fields  => { 'id': 1, ... , 'field_name': value }

    Create
    ------
      company.updates.add(update)
      company.name = 'My awesome company'

  """
  #parser = CompanyParser

  @classmethod
  def find(cls, **kwargs):
    print kwargs['id']
