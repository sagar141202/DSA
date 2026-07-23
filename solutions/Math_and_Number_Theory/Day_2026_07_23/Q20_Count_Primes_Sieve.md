# Count Primes (Sieve)

## Problem Statement
Given an integer n, write a function to return the number of prime numbers less than n. A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. For example, the first few prime numbers are 2, 3, 5, 7, 11, and 13. The function should be efficient and scalable for large inputs.

## Approach
The Sieve of Eratosthenes algorithm is used to find all primes smaller than n. It works by iteratively marking the multiples of each prime number starting from 2. The numbers in the list that are left unmarked are primes.

## Complexity
- Time: O(n log log n)
- Space: O(n)

## C++ Solution
```cpp
#include <vector>
using namespace std;

class Solution {
public:
    int countPrimes(int n) {
        vector<bool> sieve(n, true);
        sieve[0] = sieve[1] = false; // 0 and 1 are not prime numbers
        for (int i = 2; i * i < n; i++) {
            if (sieve[i]) {
                for (int j = i * i; j < n; j += i) {
                    sieve[j] = false; // mark multiples of i as non-prime
                }
            }
        }
        int count = 0;
        for (bool isPrime : sieve) {
            if (isPrime) count++;
        }
        return count;
    }
};
```

## Test Cases
```
Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10: 2, 3, 5, and 7.

Input: n = 20
Output: 8
Explanation: There are 8 prime numbers less than 20: 2, 3, 5, 7, 11, 13, 17, and 19.
```

## Key Takeaways
- The Sieve of Eratosthenes is an efficient algorithm for finding all primes smaller than n.
- The time complexity of the Sieve of Eratosthenes is O(n log log n), making it suitable for large inputs.
- The space complexity is O(n), which is used to store the sieve.