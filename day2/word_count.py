#counts the number of times a word appears in a sentence.

def word_count( words):
	
	sent = words.split()
	counter = {}

	for word in sent:
		if word in counter:
			counter[word] += 1 
		else:
			counter[word] = 1	
				
	return counter 


