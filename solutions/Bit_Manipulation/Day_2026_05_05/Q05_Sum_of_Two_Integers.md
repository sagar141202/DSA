# Sum of Two Integers

## Problem Statement
The problem requires finding the sum of two integers without using the arithmetic operators + and -. The function should take two integers as input and return their sum. The integers can be positive, negative, or zero. For example, given the integers 3 and 5, the function should return 8.

## Approach
The approach to solve this problem is to use bitwise operators to add the two integers. We can use the XOR operator (^) to find the sum of two numbers without considering the carry, and the AND operator (&) to find the carry. Then, we can use the left shift operator (<<) to shift the carry to the left and add it to the sum.

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
        
        // Calculate the sum without considering the carry using XOR
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
Input: a = 3, b = 5
Output: 8
Input: a = -3, b = 5
Output: 2
Input: a = 0, b = 0
Output: 0
```

## Key Takeaways
- Bitwise operators can be used to perform arithmetic operations without using the traditional arithmetic operators.
- The XOR operator (^) can be used to find the sum of two numbers without considering the carry.
- The AND operator (&) and left shift operator (<<) can be used to find and add the carry to the sum.