# Factorial Trailing Zeroes

## Problem Statement
The problem requires finding the number of trailing zeroes in the factorial of a given number `n`. The factorial of a number `n` (denoted as `n!`) is the product of all positive integers less than or equal to `n`. A trailing zero is a zero that appears at the end of the number. For example, the factorial of 5 is `5! = 120`, which has 1 trailing zero. The input `n` will be a non-negative integer, and the output should be the number of trailing zeroes in `n!`. The constraints are `0 <= n <= 10^5`.

## Approach
The algorithm is based on the fact that trailing zeroes are created by the product of 2 and 5. Since there are usually more factors of 2 than 5 in a factorial, we just need to count the number of factors of 5. We will use a loop to calculate the number of factors of 5 in `n!`.

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
        // calculate the number of factors of 5 in n!
        while (n >= 5) {
            count += n / 5;
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
- The number of trailing zeroes in `n!` is determined by the number of factors of 5 in `n!`.
- We can calculate the number of factors of 5 in `n!` by using a loop that divides `n` by 5 and adds the result to the count.
- The time complexity of this solution is O(log n) because we are dividing `n` by 5 in each iteration of the loop.