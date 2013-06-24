class CompanyUpdate(dict):

  def __init__(self, update, company):
    attrs = self.parse_update(update)

    super(CompanyUpdate, self).__init__(attrs)
    self.__dict__ = self

    self.company = company

  def parse_update(self, update):
    attrs = {}

    for getter in dir(self):
      if getter.startswith("_get_"):
        item = getattr(self, getter)(update)

        attrs[getter[5:]] = item

    return attrs

  def _get_author(self, update):
    try:
      author = update['updateContent']['companyStatusUpdate']['share']['author']
    except KeyError:
      author = update['updateContent']['company']['name']

    return author

  def _get_content(self, update):
    content = update['updateContent']['companyStatusUpdate']['share']['comment']
    return content

  def _get_snid(self, update):
    snid = update['updateContent']['companyStatusUpdate']['share']['id']
    return snid

  def _get_timestamp(self, update):
    timestamp = update['timestamp']
    return timestamp

  def _get_comments(self, update):
    comments = [] 

    if 'updateComments' in update:
      comments = update['updateComments']

    return comments

  def _get_likes(self, update):
    likes = []

    if 'numLikes' in update and update['numLikes']:
      for like in update['likes']:
        likes.append(like['person'])

    return likes

  def add(self, update):
    pass
