# criar uma função em python para inserir um elemento em uma lista encadeada simples

def insert_at_begin(self, data):
  new_node = Node(data)
  if self.head is None:
    self.head = new_node
  else:
    new_node.next = self.head
    self.head = new_node
  return