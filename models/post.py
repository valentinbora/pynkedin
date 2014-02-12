from ..managers.comments import CommentsManager

comments = CommentsManager()

class CompanyPost(dict):
  raw_attrs = None

  def __init__(self, post):
    attrs = self.parse_post(post)

    super(CompanyPost, self).__init__(attrs)
    self.__dict__ = self

  def parse_post(self, post):
    attrs = {}

    for getter in dir(self):
      if getter.startswith("_get_"):
        item = getattr(self, getter)(post)

        attrs[getter[5:]] = item

    return attrs

  def _get_author(self, post):
    try:
      author = post['updateContent']['companyStatusUpdate']['share']['author']
    except KeyError:
      author = post['updateContent']['company']['name']

    return author

  def _get_content(self, post):
    content = post['updateContent']['companyStatusUpdate']['share']
    return content

  def _get_snid(self, post):
    snid = post['updateContent']['companyStatusUpdate']['share']['id']
    return snid

  def _get_timestamp(self, post):
    timestamp = post['timestamp']
    return timestamp

  def _get_comments(self, post):
    post_comments = [] 

    if 'updateComments' in post:
      post_comments = post['updateComments']

    comments.ingest(post_comments)

    return comments

  def _get_likes(self, post):
    likes = []

    if 'numLikes' in post and post['numLikes']:
      for like in post['likes']:
        likes.append(like['person'])

    return likes
