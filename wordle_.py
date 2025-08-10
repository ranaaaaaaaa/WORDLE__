import random #library to get a random item from the list

wordle_list = ["which", "their", "there", "about"]
random_item = random.choice(wordle_list)

#print(random_item) #for testing purposes

#This program does not handle duplicates_  [FIXED partially]



for try_ in range (6):
     print ("Write your guess! (MUST BE A VALID WORD OF", len(random_item), "CHARACTERS)")
     attempt = input (">>>>> ").lower()
     if len(attempt) != len(random_item):
         print( len(attempt)," letters, " ,"TRY AGAIN!")
         continue
     correct_letters= ""
     correct_attempts= {}
     failed_attempts= []
     randomitem_list= []
     x= False
     
     for letter in range(len(random_item)):
         randomitem_list.append(random_item[letter])
         

# GREEN if letter is correct and in right position , ORANGE if letter is correct but not in right position while GRAY if the letter is incorrect!
     for i in range(len(attempt)):
         if attempt[i]== random_item[i]:
              print("GREEN")
              print (attempt[i] , "is right at position" , i+1)
              correct_letters += attempt[i]
            #   correct_attempts.append(attempt[i])
              correct_attempts[i]= attempt[i]
              if attempt[i] in randomitem_list:
                  randomitem_list.remove(attempt[i]) #handles duplicates MMKN
         

         elif attempt[i] in randomitem_list:
             will_be_green = False
             for j in range(i+1, len(attempt)):
                 if attempt[j] == random_item[j] and attempt[j] == attempt[i]:
                     will_be_green = True    # helps not get an orange output when the same iterable letter gives green somewhere else in the attempt
                     break
             
             if not will_be_green:
                 print(attempt[i], "ORANGE")
                 if attempt[i] in randomitem_list:
                     randomitem_list.remove(attempt[i])
             else:
                 print(attempt[i], "GREY")
         else:
             print(attempt[i], "GREY")
     
     if correct_letters== random_item:
         print ("YOU DID IT!")    
         break
     
if correct_letters == random_item:
     pass
else:   
     print("Out of tries! The word was:", random_item)