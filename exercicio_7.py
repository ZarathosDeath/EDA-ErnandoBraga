# Crie uma função em Python para buscar um elemento específico em uma lista utilizando o método de pesquisa sequencial. 

from exercicio_4 import DoublyLinkedList

lista = DoublyLinkedList()

def search(self, value):
  current = self.head

  while current != None:
    if current.data == value:
      return current.data
    else:
      return False

setattr(DoublyLinkedList, 'search', search)

lista.insert_at_begin({ 'name': 'Aluno 1', 'score': 5 })
print(lista.search({ 'name': 'Aluno 1', 'score': 5 }))
print(lista.search({ 'name': 'Aluno 2', 'score': 5 }))
