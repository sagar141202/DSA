# Count Primes (Sieve)

## Problem Statement
Given an integer n, write a function to return the number of prime numbers less than n. A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. The function should be able to handle large inputs efficiently. For example, if n = 10, the function should return 4, because there are 4 prime numbers less than 10: 2, 3, 5, and 7.

## Approach
The Sieve of Eratosthenes algorithm is used to find all primes smaller than n. It iteratively marks the multiples of each prime number starting from 2. The numbers in the list that are left unmarked are primes. This approach provides an efficient solution to the problem.

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
            // If p is a prime, mark as composite all the multiples of p
            if (prime[p]) {
                for (int i = p * p; i < n; i += p) {
                    prime[i] = false;
                }
            }
        }
        
        // Count all prime numbers in the list
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
- The Sieve of Eratosthenes is an efficient algorithm for finding all primes smaller than n.
- The time complexity of the Sieve of Eratosthenes is O(n log log n), making it suitable for large inputs.
- The space complexity of the Sieve of Eratosthenes is O(n), which can be a limitation for very large inputs.