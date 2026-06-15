# Sum of Two Integers

## Problem Statement
Given two integers `a` and `b`, find their sum without using the arithmetic operators `+` and `-`. The integers can be positive, negative, or zero, and the sum should be calculated using only bitwise operations. For example, if `a = 1` and `b = 2`, the function should return `3`, which is the sum of `a` and `b`.

## Approach
The algorithm uses bitwise XOR (`^`) to add the bits of `a` and `b` without considering the carry. Then, it uses bitwise AND (`&`) to calculate the carry. The process is repeated until there is no carry left. This approach ensures that the sum is calculated correctly using only bitwise operations.

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
        
        // Calculate the sum of a and b using XOR
        int sum = a ^ b;
        
        // Calculate the carry using AND and left shift
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
- Use bitwise XOR (`^`) to add the bits of two numbers without considering the carry.
- Use bitwise AND (`&`) and left shift (`<<`) to calculate the carry.
- Recursively repeat the process until there is no carry left to calculate the sum correctly.