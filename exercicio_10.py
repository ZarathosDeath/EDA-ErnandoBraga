# Elabore um algoritmo em Python para balancear uma árvore binária de busca. 
from helpers.tree_node import TreeNode, Height

def balance_tree(root):
  left_height = Height()
  right_height = Height()

  if root is None:
    return True
  
  return (
      (abs(left_height.height - right_height.height) <= 1)
      and balance_tree(root.left)
      and balance_tree(root.right)
   )

root = TreeNode(1)
root.insert_node(2)
root.insert_node(3)
root.right.insert_node(10)
root.right.insert_node(11)

if balance_tree(root):
  print("balanceada", root.print_tree())
else:
  print("não balanceada")

