# Sum of Two Integers

## Problem Statement
The problem requires finding the sum of two integers without using the arithmetic operators + and -. The function should take two integers as input and return their sum. The integers can be positive, negative, or zero. For example, given the integers 3 and 5, the function should return 8. Given the integers -2 and 4, the function should return 2.

## Approach
The approach is to use bitwise operators to add the two integers. This can be achieved by using the XOR operator (^) to add the bits of the two numbers and the AND operator (&) with left shift to handle the carry.

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
        if (b == 0)
            return a;
        
        // Calculate the sum of a and b without considering the carry
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
Input: a = 3, b = 5
Output: 8
Input: a = -2, b = 4
Output: 2
```

## Key Takeaways
- Use bitwise operators to add two integers without using arithmetic operators + and -.
- The XOR operator (^) is used to add the bits of the two numbers.
- The AND operator (&) with left shift is used to handle the carry.