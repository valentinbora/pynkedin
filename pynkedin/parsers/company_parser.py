import json

from parser import Parser

class CompanyParser(Parser):

  def get_object(self, content):

    if not content["_total"]:
      raise LookupError("Company not found!")

    return self.to_object(content["values"][0])
