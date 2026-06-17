# Count Primes (Sieve)

## Problem Statement
Given an integer n, write a function to return the number of prime numbers less than or equal to n. A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. The function should take an integer n as input and return the count of prime numbers. For example, if n = 10, the output should be 4 because there are 4 prime numbers (2, 3, 5, 7) less than or equal to 10. The input n will be in the range [1, 1000000].

## Approach
The Sieve of Eratosthenes algorithm is used to solve this problem. It works by iteratively marking the multiples of each prime number starting from 2. The numbers in the list that are left unmarked are primes. This approach allows us to find all primes smaller than n when n is smaller than 10 million or so.

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
        vector<bool> sieve(n, true);
        sieve[0] = sieve[1] = false; // 0 and 1 are not prime numbers
        
        // Iterate from 2 to sqrt(n)
        for (int i = 2; i * i < n; i++) {
            // If i is a prime number, mark its multiples as non-prime
            if (sieve[i]) {
                for (int j = i * i; j < n; j += i) {
                    sieve[j] = false;
                }
            }
        }
        
        // Count the number of prime numbers
        int count = 0;
        for (int i = 0; i < n; i++) {
            if (sieve[i]) {
                count++;
            }
        }
        
        return count;
    }
};
```

## Test Cases
```
Input: 10
Output: 4
Input: 20
Output: 8
```

## Key Takeaways
- The Sieve of Eratosthenes is an efficient algorithm for finding all primes smaller than n.
- The time complexity of the Sieve of Eratosthenes is O(n log log n) and the space complexity is O(n).
- This algorithm can be used to find all primes up to a certain limit, making it a useful tool in number theory applications.