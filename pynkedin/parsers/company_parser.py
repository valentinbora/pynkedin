import json
from pprint import pprint as pp

from parser import Parser

class CompanyParser(Parser):

  def __call__(self, content):
    content = json.loads(content)

    if not content["_total"]:
      raise LookupError("Company not found!")

    return self.to_object(content["values"][0])
