class Node:
      def __init__(self, value, next=None):
            self.value = value
            self.next = next

class BaseLinkedList:
  def __init__(self, collection=None):
    self.head = None
    self._length = 0
    if collection:
      for item in reversed(collection):
        self.insert(item)
  
  
class LinkedList(BaseLinkedList):
  
  def traverse(self, action):
    current = self.head
    while current:
      action(current.value)
      current = current.next

  def __iter__(self):
    def generator():
      current = self.head
      while current:
        yield current.value
        current = current.next
    return generator()
  
  def __str__(self):
    out = ""
    for value in self:
      out += f"[{value}] -> "
    return out + "None"

  def __len__(self):
    return self._length
  
  def insert(self, value):
    self.head = Node(value, self.head)
    self._length += 1
  
  def __getitem__(self, index):

    if index < 0:
      raise IndexError

    for i, item in enumerate(self):
      if i == index:
        return item
    raise IndexError
    


class Math:
  def __init__(self):
    self.total = 0
    self.product = 1
    self.squares = []

  def adder(self, value):
    self.total += value

  def multiplier(self, value):
    self.product *= value
  
  def squarer(self, value):
    self.squares.append(value ** 2)

if __name__=='__main__':
  list = LinkedList()
  list.insert(2)
  list.insert(6)
  list.insert(1)

  math_obj = Math()
  list.traverse(math_obj.adder)
  list.traverse(math_obj.multiplier)
  list.traverse(math_obj.squarer)

  def get_number():
    """ 
      Returns a number from the list
    """

    numbers = [2,3,4,5]
    for i in numbers:
      yield i

  gen = get_number()

  for item in list:
    print(item)
  print(list)
  print(f"item at index 1: {list[1]}")
  print(f"length of list: {len(list)}")

  list2 =  LinkedList([2,4,6,8])
  print(list2)


