import fileinput

dictionary = set()

def loaddict(filename):
	try:
		file = open(filename,"r")
		for line in file:
			dictionary.add(line.strip())
		file.close()
	except Exception as e:
		raise e

def dictcheck(w):
	if w in dictionary:
		return True
	return False

def iter_wordsplit(string):
	split_phrase = []
	splitable = iter_split_help(string,split_phrase,0)
	if splitable is False:
		print("NO, cannot be split","\n")
		return None
	else:
		print("YES, can be split")
		split_phrase.reverse()
		split_phrase=" ".join(split_phrase)
		print (split_phrase.rstrip(),"\n")

def iter_split_help(string,phrase,i):
	if dictcheck(string[i:]) is True:
		phrase.append(string[i:])
		return True
	for j in range(i,len(string)):
		if dictcheck(string[i:j+1]) is True:
			if iter_split_help(string,phrase,j+1) is True:
				phrase.append(string[i:j+1])
				return True
	return False

def memoized_wordsplit(string):
	split_phrase = [0]*len(string)
	splitable = memoized_split_help(string,split_phrase,0)
	if splitable is False:
		print("NO, cannot be split","\n")
		return None
	else:
		print("YES, can be split")
		split_phrase = [x for x in split_phrase if type(x) == str]
		split_phrase=" ".join(split_phrase)
		print (split_phrase.rstrip(),"\n")

def memoized_split_help(string,phrase,i):
	if dictcheck(string[i:]) is True:
		phrase[-1] = string[i:]
		return True
	if phrase[i] == -1:
		return False
	for j in range(i,len(string)):
		if dictcheck(string[i:j+1]) is True:
			if memoized_split_help(string,phrase,j+1) is True:
				phrase[j+1] = string[i:j+1]
				return True
	phrase[i] = -1
	return False


def main():
	loaddict("diction10k.txt")
	with fileinput.input() as f:
		nlines = int(f.readline())
		for i in range(nlines):
			line= f.readline().strip()
			print("phrase number:",i+1)
			print(line,"\n")
			print("iterative attempt:")
			iter_wordsplit(line)
			print("recursive attempt:")
			memoized_wordsplit(line)
	fileinput.close()

if __name__ == '__main__':
	main()