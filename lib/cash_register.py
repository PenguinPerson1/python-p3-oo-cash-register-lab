#!/usr/bin/env python3

class CashRegister:
  def __init__(self,discount=0):
    self.discount = discount
    self.total = 0
    self.items = []

  def add_item(self,title,price,amount=1):
    self.last_item = {"title":title,"price":price,"amount":amount}
    for i in range(amount):
      self.items.append(title)
      self.total = self.total+price

  def apply_discount(self):
    if self.discount == 0:
      print("There is no discount to apply.")
    else:
      self.total = round( self.total*((100-self.discount)/100) )
      print(f"After the discount, the total comes to ${self.total}.")

  def void_last_transaction(self):
    for i in range(self.last_item["amount"]):
      self.items.pop()
      self.total = self.total-self.last_item["price"]
