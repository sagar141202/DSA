# Factorial Trailing Zeroes

## Problem Statement
The problem requires finding the number of trailing zeroes in the factorial of a given number `n`. The factorial of a number `n` (denoted as `n!`) is the product of all positive integers less than or equal to `n`. A trailing zero is a zero at the end of the number. The problem constraints are `1 <= n <= 10^4`. For example, the factorial of 5 is `5! = 120`, which has one trailing zero.

## Approach
The approach involves counting the number of factors of 5 in the prime factorization of `n!`, as each trailing zero is a result of a factor of 2 and a factor of 5. Since there are usually more factors of 2 than 5, we only need to count the factors of 5.

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
        // count factors of 5
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
Input: 25
Output: 6
```

## Key Takeaways
- The number of trailing zeroes in `n!` is determined by the number of factors of 5 in the prime factorization of `n!`.
- We can count the factors of 5 by dividing `n` by powers of 5 and adding up the results.
- This solution has a time complexity of O(log n) because we are dividing `n` by a constant factor (5) in each iteration.