import time, sys

def DialogOptions(Options):     # Function declaration, takes a list of Options
  count = 97                    # Starts from a character 'a'
  print("--------------------------------------------------------------")
  print("Do you: ")
  for Option in Options:        # For every sentence seperated by comma:
    character = chr(count)      # Converts number to ASCII equivalent
    count += 1                  # Adds a 1 for the next letter
    print("%s) %s"%(character, Option)) # Prints the option
  

def DialogResults(Results):
  count = 97
  x = input("Enter your choice: ")    
  print("--------------------------------------------------------------")
  for Choice in Results:                # For every choice in Results    
    if x == chr(count):                 # Compare the choice with a character
      print("%s"%(Results[count - 97])) # Print the chosen choice
      time.sleep(2)
      return x
    count += 1                          # Increment the count after comparing the current one
  
  
def GameOver():
  print("\n*************")
  print("* Game over *")
  print("*************")
  return True

isGameOver = False

print("----------121COM Week 2 Lab Exercise 7----------")
print("----------------<The Dungeon of Silliness>---------------")
print("---------------<Author: Lukas>--------------")
print("\n")

print("You awake in a dark room.")
time.sleep(2)
print("--------------------------------------------------------------\nDo you:")
print("a) Scream for help.")
print("b) Press the light switch")
x = input("Enter a or b: ")
if x == "a":
    print("--------------------------------------------------------------\nSomeone hears your screams...")
    print("Sadly it's not the developer of this branch.")
    time.sleep(2)
    GameOver()
    # Another branch

elif x == "b":
    print("--------------------------------------------------------------\nThe light comes on.")
    print("You do not recognize the room but you have a really bad feeling...")
    time.sleep(2)
    DialogOptions(["Turn off the light", 
                   "Look around"])
    
    x = DialogResults(["You turn off the light. \nUnexpectedly it's hard to see anything. You can hear a silent whisper: \"What a moron\" \nWho's there? - You shout into the void but nobody answers.",
                       "You look around. \nAll you can see are walls of concrete, a door and a small opening in the wall."])
    if x == "a":
      DialogOptions(["Turn on the light", 
                     "Give up"])
      
      x = DialogResults(["'Let there be light.'\nUnlucky, the switch is broken. Looks like you're stuck here forever.", 
                         "You have an existencial crisis and eventually die from thirst."])
      isGameOver = GameOver()
      
    if x == "b" and not isGameOver:
      DialogOptions(["Open the door", 
                     "Check the small opening in the wall"])
      x = DialogResults(["You open the door in front of you.\n You see a long corridor and at the end of it notice a narrow, white figure.\n It's a skeleton!\n You close the door, it's too spooky.\n Suddenly, you remember an old superstition, something you should say after you see a skeleton.",
                     "It takes you a while to pry out a large enough portion of the wall to fit your hand in but you manage to do it.\nYou find a piece of paper. It reads:\n \"Don't forget to thank Mr. Skeltal for good bones.\""])      
      if x == "a":
        DialogOptions(["Say \"thank mr skeltal\"", "Don't do anything"])
        x = DialogResults(["Suddendly you hear a loud \"DOOT DOOT\", skeleton breaks the door and slays you. Should've thanked him faster.",
                       "You slip and die. Poor you."])
      elif x == "b":
        DialogOptions(["Say \"Mr Skeltal thank for calcium and good bones\"",
                       "Say \"This is stupid\""])
        x = DialogResults(["Suddenly you hear a loud \"DOOT DOOT\", skeleton breaks the door and slays you. Such is life (or death in this case).",
                           "You hear a strange noise, that you could only describe as bones rattling, on the other side of the door. As you try to get your bearings a skeleton breaks in and slays you."])      
      isGameOver = GameOver()
else:
    print("That was not an option.")
    isGameOver = GameOver()

