import sys
sys.path.append("../dbi")
sys.path.append("../nlu")
import nlu
import dbi
import dmp
import dm
import dr
import pref

Movee = pref.Preference()
choice = ["empty", "empty", "empty"]
#choice = Movee.get_recommendation()
memory = Movee.get_preferenceSet()
memoryTrivia = Movee.get_triviaSet()

N = nlu.NLU()

print "Welcome to the Dialogue Manager! My name is Movee, a highly original name conceived by the most brilliant of the team that designed me. The core functionalities I fascillitate are movie list generation based off of preference, basic trivia, and true/false trivia resolution."
print "... "
raw_input()
print "Oh yeah, I'm supposed to help you right?"
   
while choice[0] != "bye":

   input = raw_input("Alright, how may I help you? ")
   choice = N.process(input)
   
   if not choice:
      choice = ["empty", "empty", "empty"]
      
   if choice[0] == "bye":
      exit()
      
   if choice[0] == "reset":
      memory = Movee.get_preferenceSet()

   print choice
   
   if choice[0] == "like" or choice[0] == "dislike":
      if len(choice) < 3:
         print "Sorry, that inquiry is too vague. Can you elaborate please?"
         continue
      memory = dmp.generateMoviePreferenceList(choice, memory)
   if choice[0] == "trivia":
      memoryTrivia = dm.trivia(choice)
   if choice[0] == "True_False":
      memoryTrivia = dm.trueFalse(choice)
      
   print "choice is = ", choice
                           
   dr.dialogueResolution(choice, memory, memoryTrivia, Movee)