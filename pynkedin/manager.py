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

  def exclude(self, **criteria):
    """
      Filter the items from self and return the diference between filtered items
      and existing items 
    """

    filtered_items = self.filter(**criteria)

    return Manager([item for item in self if item not in filtered_items])
