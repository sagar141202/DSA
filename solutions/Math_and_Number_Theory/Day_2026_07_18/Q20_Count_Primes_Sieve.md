# Count Primes (Sieve)

## Problem Statement
Count the number of prime numbers less than or equal to a given number, n. A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. The input will be an integer n, where 2 <= n <= 5 * 10^6. For example, if n = 10, the output should be 4, because there are 4 prime numbers (2, 3, 5, 7) less than or equal to 10.

## Approach
The Sieve of Eratosthenes algorithm is used to find all primes smaller than n. It iteratively marks the multiples of each prime number starting from 2, effectively creating a list of all prime numbers up to n. The algorithm has a simple and efficient implementation.

## Complexity
- Time: O(n log log n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int countPrimes(int n) {
        // Create a boolean array, prime, of size n
        vector<bool> prime(n, true);
        
        // 0 and 1 are not prime numbers
        prime[0] = prime[1] = false;
        
        // Iterate from 2 to sqrt(n)
        for (int p = 2; p * p < n; p++) {
            // If p is a prime number, mark its multiples as non-prime
            if (prime[p]) {
                for (int i = p * p; i < n; i += p) {
                    prime[i] = false;
                }
            }
        }
        
        // Count the number of prime numbers
        int count = 0;
        for (int i = 2; i < n; i++) {
            if (prime[i]) {
                count++;
            }
        }
        
        return count;
    }
};
```

## Test Cases
```
Input: n = 10
Output: 4
Input: n = 20
Output: 8
```

## Key Takeaways
- The Sieve of Eratosthenes is an efficient algorithm for finding all prime numbers up to a given number, n.
- The time complexity of the Sieve of Eratosthenes is O(n log log n), making it a suitable solution for large inputs.
- The algorithm uses a boolean array to mark non-prime numbers, allowing for a simple and efficient implementation.