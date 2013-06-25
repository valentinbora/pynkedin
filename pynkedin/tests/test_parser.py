import json

from nose.tools import eq_
from mock import MagicMock

from pynkedin.parser import Parser

def test_parser_no_content():

  mocked_response = MagicMock()
  mocked_response.content = json.dumps({'status_code': 123})
  mocked_response.status_code = 123

  parser = Parser()
  eq_(parser(mocked_response), None)
