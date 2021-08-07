def isMersenne(n) :
	while (n != 0) :
		r = n % 2;
		if (r == 0) :
			return False;
		n //= 2;
		
	return True;

# Function to return the sum of all the
# Mersenne numbers from the given array
def sumOfMersenne(arr, n) :
	# To store the required sum
	sum = 0;
	for i in range(n) :

		# If current element is a Mersenne number
		if (arr[i] > 0 and isMersenne(arr[i])) :
			sum += arr[i];
	
	return sum;


# Driver code
if __name__ == "__main__" :

	arr = [17, 6, 7, 63, 3 ];
	n = len(arr);
	print(sumOfMersenne(arr, n));
