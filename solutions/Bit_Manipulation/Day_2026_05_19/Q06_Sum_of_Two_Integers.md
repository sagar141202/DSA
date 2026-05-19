# Sum of Two Integers

## Problem Statement
The problem requires finding the sum of two integers without using the arithmetic operators `+` and `-`. The function should take two integers `a` and `b` as input and return their sum. The integers can be positive, negative, or zero. For example, given `a = 1` and `b = 2`, the function should return `3`. Given `a = -2` and `b = 3`, the function should return `1`.

## Approach
The approach involves using bit manipulation to add the two integers. This can be achieved by performing bitwise XOR and left shift operations. The XOR operation is used to add the bits without considering the carry, while the left shift operation is used to consider the carry.

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
        // If b is 0, return a (base case)
        if (b == 0) return a;
        
        // Calculate the sum without considering the carry
        int sum = a ^ b;
        
        // Calculate the carry
        int carry = (a & b) << 1;
        
        // Recursively call the function with the sum and carry
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
- Bit manipulation can be used to perform arithmetic operations without using the arithmetic operators.
- The XOR operation can be used to add bits without considering the carry.
- The left shift operation can be used to consider the carry in bit manipulation.