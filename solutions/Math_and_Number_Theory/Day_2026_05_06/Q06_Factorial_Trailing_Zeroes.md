# Factorial Trailing Zeroes

## Problem Statement
The problem requires finding the number of trailing zeroes in the factorial of a given number `n`. The factorial of a number `n` (denoted as `n!`) is the product of all positive integers less than or equal to `n`. A trailing zero is a zero that appears at the end of the number. For example, the factorial of 5 is `5! = 120`, which has one trailing zero. The constraints are `1 <= n <= 10^4`.

## Approach
The algorithm uses the concept of prime factorization to count the number of trailing zeroes. It calculates the number of factors of 5 in the factorial, as each trailing zero is created by a factor of 2 and a factor of 5. The intuition is to count the factors of 5, as they are less frequent than factors of 2.

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
Input: n = 5
Output: 1
Input: n = 10
Output: 2
```

## Key Takeaways
- The number of trailing zeroes in `n!` is determined by the number of factors of 5.
- The algorithm has a time complexity of O(log n) due to the division operation in the while loop.
- The space complexity is O(1) as it only uses a constant amount of space.