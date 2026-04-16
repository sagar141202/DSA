# Sum of Two Integers

## Problem Statement
Given two integers `a` and `b`, find their sum without using the arithmetic operators `+` and `-`. The integers can be positive, negative, or zero. For example, if `a = 1` and `b = 2`, the function should return `3`, and if `a = -2` and `b = 3`, the function should return `1`. The function should handle integer overflow.

## Approach
The approach is to use bitwise operators to add the two integers. We will use the XOR operator (`^`) to add the bits of `a` and `b` without considering the carry, and the AND operator (`&`) to calculate the carry. Then, we will shift the carry to the left by one bit and repeat the process until there is no carry left.

## Complexity
- Time: O(log(max(a, b)))
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int getSum(int a, int b) {
        // If b is 0, return a
        if (b == 0) return a;
        
        // Calculate the sum of a and b without considering the carry
        int sum = a ^ b;
        
        // Calculate the carry
        int carry = (a & b) << 1;
        
        // Repeat the process until there is no carry left
        return getSum(sum, carry);
    }
};
```

## Test Cases
```
Input: a = 1, b = 2
Output: 3
Input: a = -2, b = 3
Output: 1
```

## Key Takeaways
- Use bitwise operators to add two integers without using arithmetic operators.
- The XOR operator (`^`) can be used to add the bits of two numbers without considering the carry.
- The AND operator (`&`) can be used to calculate the carry.