def recursive_longest(string, i , j):
	if i == j:
		return 1 
	if i > j:
		return 0

	if string[i] == string[j]:
		return 2 + recursive_longest(string, i + 1, j - 1)
	else:
		return max(recursive_longest(string, i, j-1), recursive_longest(string, i +1, j))

string = "toptensecretsofcs"

print recursive_longest(string, 0, len(string)-1)
