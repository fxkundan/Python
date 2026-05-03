# Last updated: 04/05/2026, 00:33:41
class Solution:
	def addBinary(self, a: str, b: str) -> str:
		aLen = len(a)
		bLen = len(b)

		# make both strings same length
		if aLen < bLen:
			while aLen < bLen:
				a = "0" + a
				aLen += 1
		elif bLen < aLen:
			while bLen < aLen:
				b = "0" + b
				bLen += 1

		addition = 0
		carry = 0
		ansString = ""

		# add each character
		for i in range(aLen-1,-1,-1):
			addition = int(a[i])+int(b[i])+carry
			# if we have a carry situation
			if addition > 1:
				# the carry value will be whatever was added divided by 2, rounded down
				# e.g. remainder 3, the carry will be 1
				carry = int(addition/2)
				# the addition will always either be 0 or 1, determined by if the sum is even or not
				# i.e. if addition is even, the sum will be 0, and odd he sum will be 1
				addition %= 2
			else:
				carry = 0
			ansString = str(addition) + ansString

		# if there are any leftovers, append any additions to the end
		if carry > 0:
			while carry > 0:
				ansString = str(carry%2) + ansString
				carry -= 2

		return ansString