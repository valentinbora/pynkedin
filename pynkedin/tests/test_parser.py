import json

from nose.tools import eq_, raises
from mock import MagicMock

from pynkedin.exceptions import NotFoundException
from pynkedin.parser import Parser

def test_parser_no_content():
  '''
    Test the parser without any response
  '''

  mocked_response = MagicMock()
  mocked_response.content = json.dumps({'status_code': 123})
  mocked_response.status_code = 123

  parser = Parser()
  eq_(parser(mocked_response), None)

@raises(NotFoundException)
def test_parser_error_raising():
  '''
    Test parser when the response contains 404
  '''

  mocked_response = MagicMock()
  mocked_response.content = json.dumps({'content': 'nothing here'})
  mocked_response.status_code = 404

  parser = Parser()
  parser(mocked_response)
