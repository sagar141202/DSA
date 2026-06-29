# Count Primes (Sieve)

## Problem Statement
The problem requires us to count the number of prime numbers less than or equal to a given number `n`. A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. The input is an integer `n`, and the output is the count of prime numbers less than or equal to `n`. For example, if `n` is 10, the output should be 4, because there are 4 prime numbers (2, 3, 5, 7) less than or equal to 10.

## Approach
We will use the Sieve of Eratosthenes algorithm, which iteratively marks the multiples of each prime number starting from 2. The algorithm works by iteratively marking the multiples of each prime number, effectively creating a sieve that separates the prime numbers from the non-prime numbers. This approach allows us to efficiently count the number of prime numbers less than or equal to `n`.

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
        
        // Iterate over the array starting from 2
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
- The algorithm works by iteratively marking the multiples of each prime number, effectively creating a sieve that separates the prime numbers from the non-prime numbers.