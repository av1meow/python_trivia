score = 0
print("Welcome to Amanda's Horriffic Triva" )
begin = input("Would You Like To Play A Game?: " )
if begin == "yes":
  
  print("Who played Pennywise in It?: ")
  print("a. Jhonny Depp")
  print("b. Tim Curry")
  print("c. Robert Englund")
  q1 = input ("> ")
  if q1 == "b":
    print("We all Float down here!, Yes ")
    score = score + 1
  else:
    print("Your No Fun!")
    
  print("")
  
  print("Who was the killer in Friday the 13th?: ")
  print("a. Pamela Voorhees")
  print("b. Elias Voorhees")
  print("c. Jason Voorhees")
  q2 = input ("> ")
  if q2 == "a":
    print("And Today Is His Birthday! Yes")
    score = score + 1
  else:
    print("Your No Fun!")
    
  print("")
  
  print("Who directed the movie Plan 9 From Outer Space?: ")
  print("a. Edd D Wood Jr")
  print("b. Tim Burtton")
  print("c. Sam Raimi")
  q3 = input ("> ")
  if q3 == "a":
    print("We Got Bela Lagousi! Yes")
    score = score + 1
  else:
    print("Your No Fun!")
    
  print("")
    
  print("How many main clowns are in Killer Clowns From Outer Space?: ")
  print("a. to many clowns")
  print("b. 5")
  print ("c.8 ")
  q4 = input("> ")
  if q4 == "c":
      print("What Are You Gonna Do... Knock My Block Off? Yes")
      score = score + 1
  else:
    print("Your No Fun")
    
  print("")

  print("In the movie Carrie, how does she kill her mother?: ")
  print("a. Burning her alive")
  print("b. Hanging her from the celling in there home")
  print("c. Stabbing her to death with knives and tools ")
  q5 = input("> ")
  if q5 == "c":
      print("There All Gonna Laugh At You! Yes")
      score = score + 1
  else:
    print("Your No Fun!")
  
  print("")   
    
  print("In the Movie Christine, what kind of car was she?: ")
  print("a. Chevy Impala")
  print("b. Plymouth Fury")
  print ("c. Dodge Dart")
  q6 = input("> ")
  if q6 == "b":
      print("The Man That Own That Car Last Died In It! Yes")
      score = score + 1
  else:
    print("Your No Fun")
   
  print("")
    
  print("Who was the father of Rosemary's Baby?: " )
  print("a. Satan")
  print("b. Leader Of the Cult")
  print ("c. Guy Woodhouse  Husban")
  q7 = input("> ")
  if q7 == "a":
      print("Snips and snails and puppy dog's tails. Yes")
      score = score + 1
  else:
    print("Your No Fun")

  print("")
    
  print("Who played Prof. Gerald Deemer in the movie Tarantula")
  print("a.  Claude Rains")
  print("b. Jack Nicholson")
  print ("c. Leo G Carol")
  q8 = input("> ")
  if q8 == "c":
      print("No footprints! No blood! No sign of a struggle! The bones just stripped clean like peeling a banana! Yes")
      score = score + 1
  else:
    print("Your No Fun")
    
  print("")

  print("In the movie The Omen, who hangs themselves at Damien's fifth birthday party?: ")
  print("a. The Nanny")
  print("b. The Priest")
  print ("c. A child at his birthday party")
  q9 = input("> ")
  if q9 == "a":
      print("These are knives. He wants me to stab him! He wants me to murder a child. Yes") 
      score = score + 1
  else:
    print("Your No Fun")
    
  print("")
    
  print("In the movie Army Of Darkness what words are to be spooken and what is the name of the book he needs to go back home?: ")
  print("a. Necronomicon, Klaatu barada nikto")
  print("b. Necorncoin, Klaatu Barada Nectar")
  print ("c. The Book Of The Dead, Klaatu Barada necktie")
  q10 = input("> ")
  if q10 == "a":
      print("Shop Smart Shop At S.Mart You Got That! Yes")
      score = score + 1
  else:
    print("Your No Fun")
    
  print("")
  
  print("You Ghoul You Got", str(score)+"/10 Correct")
  
  print("")
  
  print("Thanks for playing have a Happy Halloween!" )