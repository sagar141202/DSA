# Count Primes (Sieve)

## Problem Statement
Given an integer n, write a function to return the number of prime numbers less than or equal to n. A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. For example, the first few prime numbers are 2, 3, 5, 7, 11, and 13. The function should be efficient and scalable for large inputs.

## Approach
The Sieve of Eratosthenes algorithm is used to find all prime numbers up to a given limit. This algorithm iterates over the numbers from 2 to the square root of the limit, marking the multiples of each number as non-prime. The remaining unmarked numbers are prime.

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
        
        // Iterate over the numbers from 2 to the square root of n
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
Explanation: The prime numbers less than or equal to 10 are 2, 3, 5, and 7.

Input: n = 20
Output: 8
Explanation: The prime numbers less than or equal to 20 are 2, 3, 5, 7, 11, 13, 17, and 19.
```

## Key Takeaways
- The Sieve of Eratosthenes algorithm is an efficient method for finding all prime numbers up to a given limit.
- The algorithm has a time complexity of O(n log log n) and a space complexity of O(n).
- The algorithm can be optimized by only iterating up to the square root of the limit.