class Manager(list):

  def filter(self, **criteria):
    filtered_items = []

    for item in self:
      try:
        result = list((True for key, value in criteria.iteritems() if item[key] == value))

        if all(result) and result:
          filtered_items.append(item)
      except KeyError:
        continue

    return Manager(filtered_items)
