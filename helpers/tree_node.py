class TreeNode:
  def __init__(self, data):
    self.data = data
    self.left = self.right = None

  def insert_node(self, data):
    if self.data:
      if data < self.data:
        if self.left is None:
          self.left = TreeNode(data)
        else:
          self.left.insert_node(data)
      if data > self.data:
        if self.right is None:
          self.right = TreeNode(data)
        else: 
          self.right.insert_node(data)
    else:
      self.data = data

  def print_tree(self):
    if self.left:
      self.left.print_tree()
    print( self.data),
    if self.right:
      self.right.print_tree()

class Height:
  def __init__(self):
    self.height = 0