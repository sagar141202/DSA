# Reverse Bits

## Problem Statement
The problem requires reversing the bits of a given 32-bit unsigned integer. The integer is represented in binary form, and the goal is to reverse the order of its bits. For example, if the input is 43261596 (represented as 00000010100101000001111010011100 in binary), the output should be 964176192 (represented as 00111001011110000010100100000000 in binary). The input integer will be in the range [0, 2^32 - 1], and the output should also be in the same range.

## Approach
The approach involves using bitwise operations to reverse the bits of the input integer. This can be achieved by iterating over each bit of the input integer, checking if it's set, and setting the corresponding bit in the result integer.

## Complexity
- Time: O(1)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

uint32_t reverseBits(uint32_t n) {
    uint32_t result = 0;
    for (int i = 0; i < 32; i++) {
        // Check if the current bit is set in the input integer
        result = (result << 1) | (n & 1);
        // Right shift the input integer to move to the next bit
        n = n >> 1;
    }
    return result;
}
```

## Test Cases
```
Input: 43261596
Output: 964176192
Input: 4294967293
Output: 4294967293
```

## Key Takeaways
- Use bitwise operations to reverse the bits of an integer.
- Iterate over each bit of the input integer to achieve this.
- The time complexity is constant (O(1)) because the number of bits in an integer is fixed.