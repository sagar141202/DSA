# Count Primes (Sieve)

## Problem Statement
The problem requires us to count the number of prime numbers less than or equal to a given number `n`. A prime number is a positive integer that is divisible only by itself and 1. The input is an integer `n`, and the output is the count of prime numbers less than or equal to `n`. For example, if `n = 10`, the output should be `4` because there are 4 prime numbers less than or equal to 10: 2, 3, 5, and 7.

## Approach
The approach is to use the Sieve of Eratosthenes algorithm, which iteratively marks the multiples of each prime number starting from 2. The numbers that are not marked are prime numbers. This algorithm has a time complexity of O(n log log n) and a space complexity of O(n).

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
            // If p is a prime number, mark its multiples as not prime
            if (prime[p]) {
                for (int i = p * p; i < n; i += p) {
                    prime[i] = false;
                }
            }
        }
        
        // Count the number of prime numbers
        int count = 0;
        for (int i = 0; i < n; i++) {
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
- The Sieve of Eratosthenes algorithm is an efficient way to find all prime numbers up to a given number `n`.
- The algorithm has a time complexity of O(n log log n) and a space complexity of O(n).
- The algorithm can be used to solve other problems related to prime numbers, such as finding the `k`-th prime number or checking if a number is prime.