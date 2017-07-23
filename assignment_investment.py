# investment calculator
# Real Python Book Page 61 Assignment

def invest(amount, rate, time):
	print('principal amount: ${}'.format (amount))
	print('annual rate of return:', rate)

	for n in range(1, time + 1):
		growth = amount * rate
		amount = amount + growth
		print('year {}: ${}'.format(n, amount))
	print()

invest(100, 0.05, 8)
invest(2000, 0.025, 5)
