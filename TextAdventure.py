def DialogOptions(Options):     # Function declaration, takes a list of Options
  count = 97                    # Starts from a character a
  print("--------------------------------------------------------------")
  print("Do you: ")
  for Option in Options:        # For every sentence seperated by comma:
    character = chr(count)      # Converts number to ASCII equivalent
    count += 1                  # Adds a 1 for the next letter
    print("%s) %s"%(character, Option)) # Prints the option
#    print("Worked properly %i"%(count - 97))
  

def DialogResults(Results):
  count = 97
  x = input("Enter your choice: ")    
  print("--------------------------------------------------------------")
  for Choice in Results:                # For every choice in Results    
    if x == chr(count):                 # Compare the choice with a character
      print("%s"%(Results[count - 97])) # Print the chosen choice
    count += 1                          # Increment the count after comparing the current one
  
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
    DialogOptions(["Turn off the light", 
                   "Look around"])
    
    DialogResults(["You turn off the light. \nUnexpectedly it's hard to see anything. You can hear a silent whisper: \"What a moron.\" \nWho's there? - You shout into the void but nobody answers.",
                   "You look around. \nAll you can see are walls of concrete, a door and a small opening in the wall."])
    print(x)
    if x == "a":
      DialogOptions(["Turn on the light", 
                     "Give up"])
      
      DialogResults(["Let there be light.\n", 
                     "You have an existencial crisis and eventually die from thirst."])
else:
    print("That was not an option.  Game Over")

