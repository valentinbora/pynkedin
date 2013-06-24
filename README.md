pynkedin
========

Easiest to use Linkedin library

### Overview
Linkedin, by default, have a hard time building a really nice and easy to use
APi. Focusing on a lot of directions and implementing 2-3 methods for the same
things, transform a potential nice API in a mess.

I wanted to keep every aspect really basic and to transform the API to an ORM

### API ---> ORM
```python

#simple company retrieve by id
company = Company(id=21476)

#get all updates off a company
for update in company.updates:
  # retrieve stuff from an update
  comments = update.comments
  content = update.content
  author = update.author
  social_network_id = update.snid
```
