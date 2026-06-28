# Sum of Two Integers

## Problem Statement
Given two integers a and b, find the sum of the two integers without using the + operator. The integers can be positive, negative, or zero. The solution should handle overflow cases. For example, if a = 1 and b = 2, the output should be 3. If a = -1 and b = 1, the output should be 0.

## Approach
The approach is to use bitwise operators to add the two integers. We can use the XOR operator (^) to add the bits of the two integers without considering the carry. Then, we can use the AND operator (&) to find the carry bits. We can repeat this process until there is no carry left.

## Complexity
- Time: O(log max(a, b))
- Space: O(1)

## C++ Solution
```cpp
class Solution {
public:
    int getSum(int a, int b) {
        // if b is 0, return a
        if (b == 0) return a;
        // calculate the sum of a and b without considering the carry
        int sum = a ^ b;
        // calculate the carry
        int carry = (a & b) << 1;
        // repeat the process until there is no carry left
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
Input: a = -2, b = 3
Output: 1
```

## Key Takeaways
- The XOR operator (^) can be used to add the bits of two integers without considering the carry.
- The AND operator (&) can be used to find the carry bits.
- The left shift operator (<<) can be used to shift the carry bits to the left.