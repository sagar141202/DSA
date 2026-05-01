# Reverse Bits

## Problem Statement
The problem requires reversing the bits of a given 32-bit unsigned integer. The input is an unsigned integer, and the output should be the integer with its bits reversed. For example, if the input is 43261596 (represented as 00000010100101000001111010011100 in binary), the output should be 964176192 (represented as 00111001011100000010100101000000 in binary). The function should handle integers with leading zeros and should not use any built-in functions to reverse the bits.

## Approach
The algorithm uses bit manipulation to reverse the bits of the input integer. It iterates over each bit in the integer, checks if the bit is set, and if so, sets the corresponding bit in the result integer. The approach utilizes bitwise shift operators to achieve this.

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
        if (n & 1) {
            // Set the corresponding bit in the result
            result |= (1 << (31 - i));
        }
        // Right shift the input to move to the next bit
        n >>= 1;
    }
    return result;
}
```

## Test Cases
```
Input: 43261596
Output: 964176192
```

## Key Takeaways
- Bit manipulation can be used to reverse the bits of an integer without using built-in functions.
- The approach involves iterating over each bit in the integer and setting the corresponding bit in the result integer using bitwise shift operators.
- The time complexity is O(1) because the number of bits in an integer is constant (32 bits for a 32-bit unsigned integer).