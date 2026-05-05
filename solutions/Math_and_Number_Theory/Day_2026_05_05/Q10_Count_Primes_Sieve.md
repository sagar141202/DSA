# Count Primes (Sieve)

## Problem Statement
Given an integer n, write a function to return the number of prime numbers less than or equal to n. A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. The function should be efficient and handle large inputs. For example, if n = 10, the output should be 4, since there are 4 prime numbers less than or equal to 10: 2, 3, 5, and 7.

## Approach
The approach is to use the Sieve of Eratosthenes algorithm, which iteratively marks the multiples of each prime number starting from 2. The algorithm uses a boolean array to keep track of prime numbers. The intuition is to eliminate composite numbers by marking their multiples.

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
        vector<bool> isPrime(n, true);
        isPrime[0] = isPrime[1] = false;
        for (int i = 2; i * i < n; i++) {
            if (isPrime[i]) {
                for (int j = i * i; j < n; j += i) {
                    isPrime[j] = false;
                }
            }
        }
        int count = 0;
        for (int i = 2; i < n; i++) {
            if (isPrime[i]) count++;
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
- The Sieve of Eratosthenes algorithm is an efficient method for finding all primes smaller than a given number.
- The algorithm has a time complexity of O(n log log n) and a space complexity of O(n).
- The boolean array isPrime is used to keep track of prime numbers, where isPrime[i] represents whether i is a prime number or not.