# Factorial Trailing Zeroes

## Problem Statement
The problem requires finding the number of trailing zeroes in the factorial of a given number `n`. The factorial of a number `n` (denoted as `n!`) is the product of all positive integers less than or equal to `n`. A trailing zero is a zero at the end of the number. For example, the factorial of 5 is `5! = 120`, which has one trailing zero. The input `n` is a positive integer, and the output should be the number of trailing zeroes in `n!`. The constraint is `1 <= n <= 10^4`.

## Approach
The algorithm is based on the fact that trailing zeroes in a factorial are caused by the multiplication of 2 and 5. Since there are usually more factors of 2 than 5, we count the factors of 5. We use a loop to count the factors of 5 in all numbers from 1 to `n`.

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
        // count the factors of 5
        while (n >= 5) {
            n /= 5;
            count += n;
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
- The number of trailing zeroes in `n!` is determined by the number of factors of 5 in all numbers from 1 to `n`.
- We can use a simple loop to count the factors of 5.
- The time complexity is O(log n) because we are dividing `n` by 5 in each iteration.