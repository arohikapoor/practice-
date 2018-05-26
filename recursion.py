def recur(checklist, addlist):
	print 'X'
	addlist_curr = list(addlist)
	
	if len(checklist) == 0:
		return addlist_curr
	addlist_curr.append(1)
	return recur(checklist[1:], addlist_curr)



def combinedword(word, addlist, my_dict):
	if len(word) == 0:
		return (True, [])

	for i in range(0,len(word)):
		print 'not if', i, word[0:i+1] 
		if (word[0:i+1] in my_dict):
			print 'if', i, word[0:i+1] 
			res = combinedword(word[i+1:], addlist, my_dict)
			if res[0] == True:
				print 'res True', res
				addlist_curr = list(res[1])
				addlist_curr.append(word[0:i+1])
				return (True, addlist_curr)
	return (False, [])




