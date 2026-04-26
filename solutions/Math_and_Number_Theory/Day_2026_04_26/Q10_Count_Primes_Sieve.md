# Count Primes (Sieve)

## Problem Statement
Given an integer n, write a function to return the number of prime numbers less than or equal to n. A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. For example, the first few prime numbers are 2, 3, 5, 7, 11, etc. The function should be efficient and handle large inputs.

## Approach
The Sieve of Eratosthenes algorithm is used to find all primes smaller than n. It works by iteratively marking the multiples of each prime number starting from 2. The numbers in the list that are left unmarked are primes. This approach is efficient for large inputs.

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
Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than or equal to 10: 2, 3, 5, 7.

Input: n = 20
Output: 8
Explanation: There are 8 prime numbers less than or equal to 20: 2, 3, 5, 7, 11, 13, 17, 19.
```

## Key Takeaways
- The Sieve of Eratosthenes is an efficient algorithm for finding all primes smaller than n.
- The algorithm has a time complexity of O(n log log n) and a space complexity of O(n).
- The solution uses a boolean array to mark the multiples of each prime number, making it efficient for large inputs.