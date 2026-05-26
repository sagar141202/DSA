# Sum of Two Integers

## Problem Statement
Given two integers a and b, return the sum of the two integers without using the + operator. The integers can be positive, negative, or zero. For example, when a = 1 and b = 2, the output should be 3. When a = -1 and b = 1, the output should be 0.

## Approach
We will use bitwise operations to achieve this. The XOR operation (^) can be used to add two numbers without considering the carry. The AND operation (&) can be used to calculate the carry. We will repeat this process until there is no carry left.

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
        
        // Calculate the sum without considering the carry using XOR
        int sum = a ^ b;
        
        // Calculate the carry using AND and left shift
        int carry = (a & b) << 1;
        
        // Repeat the process until there is no carry left
        return getSum(sum, carry);
    }
};
```

## Test Cases
```
Input: a = 1, b = 2
Output: 3
Input: a = -1, b = 1
Output: 0
```

## Key Takeaways
- The XOR operation (^) can be used to add two numbers without considering the carry.
- The AND operation (&) can be used to calculate the carry.
- Bitwise operations can be used to solve problems that involve binary numbers.