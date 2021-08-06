#937. Reorder Data in Log Files
#letter log sort using tuple to put into list, then switch id and content and switch back
#time: O(NlogN) cause order, space O(N)
 def reorderLogFiles(self, logs: List[str]) -> List[str]:
	digit = []
	letter = []
	for log in logs:
		id, content = log.split(" ",maxsplit=1)#only split 2 size
		if content[0].isdigit():
			digit.append(log)
		else:
			letter.append((content,id))#switch id and content order
	letter.sort()#first based on content, if content same using id
	return [l[1]+" "+l[0] for l in letter] + digit#each l is a tuple, l[0] is content and l[1] is id