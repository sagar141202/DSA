# Reverse Bits

## Problem Statement
The problem requires reversing the bits of a given 32-bit unsigned integer. The integer is represented in binary form, and the task is to reverse the order of its bits. For example, if the input is 43261596 (represented as 00000010100101000001111010011100 in binary), the output should be 964176192 (represented as 00111001011110000010100100000000 in binary). The constraints are that the input is a 32-bit unsigned integer, and the output should also be a 32-bit unsigned integer.

## Approach
The approach to solve this problem is to use bit manipulation techniques. We can iterate through each bit of the input number, and for each bit, we check if it is 1 or 0. If it is 1, we set the corresponding bit in the result from the right (i.e., the least significant bit). We can use the left shift operator to move the bits to the left and the bitwise OR operator to set the bits in the result.

## Complexity
- Time: O(1)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        uint32_t result = 0;
        for (int i = 0; i < 32; i++) {
            // check the least significant bit of n
            result = (result << 1) | (n & 1);
            // right shift n by 1 bit
            n = n >> 1;
        }
        return result;
    }
};
```

## Test Cases
```
Input: 43261596
Output: 964176192
```

## Key Takeaways
- The problem can be solved using bit manipulation techniques.
- We can use the left shift operator to move the bits to the left and the bitwise OR operator to set the bits in the result.
- The time complexity of the solution is O(1) because we are iterating through a fixed number of bits (32 bits).