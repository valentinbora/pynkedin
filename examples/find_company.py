from pynkedin import Company
from pynkedin.lib.auth import AuthSession

token = 'AQWL69--MU24jYiZZ1RpHDYF4CTrYoLNM30bstwKtD8GvYPqyfDDiA-QBbMO3Nx5-NnFxh-EKIiIbAxqOm9IYnUerIPlhzEJHmXn6RuzOqxqTBoAWDBEUq7YEFnw-e0X5lIq4mmuxoxm_JAIXrjOZ0ccOqp10vyqQ1kaOv4e0tKYnY0GLxQ'

AuthSession(client_id='hbm5ioyd4zvu', client_secret='1kDH3xYwW2D5Qwa3', access_token=token)

company = Company.find(id=7, universal_name='apple')
