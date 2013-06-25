class Manager(list):

  def filter(self, **criteria):
    filtered_items = []

    for item in self:
      try:
        if all(True for key, value in criteria.iteritems() if item[key] == value):
          filtered_items.append(item)
      except KeyError:
        print error
        continue

    return filtered_items
