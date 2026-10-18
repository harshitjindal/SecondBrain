1. Striver’s Calculate HCF and LCM: https://practice.geeksforgeeks.org/problems/lcm-and-gcd4516/1
	1. Calculate HCF, and use property: HCF x LCM = Product of numbers
	2. Calculate HCF using Euclid’s algorithm
	3. Code

```
long long calcHCF(long long A, long long B) {
	long long temp = max(A,B);
	B = min(A, B);
	A = temp;
	long long remainder = A % B;
	    
	// A = B * quotient + remainder
	while (remainder != 0) {
		A = B;
		B = remainder;
		remainder = A % B;
	}
	return B;
 }
```
