### **Exercise 3**

#Define a class called `Lunch`.Its `__init__()` method should have two arguments:`self`anf `menu`.
# Where menu is a string. Add a method called `menu_price`.It will involve a `if`statement:

#if "menu 1" print "Your choice:", menu, "Price 12.00", if "menu 2" print "Your choice:", menu, "Price 13.40", else print "Error in menu".

#To check if it works define: `Paul=Lunch("menu 1")` and call `Paul.menu_price()`.

class Lunch:
    def __init__(self,menu):
        self.menu = menu
    def menu_price(self):
        if self.menu == "menu1":
            print("Your choice",self.menu,"Price 12.00")
        elif self.menu == "menu2":
            print("Your choice",self.menu,"Price 13.40")
        else:
            print("Error in menu.")

paul = Lunch("menu1")


paul.menu_price()