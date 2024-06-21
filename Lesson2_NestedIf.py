#Lesson2_Assignments: Nested If

#Q1 - Task 1

place = input("Choose a place: forest or cave? ")
if place == "forest":  
    action = input("climb a tree or cross a river? ")
    if action == "climb a tree":  
        print("You found a bird's nest!")
    elif action == "cross a river":  
        print("You found a boat!")
    else:
        pass  
elif place == "cave":
    print("You find a hidden treasure!")
else:
    pass


#Task 2

place = input("Choose a place: forest or cave? ")
if place == "forest":
    action = input("climb a tree or cross a river? ")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
    else:
        pass  
elif place == "cave":
    action = input("light a torch or proceed in the dark? ")
    if action == "light a torch":
        print("You find an ancient mural!")
    elif action == "proceed in the dark":
        print("You stumble upon a hidden pit!")
    else:
        pass  
else:
    pass  


#Q2 - Task 1

attendees = int(input("Enter number of attendees: "))  
venue = "large hall" if attendees > 100 else "conference room"
print(venue)


#Task 2

attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
print(venue)
if attendees > 100:
    additional = "audio system"
else:
    additional = "projector"
print(f"Recommended additional item: {additional}")


#Task 3

attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
print(venue)
if attendees > 100:
    additional = "audio system"
else:
    additional = "projector"
print(f"Recommended additional item: {additional}")
catering = input("Do you want vegetarian food? (yes/no): ").strip().lower()
if catering == "yes":
    print("Recommended Caterer: Veggie Delight Caterers")
else:
    print("Recommended Caterer: Gourmet Meals Caterers")
