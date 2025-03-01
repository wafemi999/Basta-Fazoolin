class Menu():
  def __init__(self, name,items,start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time


  def __repr__(self):
    return f"{self.name} is available from {self.start_time}am to {self.end_time}pm"

  def calculate_bill(self, purchased_items):
    total = 0
    for item in purchased_items:
      total += self.items[item]
    return total


brunch_items = {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}


brunch = Menu("brunch",brunch_items,11,16)

early_bird_items =  {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}
early_bird = Menu("early_bird", early_bird_items, 15, 18)

dinner_items = {
  'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}

dinner = Menu("Dinner", dinner_items, 17,23 )

kids_items = {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}

kids = Menu("kids", kids_items, 11, 21)

# Test Brunch:
print(brunch)
print(f"Bill for breakfast: ${brunch.calculate_bill(['pancakes', 'home fries', 'coffee'])}")


#Test Early bird:
print(early_bird)
print(f"Bill for breakfast: ${early_bird.calculate_bill(['salumeria plate','mushroom ravioli (vegan)' ])} ")


#expansion of Basta Fazoolin'
class Franchise:
 
  def __init__(self,address, menus):
    self.address = address
    self.menus = menus


  def __repr__(self):
    return f"restaurant is located at: {self.address}"
  
  def available_menus(self, time,):
    available_menus  = []
    for menu in self.menus:
      if menu.start_time <= time <= menu.end_time:
        available_menus.append(menu)
    
    return available_menus

# Testing Franchise:
menus = [brunch, early_bird, dinner, kids]
flagship_store = Franchise("1232 West End Road", menus)
new_installment = Franchise("12 East Mulberry Street", menus)

print("\nTesting available menus at different times:")
print("Available at 12 noon:")
print(flagship_store.available_menus(12))
print("\nAvailable at 5pm:")
print(flagship_store.available_menus(17))



class Business:
  def __init__(self,name,franchises):
    self.name = name
    self.franchises = franchises


basta  = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])

#Arepa available:

arepas_menu = {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}

arepas_place = Franchise("189 Fitzgerald Avenue", [arepas_menu])





    






  






