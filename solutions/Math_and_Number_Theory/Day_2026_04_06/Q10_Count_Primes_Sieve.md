# Count Primes (Sieve)

## Problem Statement
The problem requires us to count the number of prime numbers less than or equal to a given number, n. A prime number is a positive integer that is divisible only by itself and 1. The input will be an integer n, and the output will be the count of prime numbers less than or equal to n. For example, if n = 10, the output will be 4 because there are 4 prime numbers (2, 3, 5, 7) less than or equal to 10. The constraint is 0 <= n <= 5 * 10^6.

## Approach
We will use the Sieve of Eratosthenes algorithm to solve this problem. The algorithm works by iteratively marking the multiples of each prime number starting from 2. The numbers in the list that are left unmarked are primes. We will create a boolean array, prime, of size n+1 and initialize all entries as true. Then, we will iterate over the array and mark the multiples of each prime number as false.

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
        
        // Iterate over the array and mark the multiples of each prime number as false
        for (int i = 2; i * i <= n; i++) {
            if (prime[i]) {
                for (int j = i * i; j <= n; j += i) {
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
- The Sieve of Eratosthenes algorithm is an efficient way to find all prime numbers up to a given number, n.
- The algorithm has a time complexity of O(n log log n) and a space complexity of O(n).
- The algorithm can be used to solve problems that require finding prime numbers within a given range.