class Hotel:
 rooms = 42 # preset that the hotel has 42 rooms
def countRooms (self): # Reference to its own class
#return the number of rooms that exist
 return self.rooms
def setRooms (self, numberOfRooms):   #set the number of rooms
 self.rooms = numberOfRooms
 return
# define a new instance of the Hotel clas
newHotel = Hotel
# output the number of rooms
print(newHotel.countRooms())
# set the number of rooms to 30
newHotel.setRooms(30)
