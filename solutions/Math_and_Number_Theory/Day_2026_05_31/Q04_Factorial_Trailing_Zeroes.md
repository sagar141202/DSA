# Factorial Trailing Zeroes

## Problem Statement
The problem requires finding the number of trailing zeroes in the factorial of a given number. The factorial of a number n, denoted as n!, is the product of all positive integers less than or equal to n. A trailing zero is a zero at the end of the number. For example, the factorial of 5 (5! = 120) has one trailing zero. Given a positive integer n, we need to find the number of trailing zeroes in n!. The input n will be in the range [1, 10^4] and the output will be the number of trailing zeroes in n!.

## Approach
The algorithm is based on the fact that a trailing zero is formed by a pair of 2 and 5. Since there are more factors of 2 than 5 in a factorial, we only need to count the number of factors of 5. We can use a loop to count the factors of 5 in n!.

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
```

## Key Takeaways
- The number of trailing zeroes in n! is determined by the number of factors of 5 in n!.
- We can use a loop to count the factors of 5 in n!.
- The time complexity of the solution is O(log n) because we are dividing n by 5 in each iteration of the loop.