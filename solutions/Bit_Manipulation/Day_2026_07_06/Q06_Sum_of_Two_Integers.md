# Sum of Two Integers

## Problem Statement
Given two integers `a` and `b`, find the sum of the two integers without using the arithmetic operators `+` and `-`. The integers can be positive, negative, or zero. For example, if `a = 1` and `b = 2`, the function should return `3`. If `a = -1` and `b = 1`, the function should return `0`.

## Approach
The algorithm uses bit manipulation to achieve the sum of two integers. It works by performing bitwise XOR and left shift operations to add the two numbers. The XOR operation is used to add the bits without considering the carry, and the left shift operation is used to consider the carry.

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
        // if b is zero, return a
        if (b == 0) return a;
        // calculate the sum without considering the carry
        int sum = a ^ b;
        // calculate the carry
        int carry = (a & b) << 1;
        // recursively call the function with the sum and carry
        return getSum(sum, carry);
    }
};

// alternative iterative solution
class Solution {
public:
    int getSum(int a, int b) {
        while (b != 0) {
            // calculate the sum without considering the carry
            int sum = a ^ b;
            // calculate the carry
            int carry = (a & b) << 1;
            // update a and b
            a = sum;
            b = carry;
        }
        return a;
    }
};
```

## Test Cases
```
Input: a = 1, b = 2
Output: 3
Input: a = -1, b = 1
Output: 0
Input: a = 5, b = 7
Output: 12
```

## Key Takeaways
- The XOR operation can be used to add two bits without considering the carry.
- The left shift operation can be used to consider the carry.
- The algorithm can be implemented recursively or iteratively.