import random


def main():
	a = random.sample(range(1, 100), 1000)
	b = [None]*100
	c = [None]*100
	for i in a:
		if b[i] != None:
			if b[i] == i:
				c[i] += 1
			else:
				

if __name__ == '__main__':
	main()

