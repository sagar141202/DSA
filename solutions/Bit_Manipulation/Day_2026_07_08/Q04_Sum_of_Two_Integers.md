# Sum of Two Integers

## Problem Statement
Given two integers `a` and `b`, find the sum of these two integers without using the `+` operator. The integers can be negative or positive, and the range of the integers is within the range of a 32-bit signed integer. For example, given `a = 1` and `b = 2`, the function should return `3`. Given `a = -2` and `b = 3`, the function should return `1`.

## Approach
The algorithm uses bit manipulation to achieve the sum of two integers. It utilizes the properties of bitwise XOR and left shift operators to calculate the sum. The XOR operator is used to calculate the sum of two numbers without considering the carry, while the left shift operator is used to calculate the carry.

## Complexity
- Time: O(log(max(a, b)))
- Space: O(1)

## C++ Solution
```cpp
class Solution {
public:
    int getSum(int a, int b) {
        // If b is 0, return a as there is no carry
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
Input: a = 1, b = 2
Output: 3
Input: a = -2, b = 3
Output: 1
```

## Key Takeaways
- Bit manipulation can be used to solve problems that involve binary operations.
- The XOR operator (`^`) can be used to calculate the sum of two numbers without considering the carry.
- The left shift operator (`<<`) can be used to calculate the carry by shifting the bits of the number to the left.