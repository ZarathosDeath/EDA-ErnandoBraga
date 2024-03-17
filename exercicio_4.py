from helpers.node import Node

class DoublyLinkedList:
  # Lista duplamente encadeada

  def __init__(self):
    self.head = None
    self.tail = None

  def insert_at_begin(self, data):
    new_node = Node(data)
    if self.head is None:
      self.head = self.tail = new_node
    else:
      new_node.next = self.head
      self.head.prev = new_node
      self.head = new_node

  def insert_at_end(self, data):
    new_node = Node(data)
    if self.head is None:
      self.head = self.tail = new_node
    else:
      new_node.prev = self.tail
      self.tail.next = new_node
      self.tail = new_node

  def delete_by_name(self, name):
    current = self.head
    if current.data.name == name:
      self.head = current.next
    else:
      while current:
        if current.data.name == name:
          break
        prev = current
        current  = current.next
      if current == None:
        return
      prev.next = current.next
      current = None

  def update_student(self, name, score):
    current = self.head

    if current.data['name'] == name:
      current.data['score'] = score
    else:
      while (current):
        if current.data['name'] == name:
          break
        if current is None:
          return "Aluno não existente na lista."
        current.data['score'] = score
        return

  def delete_from_beginning(self):
    if self.head is None:
        return
    data = self.head.data
    if self.head == self.tail:
        self.head = self.tail = None
    else:
        self.head = self.head.next
        self.head.prev = None
    return data

  def delete_from_end(self):
    if self.head is None:
        return
    data = self.tail.data
    if self.head == self.tail:
        self.head = self.tail = None
    else:
        self.tail = self.tail.prev
        self.tail.next = None
    return data

  def printList(self):
    current = self.head
    while current:
      print(current.data, end = " ")
      current = current.next


# lista = DoublyLinkedList()
# lista.insert_at_begin({ 'name': "Aluno 1", 'score': 5.0 })
# lista.insert_at_end({ 'name': "Aluno 2", 'score': 9.0 })
# lista.printList()
# lista.update_student("Aluno 1", 7.5)
# lista.printList()
