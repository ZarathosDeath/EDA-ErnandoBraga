# Crie um programa em Python que utilize uma tabela hash para armazenar e recuperar 
# informações de alunos com base em seus números de matrícula. 

class StudentsList:
  def __init__(self, capacity = 1):
    self.list = {}
    self.capacity = capacity
  
  def insert_student(self, registration, data):
    if registration not in self.list:
      self.list[registration] = data
    else:
      print("aluno já cadastrado")
  
  def find_student(self, registration):
    if registration in self.list:
      return self.list[registration]
    else:
      print("aluno não existente")
      return None

lista = StudentsList()
lista.insert_student(1001, { 'name': 'Aluno 1', 'score': 1})
lista.insert_student(1003, { 'name': 'Aluno 3', 'score': 3})
lista.insert_student(1003, { 'name': 'Aluno 3', 'score': 3})
print(lista.find_student(1003))
print(lista.find_student(1005))
