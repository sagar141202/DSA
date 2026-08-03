# Sum of Two Integers

## Problem Statement
The problem requires finding the sum of two integers without using the arithmetic operators + and -. The function should take two integers as input and return their sum. The integers can be positive, negative, or zero. For example, given the integers 2 and 3, the function should return 5. Given the integers -2 and 3, the function should return 1.

## Approach
The approach is to use bitwise operators to add the two integers. This can be achieved by using the XOR operator (^) to add the bits of the two numbers and the AND operator (&) with left shift to handle the carry.

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
Input: a = 2, b = 3
Output: 5
Input: a = -2, b = 3
Output: 1
```

## Key Takeaways
- Bitwise operators can be used to perform arithmetic operations without using the arithmetic operators + and -.
- The XOR operator (^) can be used to add the bits of two numbers without considering the carry.
- The AND operator (&) with left shift can be used to handle the carry.