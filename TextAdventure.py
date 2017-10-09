def DialogOptions(Options):
  count = 96
  print("--------------------------------------------------------------")
  print("Do you: ")
  for Option in Options:
    count += 1
    character = chr(count)
    print("%s) %s"%(character, Option))
  print("--------------------------------------------------------------")
  
print("----------121COM Week 2 Lab Exercise 7----------")
print("----------------<InsertTitleHere>---------------")
print("---------------<Lukas>--------------")
print("\n")

print("You awake in a dark room.  Do you:")
print("a) Scream for help.")
print("b) Press the light switch")
x = input("Enter a or b: ")
if x == "a":
    print("Someone hears your screams...")
    # Another branch
elif x == "b":
    print("The light comes on.")
    print("You do not recognise the room but you have a really bad feeling...")
    DialogOptions(["Look around", "Inspect the bed"])
    if x == 
else:
    print("That was not an option.  Game Over")

