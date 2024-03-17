#Desenvolva um programa em Python que utilize o método de pesquisa binária para encontrar um elemento em uma lista ordenada. 


def binary_search(arr, value):
  low = 0
  high = len(arr) - 1
  mid = 0

  while low <= high:

      mid = (high + low) // 2

      if arr[mid] < value:
          low = mid + 1

      elif arr[mid] > value:
          high = mid - 1

      else:
          return arr[mid]

  return "Valor não presente na lista"

lista = [1, 3, 6, 7, 13, 23, 56, 65, 70]
value = 56

result = binary_search(lista, value)
print(result)