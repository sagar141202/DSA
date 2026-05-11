# Factorial Trailing Zeroes

## Problem Statement
The problem requires finding the number of trailing zeroes in the factorial of a given number `n`. The factorial of a number `n` (denoted as `n!`) is the product of all positive integers less than or equal to `n`. A trailing zero is a zero at the end of the number. For example, the factorial of 5 is `5! = 120`, which has one trailing zero. The constraints are `1 <= n <= 10^4`.

## Approach
The algorithm counts the number of factors of 5 in the factorial, as each trailing zero is formed by a factor of 2 and a factor of 5, and there are usually more factors of 2 than 5. We use a loop to count the factors of 5.

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
            count += n / 5;
            n /= 5;
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
```

## Key Takeaways
- The number of trailing zeroes is determined by the number of factors of 5 in the factorial.
- We use a while loop to count the factors of 5, dividing `n` by 5 in each iteration.
- The time complexity is O(log n) because we divide `n` by 5 in each iteration, effectively reducing the problem size logarithmically.