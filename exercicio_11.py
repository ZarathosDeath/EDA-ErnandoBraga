# Construa uma função em Python para percorrer uma árvore binária realizando o caminhamento em pré-ordem. 


from helpers.tree_node import TreeNode

def print_tree_pre_ordered(root):
  if root is None:
    return
  
  print(root.data, end=' ')

  print_tree_pre_ordered(root.left)
  print_tree_pre_ordered(root.right)


root = TreeNode(5)
root.insert_node(2)
root.left.insert_node(3)
root.insert_node(8)
root.right.insert_node(10)
root.right.insert_node(11)

print("arvore binaria pre ordem: ", print(print_tree_pre_ordered(root)))