#when you run this file from the command line with a txt file 
#it counts the words in the txt file
# then writes to a new file with a new name based on the txt file, like txt_count.txt


import sys, operator

with open(sys.argv[1], 'r') as file_obj:
	file = file_obj.read()
	sample = sys.argv[1]
wordlist = file.lower().split() # splits the text string into a list of words

tally = {}
for word in wordlist: #puts the words in the dictionary
	tally[word] = 0
for word in wordlist: #counts how many times the word appears
	tally[word] += 1

once_words = []  #words that only appear once
for key, value in tally.items():
	if value == 1:
		once_words.append(key)
total = 0
for key, value in tally.items():  #calculates the average word length
	total += len(key) * value
avg_len = int(total/len(wordlist))

sorted_tally = sorted(tally.items(), key=operator.itemgetter(1), reverse = True) 

new_file = open(sample[:-4] + "-count" + sample[-4:], "w")
new_file.write("There are {} words in the sample.\nThere are {} unique words.\nThere are {} words that appear only once.\nThe average word length is {}.\n\n".format(len(wordlist), len(tally), len(once_words), avg_len))

for info in sorted_tally:
	new_file.write("{} -- {}\n".format(info[0], info[1]))
new_file.close()

