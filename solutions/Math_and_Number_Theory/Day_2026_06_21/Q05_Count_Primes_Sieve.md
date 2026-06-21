# Count Primes (Sieve)

## Problem Statement
Given an integer n, write a function to count the number of prime numbers less than or equal to n. A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. For example, if n = 10, the prime numbers less than or equal to 10 are 2, 3, 5, 7, so the output should be 4. The input n will be in the range [1, 10^6].

## Approach
The Sieve of Eratosthenes algorithm is used to solve this problem, which works by iteratively marking the multiples of each prime number starting from 2. The intuition is to keep track of the prime numbers and mark their multiples as non-prime. This approach allows us to find all prime numbers up to n in a single pass.

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
        for (int i = 2; i * i < n; i++) {
            // If i is a prime, mark its multiples as non-prime
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
- The Sieve of Eratosthenes is an efficient algorithm for finding all prime numbers up to a given number n.
- The time complexity of the Sieve of Eratosthenes is O(n log log n), making it suitable for large inputs.
- The space complexity is O(n), which can be a limitation for very large inputs.