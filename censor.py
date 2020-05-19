# Censoring the word in the text 
def censor(text, word):
  new_text = text.split()
  star = "*" * len(word)
  count = 0
  for item in new_text:
    if item == word:
      new_text[count] = star
    count += 1
      #print word
    result = " ".join(new_text)
  return result   
  #return " ".join(new_text)
      
print censor("how are you", "you" )


"""o/p: how are ***"""