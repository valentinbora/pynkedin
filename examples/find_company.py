from pynkedin import Company
from pynkedin.auth import AuthSession

token = 'AQXqW96j6u9T91hxk7gjTPdpZ9vpNFcAc4e-1JbZVwvA_kOuNA3CMxJAYDMxzZhj2J2zRoeo9WUoiu6cMowOvOp4JsrV_BUPALWu_Zo9g3z1nDAXbae8sQ1cMKakykjf8zKF3m7IuqdIddTMs_Ma1-BpR3Ng7LglkFZ4qn2YVducSHsc72A'

AuthSession(client_id='hbm5ioyd4zvu', client_secret='1kDH3xYwW2D5Qwa3', access_token=token)

company = Company(company_id=7)
print company.industries
