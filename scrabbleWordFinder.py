allwords = []  #List of all the words in dictionary file
file = open('dictionary.txt','r') 
for eachword in file: 
  allwords.append(eachword.strip()) 
file.close()

letterwords = []
truewords = []
letters = input('ENTER letters: ')

letterscores = {'a' : 1, 'b' : 3, 'c' : 3, 'd' : 2, 'e' : 1, 'f' :  4, 'g' : 2, 'h' : 4, 'i' : 1, 'j' :8, 'k' :5, 'l' :1, 'm' :3, 'n' :1, 'o' :1, 'p' : 3, 'q' : 10, 'r' : 1, 's' : 1, 't' : 1, 'u' : 1, 'v' : 4, 'w' : 4, 'x' : 8, 'y' : 4, 'z' : 10}

def findbestword():
  bestword = ''
  bestscore = 0
  
  for word in truewords:
    score = 0
    for let in word: 
      
      letterpoint = letterscores[let]
      score = score + letterpoint
     
    if score != 0: 
      if score > bestscore:
        bestscore = score 
        bestword = word 
  print(bestword, bestscore) 
  
  
for word in allwords:  #Searches through all the words  
  spell = True 
  
  for letter in word:  #Checks that each letter of the word is in the INPUT letters 
    if letter not in letters: 
      spell = False
  if spell == True: 
    letterwords.append(word)  #List of appropriate words

for word in letterwords:  #Checks for correct amount of each letter in the word
    valid = True 
    

    for letter in word:
      if letter not in letters: 
        valid = False
      elif word.count(letter) > letters.count(letter): 
        valid = False
        
    if valid == True: 
      truewords.append(word) #List of FULLY appropriate words
    
findbestword()  #Finds word in "truewords" with highest scrabble score
   

