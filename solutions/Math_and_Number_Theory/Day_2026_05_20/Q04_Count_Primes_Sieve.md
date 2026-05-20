# Count Primes (Sieve)

## Problem Statement
Given an integer n, write a function to return the number of prime numbers less than or equal to n. The function should be efficient and scalable for large values of n. For example, if n = 10, the output should be 4, because there are 4 prime numbers (2, 3, 5, 7) less than or equal to 10.

## Approach
The Sieve of Eratosthenes algorithm is used to find all prime numbers up to a given number n. It works by iteratively marking the multiples of each prime number starting from 2. The numbers that are left unmarked are prime numbers.

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
- The Sieve of Eratosthenes algorithm is an efficient method for finding all prime numbers up to a given number n.
- The algorithm has a time complexity of O(n log log n) and a space complexity of O(n), making it suitable for large values of n.
- The algorithm can be used to solve problems that involve counting prime numbers or finding prime numbers within a given range.