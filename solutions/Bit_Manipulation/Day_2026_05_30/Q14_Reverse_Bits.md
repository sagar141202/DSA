# Reverse Bits

## Problem Statement
Reverse the bits of a given 32-bit unsigned integer. The input integer will be represented as a binary string of 32 bits, with leading zeros if necessary. The output should be the decimal representation of the reversed binary string. For example, given the input 43261596 (which is 00000010100101000001111010011100 in binary), the output should be 964176192 (which is 11101000001101101010000100000000 in binary). The input integer will be in the range [0, 2^32 - 1].

## Approach
The approach is to use bit manipulation to reverse the bits of the input integer. This can be achieved by shifting the bits of the input integer to the left and right, and using bitwise operations to construct the reversed binary string.

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
            // Shift the bits of the result to the left
            result = result << 1;
            // Check the least significant bit of the input integer
            result = result | (n & 1);
            // Shift the bits of the input integer to the right
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
Input: 4294967293
Output: 4294967293
```

## Key Takeaways
- Use bit manipulation to reverse the bits of the input integer.
- Shift the bits of the result to the left and the input integer to the right to construct the reversed binary string.
- Use bitwise operations to check the least significant bit of the input integer and construct the result.