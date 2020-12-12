# Probleme 1

colours = [
    ['red', 'F00'],
    ['yellow', 'FF0'],
    ['green', '0F0'],
    ['cyan', '0FF'],
    ['blue', '00F'],
    ['magenta', 'F0F'],
]
print(f'I have learned the RGB code for {len(colours)} colours so far.')
colour = input("Please enter a colour name: ")
colours_dict =dict(colours) 
print(f'The RGB code for {colour} is {colours_dict[colours]}.')


# Probleme 2

odd_list = [1, 3, 5, 7, 9]
natural_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
odd_set = set(odd_list) 
natural_set = set(natural_list) 
difference_on= odd_set.difference(natural_set)
difference_no= natural_set.difference(odd_set) 
difference_no_list = list(difcerence_no) 
print(difcerence_no_list) 


# # problem 3
locations = ['Italy','Jaban','londan','korea','Africa']
print(locations)
sort_locations = sorted(locations)
print(sort_locations)
print(locations)
sort_locations2 =sorted(sort_locations,reverse=True)
print(sort_locations2)
print(locations)
locations.reverse()
print(locations)
locations.reverse()
print(locations)
locations.sort()
print(locations)
locations.sort(reverse=True)
print(locations)

# Problem 4

guests = ['nicola tesla', 'albert einstine', 'leonardo da vinci']
name = guests[0].title()
print(f"{name}, please come to dinner.")
name = guests[1].title()
print(f"{name}, please come to dinner.")
name = guests[2].title()
print(f"{name}, please come to dinner.")
name = guests[1].title()
print(f"\nSorry, {name} can't make it to dinner.")
guests.pop(1)
guests.insert(1,'Socrates')
name = guests[1].title()
print(f"{name}, please come to dinner.")
print("\nWe got a bigger table!")
guests.insert(3,'Archimedes')
guests.insert(4,'Newton')
guests.append('Plato')
name = guests[3].title()
print(f"{name}, please come to dinner.")
name = guests[4].title()
print(f"{name}, please come to dinner.")
name = guests[5].title()
print(f"{name}, please come to dinner.")
print("\nSorry, we can only invite two people to dinner.")
name = guests.pop()
print(f"Sorry, {name.title()} there's no room at the table.")
name = guests.pop(4)
print(f"Sorry, {name.title()} there's no room at the table.")
name = guests.pop(3)
print(f"Sorry, {name.title()} there's no room at the table.")
name = guests.pop(2)
print(f"Sorry, {name.title()} there's no room at the table.")
name = guests[0].title()
print(f"{name}, please come to dinner.")
name = guests[1].title()
print(f"{name}, please come to dinner.")
print("\nGood food. Good conversation. Bye for now.")
guests.clear()
print(guests)

