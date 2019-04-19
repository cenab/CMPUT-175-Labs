class BinaryTree:
  def __init__(self, rootElement):
    self.key = rootElement
    self.left = None
    self.right = None

  def getLeft(self):
    return self.left

  def getRight(self):
    return self.right

  def getRootVal(self):
    return self.key

  def setRootVal(self,val):
    self.key=val
  
  def insertLeft(self,newNode):
    if self.left == None:
      self.left = BinaryTree(newNode)
    else:
      t = BinaryTree(newNode)
      t.left = self.left
      self.left = t
  
  def insertRight(self,newNode):
    if self.right == None:
      self.right = BinaryTree(newNode)
    else:
      t = BinaryTree(newNode)
      t.right = self.right
      self.right = t


def preorder(tree):
  if tree != None:
    print(tree.getRootVal(), end=' ')
    preorder(tree.getLeft())
    preorder(tree.getRight())


def inorder(tree):
  if tree != None:
    inorder(tree.getLeft())
    print(tree.getRootVal(), end=' ')
    inorder(tree.getRight())


def postorder(tree):
  if tree != None:
    postorder(tree.getLeft())
    postorder(tree.getRight())
    print(tree.getRootVal(), end=' ')


def findMinValue(tree):
  if tree == None:
    return None
  via1 = tree.getRootVal()
  via2 = findMinValue(tree.getLeft())
  via3 = findMinValue(tree.getRight())
  list = []
  if via1 is not None:
    list.append(via1)
  if via2 is not None:
    list.append(via2)
  if via3 is not None:
    list.append(via3)
  return min(list)

def findMaxValue(tree):
  if tree == None:
    return None
  via1 = tree.getRootVal()
  via2 = findMaxValue(tree.getLeft())
  via3 = findMaxValue(tree.getRight())
  list = []
  if via1 is not None:
    list.append(via1)
  if via2 is not None:
    list.append(via2)
  if via3 is not None:
    list.append(via3)
  return max(list)

def contains(tree, item):
  if tree == None:
    return False
  via1 = tree.getRootVal()
  via2 = contains(tree.getLeft(), item)
  via3 = contains(tree.getRight(), item) 
  if via1 == False and via2 == False and via3 == False:
    return False
  else:
    return True
  
def add(tree, item):
  if tree == None:
    return None
  tree2 = binaryTree(item)
  tree2.insertLeft(tree)
  tree = tree2
  
def remove(tree, item):
  if contains(tree, item) == True:
    via1 = tree.getRootVal()
    via2 = contains(tree.getLeft(), item)
    via3 = contains(tree.getRight(), item) 
    if via1 == False and via2 == False and via3 == False:
  if       
  tree.getLeft().setRootVal(tree.getRight())
  tree.getRight().setRootVal(None)
    
    

  
  



def main():
  tree = BinaryTree(1)
  tree.insertLeft(2)
  tree.insertRight(7)
  tree.getLeft().insertLeft(3)
  tree.getLeft().insertRight(6)
  tree.getLeft().getLeft().insertLeft(4)
  tree.getLeft().getLeft().insertRight(5)
  tree.getRight().insertLeft(8)
  tree.getRight().insertRight(9)

  preorder(tree)
  print()
  inorder(tree)
  print()
  postorder(tree)
  print()
  print(contains(tree, 2))
  print('Max value in tree:', findMaxValue(tree))
  print('Min value in tree:', findMinValue(tree))

if __name__ == "__main__":
  main()