# Factorial Trailing Zeroes

## Problem Statement
The problem requires finding the number of trailing zeroes in the factorial of a given integer `n`. The factorial of `n`, denoted as `n!`, is the product of all positive integers less than or equal to `n`. A trailing zero is a zero that appears at the end of the number. For example, `5! = 120` has one trailing zero, and `10! = 3628800` has two trailing zeroes. The input `n` is a positive integer, and the output is the number of trailing zeroes in `n!`. The constraints are `1 <= n <= 10^4`.

## Approach
The approach is based on the fact that trailing zeroes are created by the multiplication of 2 and 5. Since there are more factors of 2 than 5 in the factorial, we only need to count the factors of 5. We will use a loop to count the factors of 5 in `n!`.

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
        // loop to count the factors of 5
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
Input: n = 5
Output: 1
Input: n = 10
Output: 2
Input: n = 25
Output: 6
```

## Key Takeaways
- The number of trailing zeroes in `n!` is determined by the number of factors of 5 in `n!`.
- The loop iterates `log(n)` times, making the time complexity O(log n).
- The space complexity is O(1) because we only use a constant amount of space to store the count.