


def fib(n: int):
	
	mem = {0:0,1:1} # store the value seen already 
	def f(x):
		if x in mem:
			return mem[x]

		else:
			mem[x] = f(x-1) + f(x-2)
			return mem[x]
	return f(n)


if __name__ == "__main__":
	n = 10
	print(fib(n))
	print("#"* 20) 



