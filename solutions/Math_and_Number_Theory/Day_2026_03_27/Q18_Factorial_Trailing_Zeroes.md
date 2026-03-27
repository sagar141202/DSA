# Factorial Trailing Zeroes

## Problem Statement
The problem requires finding the number of trailing zeroes in the factorial of a given integer n. The factorial of a number is the product of all positive integers less than or equal to that number. A trailing zero is a zero at the end of the number. For example, the factorial of 5 (5! = 5*4*3*2*1 = 120) has one trailing zero. The input will be an integer n, where 1 <= n <= 10^4. The output will be the number of trailing zeroes in n!.

## Approach
To solve this problem, we can use the concept that a trailing zero is formed by a pair of 2 and 5. Since there are usually more factors of 2 than 5 in a factorial, we just need to count the number of factors of 5. We will iterate through all numbers from 1 to n and count the factors of 5.

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
Input: 5
Output: 1
Input: 10
Output: 2
```

## Key Takeaways
- The number of trailing zeroes in n! is determined by the number of factors of 5 in all numbers from 1 to n.
- We can use a loop to count the factors of 5 by dividing n by powers of 5.
- The time complexity is O(log n) because we are dividing n by powers of 5 in each iteration.