"""Pig Latin translator"""
# a language game, where you move the first letter of the word to the end and add "ay".

original = raw_input('Enter a word: ')
  
if len(original) > 0 and original.isalpha():
  print "You word is: " + original

else:
  print 'Try again'

word = original.lower()
first = word[0]
pyg = 'ay'

new_word = word + first + pyg
new_word = new_word[1:len(new_word)]

print "The result is: " + new_word
