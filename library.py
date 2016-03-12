def getHammingDistance(input1, input2):
	count = 0

	if(len(input1) != len(input2)):							#checks if the 2 inputs have same length
		print"Error! Strings are not equal"
		return
	else:
		length = len(input1)
		if(length > 0):										#checks if the inputs are not empty strings
			while(length != 0):
				if(input1[length-1] == input2[length-1]):	
					length -= 1
				else:										#if char at index length-1 in first input is same in second input, counter increments
					count += 1
					length -= 1

		print"Hamming distance: ", count
	return

def countSubstrPattern(original, pattern):
	end = len(pattern)
	start = 0
	count = 0

	while(end <= len(original)):							#this loop basically checks if the pattern is same with the first n characters
		count += original.count(pattern, start, end)		#of the original string, then increments the start and end of the parameter of 
		start += 1											#the count function
		end += 1
	return	count

def isValidString(string, alphabet):
	isValid = 1	
	for letter in string:
		if(alphabet.find(letter) == -1):					#if a letter in the string does not exist in the alphabet, variable isValid is set
			isValid = 0										#immediately to 0 (false) and breaks through the loop
			break

	if(isValid == 0):
		return False
	else:
		return True

	return

def getSkew(string, n):
	g = 0
	c = 0

	if(len(string) <= 0):									#checks if the string length of input is less than or equal to 0
		print"Given string too short"
		return
	else:
		if(n > len(string)):								#checks if the input number is greater than string length. If yes, prompt user
			print"Given number is larger that string length"#that n must be smaller than string length
			return
		else:
			if(n <= 0):
				print"Error. Can't find skew"
			else:
				for index in range(n):						#this loop checks the string and counts every instances of C and G
					if(string[index] == "G"):
						g += 1
					if(string[index] == "C"):
						c += 1

				return g-c

def getMaxSkewN(string, n):									#this function basically calls the getSkew function with 1 to n input (as n in the parameter)
	max_skew = getSkew(string, n)							#and returns the largest getSkew result
	n -= 1
	
	while(n > 0):
		if(max_skew < getSkew(string, n)):
			max_skew = getSkew(string, n)
		n -= 1

	return max_skew

def getMinSkewN(string, n):									#same as getMaxSkewN, just get the smallest getSkew result
	min_skew = getSkew(string, n)
	n -= 1

	while(n > 0):
		if(min_skew > getSkew(string, n)):
			min_skew = getSkew(string, n)
		n -= 1

	return min_skew