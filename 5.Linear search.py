list = [4,1,2,5,3] #Set up array
search = int(input("Enter search number")) # Ask for a number
for i in range(0,len(list)): # Repeat for each item in list
    if search==list[i]: #if item at position i is search time
        print(str(search)+"found at position " + str(i)) #Report found
