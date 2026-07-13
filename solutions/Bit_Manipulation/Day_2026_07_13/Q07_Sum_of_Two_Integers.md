# Sum of Two Integers

## Problem Statement
The problem requires finding the sum of two integers without using the arithmetic operators `+` and `-`. The function should take two integers as input and return their sum. The integers can be positive, negative, or zero. For example, given `a = 1` and `b = 2`, the function should return `3`. Given `a = -2` and `b = 3`, the function should return `1`.

## Approach
The approach is to use bitwise operators to add the two integers. We can use the XOR operator (`^`) to add the bits of the two numbers without considering the carry. Then, we can use the AND operator (`&`) to find the carry bits. We can then shift the carry bits to the left by one position and add them to the result.

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
        // If b is zero, the sum is a
        if (b == 0) return a;
        
        // Calculate the sum of a and b without considering the carry
        int sum = a ^ b;
        
        // Calculate the carry bits
        int carry = (a & b) << 1;
        
        // Recursively add the carry to the sum
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
- We can use bitwise operators to add two integers without using arithmetic operators.
- The XOR operator (`^`) can be used to add the bits of two numbers without considering the carry.
- The AND operator (`&`) can be used to find the carry bits, and shifting the carry bits to the left by one position can be used to add them to the result.