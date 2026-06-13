# Count Primes (Sieve)

## Problem Statement
The problem requires us to count the number of prime numbers less than or equal to a given number, n. A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. The input is an integer n, and the output is the count of prime numbers less than or equal to n. For example, if n = 10, the prime numbers less than or equal to 10 are 2, 3, 5, and 7, so the output should be 4. The constraint is 0 <= n <= 5 * 10^6.

## Approach
The Sieve of Eratosthenes algorithm is used to solve this problem, which works by iteratively marking the multiples of each prime number starting from 2. The algorithm uses a boolean array to keep track of prime numbers. We start by assuming all numbers are prime, then we mark the multiples of each prime number as non-prime.

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
- The Sieve of Eratosthenes algorithm is an efficient way to find all prime numbers up to a given number n.
- The time complexity of the algorithm is O(n log log n) due to the iteration over the prime numbers and their multiples.
- The space complexity is O(n) because we need a boolean array of size n to keep track of prime numbers.