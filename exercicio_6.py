# Desenvolva um algoritmo em Python para enfileirar elementos em uma fila e outro para desenfileirar elementos. 

class Queue: 
  def __init__(self, limit):
    self.queue = []
    self.limit = limit

  def enqueue(self, data):
    if len(self.queue) == self.limit:
      print("Queue is full")
      return
    else:
      self.queue.append(data)

  def dequeue(amount = 0):
    if len(self.queue) == 0:
      print("Queue is empty.")
      return
    else:
      return self.queue.pop(amount)