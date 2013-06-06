operations:
  - description: "retrieve companies information based on a company id"
    request: "http://api.linkedin.com/v1/companies/162479"
    response: {
      'company': {
        'id': 123,
        'name': 'My awesome company'
      }
    }
  - 
fields:
  - id
  - name
  - universal-name
  - email-domains
  - company-type
  - ticker
  - website-url
  - industries
  - status
  - logo-url
  - square-logo-url
  - blog-rss-url
  - twitter-id
  - employee-count-range
  - specialties
  - locations
      - description
      - is-headquarters
      - is-active
      - address
          - street1
          - street2
          - city
          - state
          - postal-code
          - country-code
          - region-code
      - contact-info
          - phone1
          - phone2
          - fax
  - description
  - stock-exchange
  - founded-year
  - end-year
  - num-followers
