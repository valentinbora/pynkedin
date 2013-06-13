class ThrottleLimitException(Exception):
  pass

class OAuthSignatureException(Exception):
  pass

class BadRequestException(Exception):
  pass

class NotFoundException(Exception):
  pass

class BadHTTPMethodException(Exception):
  pass

class LinkedinServerException(Exception):
  pass

EXCEPTION_CODES = {
  500: LinkedinServerException('There was an application error on the LinkedIn server'),
  405: BadHTTPMethodException('You used the wrong HTTP method'),
  404: NotFoundException('The resource was not found'),
  403: ThrottleLimitException('You have reached a throttle limit!'),
  401: OAuthSignatureException('OAuth signature was bad'),
  400: BadRequestException('Your request was not formatted correctly'),
}

def raiser(status_code):
  raise EXCEPTION_CODES[status_code]
