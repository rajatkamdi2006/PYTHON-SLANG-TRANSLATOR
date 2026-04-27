slang_dictionary = {
"LOL":"Laughing Out Loud",
"BRB":"Be Right Back",
"G2G": "Got To Go",
"IDK" : "I Don't Know",
"TBH": "To Be Honest",
"FR" : " For Real",
"IKR" : "I Know Right",
"WTF": "What The Fuck!",
"GOAT":"Greatest of all time",
"FYI":"For Your Information"
}

print("-------Welcome to the Slang Translator------\n")

while True:
   print("Available words in the dictionary :BRB,G2G,IKR,WTF,FR,GOAT,TBH,FYI,LOL,IDK\n")

   word = input("Enter the slang word to find it's' meaning:").upper()

   if word in slang_dictionary:
     print("The word is in the dictionary.")
     
     print("Meaning : ",slang_dictionary[word])
	
   else:
     print("The word is not in the dictionary yet.")
     print("-"*30)
   a = input("Press Enter to continue and 1 to Exit the translator")
   if a =="1":
   	break
   	
   				
	
print("Thanks for using the Slang translator")	

if __name__ == "__main__":
	main()
