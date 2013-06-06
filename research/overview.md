people:
  description: "Member profiles, reading or writing network updates, messaging and connections"
  resources: 
    - http://api.linkedin.com/v1/people
    - http://api.linkedin.com/v1/people-search

groups:
  description: "Reading and writing group posts and comments, group memberships for the authenticated user, joining groups."
  resources:
    - http://api.linkedin.com/v1/groups
    - http://api.linkedin.com/v1/posts

company:
  description: "Company profiles, suggested companies for a user to follow, following companies"
  resources:
    - http://api.linkedin.com/v1/companies
    - http://api.linkedin.com/v1/company-search

jobs:
  description: "Jobs posted on LinkedIn"
  resources:
    - http://api.linkedin.com/v1/jobs
    - http://api.linkedin.com/v1/jobs-search

response-type:
  - xml: default
  - json:
      - "x-li-format" HTTP header to "json"
      - ?format=json
