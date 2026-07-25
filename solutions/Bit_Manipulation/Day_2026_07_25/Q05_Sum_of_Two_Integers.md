# Sum of Two Integers

## Problem Statement
The problem requires finding the sum of two integers without using the arithmetic operators + and -. The function should take two integers as input and return their sum. The integers can be positive, negative, or zero. For example, given the integers 5 and 7, the function should return 12.

## Approach
The approach is to use bitwise operators to add the two integers. We can use the XOR operator (^) to add the bits of the two integers without considering the carry, and the AND operator (&) to calculate the carry. We can then shift the carry to the left by one bit and repeat the process until there is no carry left.

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
        
        // Calculate the sum without considering the carry
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
Input: a = 5, b = 7
Output: 12
Input: a = -5, b = 7
Output: 2
Input: a = 0, b = 0
Output: 0
```

## Key Takeaways
- The XOR operator (^) can be used to add the bits of two integers without considering the carry.
- The AND operator (&) can be used to calculate the carry.
- The process of calculating the sum and carry can be repeated until there is no carry left, at which point the sum is the final result.