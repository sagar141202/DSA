# Count Primes (Sieve)

## Problem Statement
Given an integer n, write a function to return the number of prime numbers less than n. A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. For example, the first few prime numbers are 2, 3, 5, 7, 11, and 13. The function should return the count of all prime numbers less than the given number n.

## Approach
The problem can be solved using the Sieve of Eratosthenes algorithm, which is an efficient method for finding all primes smaller than a given number n. The algorithm iterates through all numbers from 2 to sqrt(n) and marks the multiples of each number as non-prime.

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
        
        // Iterate through all numbers from 2 to sqrt(n)
        for (int i = 2; i * i < n; i++) {
            // If the current number is prime, mark its multiples as non-prime
            if (prime[i]) {
                for (int j = i * i; j < n; j += i) {
                    prime[j] = false;
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
- The Sieve of Eratosthenes algorithm is an efficient method for finding all primes smaller than a given number n.
- The algorithm has a time complexity of O(n log log n) and a space complexity of O(n).
- The algorithm can be used to find the number of prime numbers less than a given number n.