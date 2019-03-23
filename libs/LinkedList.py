#!/usr/bin/python
from node import Node

# Our LinkedList class
class LinkedList:
  def __init__(self, value=None):
    self.head_node = Node(value)
  
  def get_head_node(self):
    return self.head_node
  
  def insert_beginning(self, new_value):
    new_node = Node(new_value)
    new_node.set_next_node(self.head_node)
    self.head_node = new_node
    
  def stringify_list(self):
    string_list = ""
    current_node = self.get_head_node()
    while current_node:
      if current_node.get_value() != None:
        string_list += str(current_node.get_value()) + "\n"
      current_node = current_node.get_next_node()
    return string_list
  
  # Define your remove_node method below:
    # Define your remove_node method below:
  def remove_node(self, value_to_remove):
    current_node = self.get_head_node()
    if current_node.get_value() == value_to_remove:
      self.head_node = current_node.get_next_node()
      current_node = None
    else:
      while current_node:
        current_next_node = current_node.get_next_node()
        if current_next_node.get_value() == value_to_remove:
            current_next_node = current_node.get_next_node()
            current_node.set_next_node(current_next_node.get_next_node())
            current_next_node = None
        current_node = current_next_node

ll=LinkedList()
ll.insert_beginning(15)
ll.insert_beginning(150)
ll.insert_beginning(315)
ll.insert_beginning(1)
print ll.stringify_list()
ll.remove_node(315)
print ll.stringify_list()
