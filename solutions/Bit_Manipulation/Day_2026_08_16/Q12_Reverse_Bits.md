# Reverse Bits

## Problem Statement
Reverse the bits of a given 32-bit unsigned integer. The function should take an unsigned integer as input and return the reversed bits as an unsigned integer. For example, if the input is 43261596 (which is 00000010100101000001111010011100 in binary), the output should be 964176192 (which is 00111001011110000010100101000000 in binary). The input integer is guaranteed to be a 32-bit unsigned integer.

## Approach
The algorithm uses bitwise operations to reverse the bits of the input integer. It iterates over each bit in the integer, checks if the bit is set, and sets the corresponding bit in the result. The approach involves shifting the bits to the left and right to achieve the reversal.

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
        // Check if the current bit is set
        result = (result << 1) | (n & 1);
        // Right shift the input number
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
- The bitwise left shift operator `<<` shifts the bits of the number to the left and fills 0 on voids left as a result.
- The bitwise right shift operator `>>` shifts the bits of the number to the right and fills 0 on voids left as a result.
- The bitwise AND operator `&` compares each bit of the first operand to the corresponding bit of the second operand. If both bits are 1, the corresponding result bit is set to 1. Otherwise, the corresponding result bit is set to 0.