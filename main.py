# Title
print(" ++ Tales of the Charm City Knight ++")
# Print a blank line
print()
# Story Introduction
print("You are a noble knight in the year 650 CE, and you're trying to become the most noble of them all.")
# Print a blank line
print()
# Story Introduction (continues)
print("You decide to go on an adventure in the city of Baltimore to earn your glory!")
# Print a blank line
print()


# Display the question
print ("You are outside of the castle grounds, and see three different people asking for help. You could talk to:")
#Dispaly the story options
print ("  a. The local black smith, who needs are rare sword")
print ("  b. The town's teacher, who has a question ")
print ("  c. The king , who needs a brave warrior")
# Prompt the user to slect their story
storySelection = input("Who will you talk to? Please select option a through c: ")
#Print a blank line
print()



if(storySelection == "a"):
  # Display the blacksmith story
  print("You meet with the town blacksmith, looking for a legendary sword.")
  print("They tell you that the legend is that the sword is frozen in ice waiting to be found.")
  print("You choose to search for it:")
  print ("  a. In the Desert")
  print ("  b. In the Forest")
  print ("  c. In the Artic")
  blackSmithanswer = input("Please select option a through c: ")
  # Display the correct blacksmith answer message
  if (blackSmithanswer == "a"):
    print("After looking long and hard through the desert, you've found it - the legendary sword of programming!")
    print("The blacksmith is thrilled and rewards you with a suit of armor worthy of a hero!")
    print("++ The End ++")
# Display the incorrect blacksmith answer message
  elif (blackSmithanswer == "c" or blackSmithanswer == "b"):
    print ("You searched and searched for the rest of your life, but you never found it. It might've been a good idea to heed the balcksmith's advice and go to a cold place")
    print("++ The End ++")


    
elif(storySelection == "b"):
  # Display the teachers story
  print("You meet with the town teacher, who is asking you a question.")
  print("'I have to be honest with you,' they say. I am not really qualified to teach and I am struggling with this question'")
  print("They gesture to a math equation that reads as follows:")
  print()
  print ("y = 6 + 2 + 1")
  print ()
  teacherAnswer = input("Please enter the solution to the problem : ")
  teacherAnswer = int(teacherAnswer)
  print()
  # Display the correct teacher answer message
  if(teacherAnswer == 9):
    print("That makes perfect sense! The teacher cries, and they award you with an honorary degree. ")
    print("You are forever known as one of the smartest in the land !")
  # Display the incorrect teacher answer message
  elif(teacherAnswer != 9 ):
    print ("You tried to the best of your ability, but you never answered it correctly. It might've been a good idea to brush up on your math before seeing the teacher again")
    print("++ The End ++")



elif(storySelection == "c"):
# Display the Kings story
  print("You meet with the king of Baltimore, looking for a noble warrior.")
  print('I need someone to conquor a nearby dragon to save the kingdom! There is no time, head east and be ready for battle!')
  print()
  print("You head to east Baltimore and find the dragon. You ready yourself for battle. But the twist, the dragon asks you to solve a riddle in exchange for your kingdom.")
  print()
  print() #Display the kings question
  print("What two numbers, when added together, equal ten?")
  print()
  print("You ponder for a moment. There's multiple answers to this question, aren't there?")
  print("After thinking for a moment, you answer with two numbers..")
   # Ask for answer one
  kingAnswerone = input("Enter the first number: ")
  kingAnswerone = int(kingAnswerone)
   # Ask for answer two
  kingAnswertwo = input("Enter the second number: ")
  kingAnswertwo = int(kingAnswertwo)
  # Display the correct teacher answer message
  if(kingAnswerone + kingAnswertwo == 10):
    print(f"Ah yes, {kingAnswerone} and {kingAnswertwo} add up to 10! the dragon explained")
    print("The dragon decides to leave your kingdom alone, and the King declares you are the greatest hero in the land!")
    print("++ The End ++")
   # Display the incorrect message
  elif(kingAnswerone + kingAnswertwo != 10):
    print(" Oh no, the numbers you selected do not add up to 10! the dragon explained")
    print(" The Dragon decides to destroy your kingdom and declares that you are unfit King!")
    print("++ The End ++")