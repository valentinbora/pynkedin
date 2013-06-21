class CompanyUpdate(dict):

  def __init__(self, update):
    attrs = self.parse_update(update)

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
    author = "gigel"
    return author

  def _get_content(self, update):
    content = "content"
    return content

  def _get_snid(self, update):
    snid = "snid"
    return snid

  def _get_timestamp(self, update):
    timestamp = "123"
    return timestamp

  def _get_comments(self, update):
    comments = ["comment1"]
    return comments

  def _get_likes(self, update):
    likes = ["like1"]
    return likes
