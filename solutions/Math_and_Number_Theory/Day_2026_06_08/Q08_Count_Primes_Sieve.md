# Count Primes (Sieve)

## Problem Statement
Given an integer n, write a function to count the number of prime numbers less than or equal to n. A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. The function should be efficient and scalable for large inputs. For example, if n = 10, the output should be 4, because there are 4 prime numbers (2, 3, 5, 7) less than or equal to 10.

## Approach
The Sieve of Eratosthenes algorithm is used to find all primes smaller than n. It works by iteratively marking the multiples of each prime number starting from 2. The algorithm uses a boolean array to mark the prime numbers, and finally counts the number of primes in the array.

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
        for (int p = 2; p * p < n; p++) {
            // If p is a prime, mark as composite all the multiples of p
            if (prime[p]) {
                for (int i = p * p; i < n; i += p) {
                    prime[i] = false;
                }
            }
        }
        
        // Count all prime numbers in the array
        int count = 0;
        for (int i = 2; i < n; i++) {
            if (prime[i]) {
                count++;
            }
        }
        
        return count;
    }
};

// Example usage:
int main() {
    Solution solution;
    int n = 10;
    int count = solution.countPrimes(n);
    cout << "Number of primes less than or equal to " << n << ": " << count << endl;
    return 0;
}
```

## Test Cases
```
Input: n = 10
Output: 4
Input: n = 20
Output: 8
```

## Key Takeaways
- The Sieve of Eratosthenes is an efficient algorithm for finding all primes smaller than n.
- The algorithm has a time complexity of O(n log log n) and a space complexity of O(n).
- The algorithm uses a boolean array to mark the prime numbers, and finally counts the number of primes in the array.