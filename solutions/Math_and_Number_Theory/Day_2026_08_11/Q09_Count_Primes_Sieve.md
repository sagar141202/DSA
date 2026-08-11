# Count Primes (Sieve)

## Problem Statement
Given an integer n, write a function to return the number of prime numbers less than or equal to n. A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. For example, the first few prime numbers are 2, 3, 5, 7, 11, and 13. The function should take an integer n as input and return the count of prime numbers less than or equal to n.

## Approach
The Sieve of Eratosthenes algorithm is used to find all primes smaller than n. It works by iteratively marking the multiples of each prime number starting from 2. The multiples of a given prime are generated as a sequence of numbers starting from that prime, with a constant difference between them that is equal to that prime.

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
        // Create a boolean array, prime, of size n+1
        vector<bool> prime(n + 1, true);
        
        // 0 and 1 are not prime numbers
        prime[0] = prime[1] = false;
        
        // Iterate from 2 to sqrt(n)
        for (int p = 2; p * p <= n; p++) {
            // If p is a prime, mark as composite all the multiples of p
            if (prime[p]) {
                for (int i = p * p; i <= n; i += p) {
                    prime[i] = false;
                }
            }
        }
        
        // Count all prime numbers in the array
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
Explanation: There are 4 prime numbers less than or equal to 10: 2, 3, 5, and 7.

Input: n = 20
Output: 8
Explanation: There are 8 prime numbers less than or equal to 20: 2, 3, 5, 7, 11, 13, 17, and 19.
```

## Key Takeaways
- The Sieve of Eratosthenes is an efficient algorithm for finding all primes smaller than n.
- The algorithm has a time complexity of O(n log log n) and a space complexity of O(n).
- The algorithm works by iteratively marking the multiples of each prime number starting from 2.