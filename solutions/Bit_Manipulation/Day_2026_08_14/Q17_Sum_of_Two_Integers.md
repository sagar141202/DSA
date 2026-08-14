# Sum of Two Integers

## Problem Statement
Given two integers `a` and `b`, return the sum of the two integers without using the `+` operator. The integers can be positive, negative, or zero. The solution should work for all possible integer values.

## Approach
We can use bitwise operators to achieve this. The XOR operator (`^`) can be used to add two numbers without considering the carry, and the AND operator (`&`) can be used to calculate the carry. We can then shift the carry to the left and repeat the process until there is no carry left.

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
        
        // Calculate the sum without considering the carry
        int sum = a ^ b;
        
        // Calculate the carry
        int carry = (a & b) << 1;
        
        // Recursively call the function with the new sum and carry
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
- Bitwise operators can be used to perform arithmetic operations without using the standard operators.
- The XOR operator can be used to add two numbers without considering the carry.
- The AND operator can be used to calculate the carry in binary addition.