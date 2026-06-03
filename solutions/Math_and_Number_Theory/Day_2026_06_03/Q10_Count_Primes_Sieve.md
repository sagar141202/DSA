# Count Primes (Sieve)

## Problem Statement
Count the number of prime numbers less than or equal to a given number `n`. A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. For example, the first few prime numbers are 2, 3, 5, 7, 11, and 13. The input `n` will be in the range [2, 5 * 10^6]. The output should be the count of prime numbers less than or equal to `n`.

## Approach
The Sieve of Eratosthenes algorithm will be used to solve this problem. This algorithm iterates through all numbers from 2 to the square root of `n`, marking the multiples of each number as non-prime. The remaining unmarked numbers are prime.

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
Explanation: The prime numbers less than or equal to 10 are 2, 3, 5, and 7.

Input: n = 20
Output: 8
Explanation: The prime numbers less than or equal to 20 are 2, 3, 5, 7, 11, 13, 17, and 19.
```

## Key Takeaways
- The Sieve of Eratosthenes algorithm is an efficient method for finding all prime numbers up to a given number `n`.
- The time complexity of the Sieve of Eratosthenes algorithm is O(n log log n), making it suitable for large inputs.
- The space complexity of the Sieve of Eratosthenes algorithm is O(n), as it requires a boolean array of size `n` to keep track of prime numbers.