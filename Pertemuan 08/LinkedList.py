#Node class
class Node:
  def __init__ (self, data):
    self.data = data
    self.next = None

#linked list class
class LinkedList:
  def __init__ (self):
    self.head = None
  
  # Fungsi untuk menambahkan node di awal linked list
  def push(self, new_data):
    new_node = Node(new_data)
    new_node.next = self.head
    self.head = new_node
  
  # Fungsi untuk menambahkan node setelah node tertentu
  def insert_after(self, prev_node, new_data):
    if prev_node is None:
      print("Node tidak ditemukan")
      return
    
    new_node = Node(new_data)
    new_node.next = prev_node.next
    prev_node.next = new_node

  # Fungsi untuk menambahkan node di akhir linked list
  def append(self, new_data):
    new_node = Node(new_data)

    if self.head is None:
      self.head = new_node
      return

    last = self.head
    
    while last.next:
        last = last.next

      last.next = new_node

  # Fungsi untuk mencetak linked list
  def print_list(self):
    temp = self.head
    while temp:
      print(temp.data)
      temp = temp.next
  
# Contoh penggunaan
llist = LinkedList()               # Membuat linked list kosong
llist.push(3)                      # Menambahkan node di awal linked list
llist.insert_after(llist.head, 5)  # Menambahkan node setelah node tertentu
llist.append(7)                    # Menambahkan node di akhir linked list
llist.print_list()                 # Mencetak linked list