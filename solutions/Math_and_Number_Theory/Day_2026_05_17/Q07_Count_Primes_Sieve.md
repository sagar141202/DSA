# Count Primes (Sieve)

## Problem Statement
Count the number of prime numbers less than or equal to a given number, n. A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. The input will be an integer n, where 2 <= n <= 5 * 10^6. For example, if n = 10, the output should be 4, because there are 4 prime numbers (2, 3, 5, 7) less than or equal to 10.

## Approach
The approach is to use the Sieve of Eratosthenes algorithm, which iteratively marks the multiples of each prime number starting from 2. The numbers in the list that are left unmarked are primes. This algorithm is efficient for finding all primes smaller than a given number.

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
        sieve[0] = sieve[1] = false;
        for (int i = 2; i * i < n; i++) {
            if (sieve[i]) {
                for (int j = i * i; j < n; j += i) {
                    sieve[j] = false;
                }
            }
        }
        int count = 0;
        for (bool b : sieve) {
            if (b) count++;
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
- The Sieve of Eratosthenes is an efficient algorithm for finding all primes smaller than a given number.
- The algorithm works by iteratively marking the multiples of each prime number starting from 2.
- The time complexity of the algorithm is O(n log log n), making it suitable for large inputs.