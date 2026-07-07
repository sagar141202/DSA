# Factorial Trailing Zeroes

## Problem Statement
The problem requires finding the number of trailing zeroes in the factorial of a given number `n`. The factorial of a number `n` (denoted as `n!`) is the product of all positive integers less than or equal to `n`. A trailing zero is a zero at the end of the number. For example, `5! = 120` has one trailing zero. The input `n` is a positive integer, and the output should be the number of trailing zeroes in `n!`. The constraints are `1 <= n <= 10^5`.

## Approach
The algorithm uses the concept of prime factorization to count the number of trailing zeroes. It counts the number of factors of 5 in all numbers from 1 to `n`, as a trailing zero is formed by a factor of 2 and a factor of 5, and there are usually more factors of 2 than 5.

## Complexity
- Time: O(log n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int trailingZeroes(int n) {
        int count = 0;
        long long i = 5;
        while (n / i >= 1) {
            count += n / i;
            i *= 5;
        }
        return count;
    }
};
```

## Test Cases
```
Input: n = 5
Output: 1
Input: n = 3
Output: 0
```

## Key Takeaways
- The number of trailing zeroes in `n!` is determined by the number of factors of 5 in all numbers from 1 to `n`.
- We use a loop to count the number of factors of 5, 25, 125, and so on, in all numbers from 1 to `n`.
- The time complexity is O(log n) because we are dividing `n` by powers of 5 in each iteration.