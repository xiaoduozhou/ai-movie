import sys
sys.path.append("../dbi")
sys.path.append("../nlu")
import nlu
import dbi
import dmp
import dm
import dr

choice = ["something", "testing", "hmmm"]
memory = list()
memory = set(memory)

memoryTrivia = list()
memoryTrivia = set(memoryTrivia)

N = nlu.NLU()
   
while choice[0] != "quit":

   input = raw_input("Alright, input something punk: ")
   choice = N.process(input)

   if choice[0] == "like" or choice[0] == "dislike":
      memory = dmp.generateMoviePreferenceList(choice, memory)
   if choice[0] == "trivia":
      memoryTrivia = dm.trivia(choice)
   if choice[0] == "true_false":
      memoryTrivia = dm.trueFalse(choice)
      
   print "choice is = ", choice
                           
   dr.dialogueResolution(choice, memory, memoryTrivia)