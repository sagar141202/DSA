# Factorial Trailing Zeroes

## Problem Statement
The problem requires finding the number of trailing zeroes in the factorial of a given integer `n`. The factorial of a number `n` (denoted as `n!`) is the product of all positive integers less than or equal to `n`. A trailing zero is a zero at the end of the number. For example, the factorial of 5 is `5! = 120`, which has one trailing zero. The problem statement is to write a function that takes an integer `n` as input and returns the number of trailing zeroes in `n!`. The constraints are `1 <= n <= 10^4`.

## Approach
The algorithm is based on the fact that trailing zeroes are created by the product of 2 and 5. Since there are more factors of 2 than 5 in a factorial, we only need to count the number of factors of 5. We can count the factors of 5 by dividing `n` by powers of 5.

## Complexity
- Time: O(log(n))
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
Input: n = 10
Output: 2
```

## Key Takeaways
- The number of trailing zeroes in `n!` is determined by the number of factors of 5 in `n!`.
- We can count the factors of 5 by dividing `n` by powers of 5.
- The time complexity is O(log(n)) because we are dividing `n` by powers of 5 in each iteration.