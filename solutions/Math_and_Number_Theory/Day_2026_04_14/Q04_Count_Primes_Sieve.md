# Count Primes (Sieve)

## Problem Statement
Count the number of prime numbers less than or equal to a given number, n. A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. The function should take an integer n as input and return the number of prime numbers less than or equal to n. For example, if n = 10, the output should be 4, because there are 4 prime numbers (2, 3, 5, 7) less than or equal to 10. The input n will be in the range [0, 1000000].

## Approach
The Sieve of Eratosthenes algorithm is used to find all prime numbers up to a given number, n. This algorithm works by iteratively marking the multiples of each prime number starting from 2. The numbers that are left unmarked are prime numbers. The algorithm uses a boolean array to mark the prime numbers.

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
        if (n <= 2) return 0;
        
        vector<bool> sieve(n, true);
        sieve[0] = sieve[1] = false;
        
        for (int i = 2; i * i < n; i++) {
            if (sieve[i]) {
                for (int j = i * i; j < n; j += i) {
                    sieve[j] = false;
                }
            }
        }
        
        int count = 0;
        for (int i = 2; i < n; i++) {
            if (sieve[i]) count++;
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
- The Sieve of Eratosthenes algorithm is an efficient way to find all prime numbers up to a given number, n.
- The algorithm has a time complexity of O(n log log n) and a space complexity of O(n).
- The algorithm uses a boolean array to mark the prime numbers, and the numbers that are left unmarked are prime numbers.