class CompanyUpdate(dict):

  def __init__(self, update):
    attrs = self.parse_update(update)
    from pprint import pprint as pp
    pp(update)
    super(CompanyUpdate, self).__init__(attrs)
    self.__dict__ = self

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
    comments = ["comment1"]
    return comments

  def _get_likes(self, update):
    likes = []

    if 'numLikes' in update and update['numLikes']:
      for like in update['likes']:
        likes.append(like['person'])

    return likes
