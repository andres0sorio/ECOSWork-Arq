import json

class Tree(object):
    """
    """
    def __init__(self, name, childTrees=None):
        self.name = name
        if childTrees is None:
            childTrees = []
        self.childTrees = childTrees

class MyEncoder(json.JSONEncoder):
    """
    """
    def default(self, obj):
        if not isinstance(obj, Tree):
            return super(MyEncoder, self).default(obj)

        return obj.__dict__

