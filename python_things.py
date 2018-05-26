#stack:
	list.pop()
	list.append()

#queue:
	q = Queue()
	q.put(item)
	try:
		q.get()

	except Empty exception

#decrementing for loop:
	for i in range(10, 0, -1))


#sort descending:
	list.sort(reverse=True)


#set:
	eg = set()
	#also, = set([list])
	eg.add()
	eg.remove()
	eg.pop()

#tuple:
	tup = ()
	tup1 = (1,)
	tup2 = (1,2)
	tup3 = tup1 + tup2

#list of size:
	x = [0]*100

#class/object oriented 
class Node:
    def __init__(self, value) :       
        self.var=value
    def parent(self):
        return self.var

#strip/split 
	re.split(r'(>+|!+|]+)', string)

#join stuff
s = "-";
seq = ("a", "b", "c");
print s.join( seq )

#global mutex and multithreaded programming 
	#something 

#negative and positive infinity
	 float('Inf')
	-float('Inf')

#throw an exception
raise ValueError('A very specific bad thing happened')

#try and except
try:
    some_code_that_may_raise_our_value_error()
except ValueError as err:
    print(err.args)

class EmptyBinTreeException(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)
