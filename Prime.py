class Prime():
	def isPrime(self, number):
		if number <= 1 or number % 2 == 0:
			return number == 2

		for n in range(number - 1, 0):
			if n % number == 0:
				return False

		return True