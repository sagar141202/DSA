# Count Primes (Sieve)

## Problem Statement
Given an integer n, write a function to return the number of prime numbers less than n. A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. The function should be efficient and handle large inputs. For example, if n = 10, the function should return 4, since there are 4 prime numbers less than 10: 2, 3, 5, and 7.

## Approach
The approach to solve this problem is to use the Sieve of Eratosthenes algorithm, which is an efficient method for finding all primes smaller than a given number. The algorithm works by iteratively marking the multiples of each prime number starting from 2. The numbers that are left unmarked are primes.

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
            // If p is a prime, mark its multiples as not prime
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
- The Sieve of Eratosthenes algorithm is an efficient method for finding all primes smaller than a given number.
- The algorithm has a time complexity of O(n log log n) and a space complexity of O(n), making it suitable for large inputs.
- The algorithm works by iteratively marking the multiples of each prime number starting from 2, leaving the prime numbers unmarked.