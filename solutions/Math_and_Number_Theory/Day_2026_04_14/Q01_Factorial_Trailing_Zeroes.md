# Factorial Trailing Zeroes

## Problem Statement
The problem requires finding the number of trailing zeroes in the factorial of a given integer `n`. The factorial of a number `n` (denoted as `n!`) is the product of all positive integers less than or equal to `n`. A trailing zero is a zero at the end of the number. For example, the factorial of 5 is `5! = 5 * 4 * 3 * 2 * 1 = 120`, which has one trailing zero. The input `n` will be a non-negative integer, and the output should be the number of trailing zeroes in `n!`. The constraint is `0 <= n <= 10^5`.

## Approach
The approach is to count the number of factors of 5 in the factorial of `n`, as each trailing zero is created by a factor of 2 and a factor of 5. Since there are usually more factors of 2 than 5, we only need to count the factors of 5. This is done by dividing `n` by powers of 5 and summing up the results.

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
            n /= 5;
            count += n;
        }
        return count;
    }
};
```

## Test Cases
```
Input: 5
Output: 1
Input: 10
Output: 2
Input: 25
Output: 6
```

## Key Takeaways
- The number of trailing zeroes in `n!` is determined by the number of factors of 5 in the factorial.
- We can count the factors of 5 by dividing `n` by powers of 5 and summing up the results.
- The time complexity of this solution is O(log n) because we are dividing `n` by 5 in each iteration.