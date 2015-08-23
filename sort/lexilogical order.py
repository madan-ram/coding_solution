# Enter your code here. Read input from STDIN. Print output to STDOUT
num_input = input()
print num_input
for _ in xrange(num_input):
    isNoAns = True
    word = raw_input()
    pos = 0
    nextMinPos = 0
    minNum = 999999
    wordList = [c for c in word]
    if len(word) >= 2:
        for i in xrange(len(word)-1):
            #print ord(word[len(word)-2-i]), ord(word[len(word)-1-i]) , "------"
            if ord(word[len(word)-2-i]) < ord(word[len(word)-1-i]):
                isNoAns = False
                pos = len(word)-2-i
                count = 0
                for char in word[pos+1:]:
                	if ord(char)-ord(word[pos]) > 0 and ord(char)-ord(word[pos]) < minNum:
                		minNum = ord(char)-ord(word[pos])
                		nextMinPos = pos+1+count
                		count += 1
                break
        if isNoAns:
            print "no answer"
        else:
        	wordList[pos], wordList[nextMinPos] = wordList[nextMinPos], wordList[pos]
        	print ''.join(wordList)
    else:
        print "no answer"