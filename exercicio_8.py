#  Implemente um algoritmo em Python para ordenar uma lista de números utilizando o método de ordenação bolha (bubble sort).

def bubble_sort(arr):
  arr_size = len(arr)
  for index in range (arr_size - 1):
    aux = False
    for JIndex in range (0, arr_size-index-1):
      if arr[JIndex] > arr[JIndex+1]:
        aux = True
        arr[JIndex], arr[JIndex + 1] = arr[JIndex + 1], arr[JIndex]

    if not aux:
      return

lista = [1, 5, 23, 75, 2, 8, 45]

bubble_sort(lista)
print(lista)