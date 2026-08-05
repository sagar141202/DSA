# Factorial Trailing Zeroes

## Problem Statement
The problem requires finding the number of trailing zeroes in the factorial of a given integer `n`. The factorial of a number `n` (denoted as `n!`) is the product of all positive integers less than or equal to `n`. A trailing zero is a zero at the end of the number. For example, the factorial of 5 is `5! = 120`, which has one trailing zero. The input `n` will be an integer between 1 and 10^4.

## Approach
The algorithm is based on the fact that a trailing zero is created by a pair of 2 and 5 in the prime factorization of the factorial. Since there are usually more factors of 2 than 5, we just need to count the number of factors of 5. This is done by dividing `n` by powers of 5 and summing up the results.

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
        while (n > 0) {
            // for each power of 5, add the count to the result
            count += n / 5;
            // move to the next power of 5
            n /= 5;
        }
        return count;
    }
};
```

## Test Cases
```
Input: n = 5
Output: 1
Input: n = 10
Output: 2
```

## Key Takeaways
- The number of trailing zeroes in `n!` is determined by the number of factors of 5 in the prime factorization of `n!`.
- We can calculate this by dividing `n` by powers of 5 and summing up the results.
- The time complexity is O(log n) because we are dividing `n` by 5 in each iteration.