# Sum of Two Integers

## Problem Statement
The problem requires finding the sum of two integers without using the arithmetic operators + and -. The integers can be positive, negative, or zero. The solution should handle integer overflow and underflow. For example, given two integers a = 5 and b = 7, the function should return 12.

## Approach
The approach involves using bitwise operators to achieve the addition of two integers. This can be done by adding the bits of the two numbers from right to left, similar to the long addition method used in elementary school. The algorithm will use bitwise XOR to add the bits and bitwise AND with left shift to handle the carry.

## Complexity
- Time: O(log(max(a, b)))
- Space: O(1)

## C++ Solution
```cpp
class Solution {
public:
    int getSum(int a, int b) {
        // If b is 0, return a (base case)
        if (b == 0) return a;
        
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
Input: a = 5, b = 7
Output: 12
Input: a = -5, b = 7
Output: 2
Input: a = 5, b = -7
Output: -2
```

## Key Takeaways
- Bitwise XOR can be used to add two bits without considering the carry.
- Bitwise AND with left shift can be used to calculate the carry.
- Recursive approach can be used to handle the addition of two integers using bitwise operators.