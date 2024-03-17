# Construa uma função em Python para empilhar elementos em uma pilha e outra para desempilhar elementos. 

class Stack:
  def __init__(self):
    self.stack = []

  def push(self, data):
    self.stack.append(data)

  def remove(self):
    self.stack.pop()