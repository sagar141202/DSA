# Bitwise AND of Numbers Range

## Problem Statement
Given a range of numbers from `left` to `right` (inclusive), find the bitwise AND of all numbers in this range. The range is defined by two integers, `left` and `right`, where `1 <= left <= right <= 2^31 - 1`. The bitwise AND operation compares each bit of the first operand to the corresponding bit of the second operand. If both bits are 1, the corresponding result bit is set to 1. Otherwise, the corresponding result bit is set to 0.

## Approach
The algorithm uses the property that the bitwise AND of a range of numbers can be calculated by finding the common prefix of the binary representations of the two numbers. This is because the bits that differ between the two numbers will result in 0 when performing a bitwise AND operation.

## Complexity
- Time: O(log n)
- Space: O(1)

## C++ Solution
```cpp
class Solution {
public:
    int rangeBitwiseAnd(int left, int right) {
        // Calculate the number of common prefix bits
        int shift = 0;
        while (left < right) {
            // Right shift both numbers by 1 bit
            left >>= 1;
            right >>= 1;
            shift++;
        }
        
        // Restore the common prefix bits
        return left << shift;
    }
};
```

## Test Cases
```
Input: left = 5, right = 7
Output: 4
Input: left = 2, right = 3
Output: 2
```

## Key Takeaways
- The bitwise AND operation can be used to find the common prefix of binary representations of two numbers.
- Right shifting both numbers by 1 bit effectively removes the least significant bit, allowing us to find the common prefix.
- The number of common prefix bits can be restored by left shifting the result by the number of bits shifted.