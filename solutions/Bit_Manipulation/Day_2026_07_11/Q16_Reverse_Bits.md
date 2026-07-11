# Reverse Bits

## Problem Statement
Reverse the bits of a given 32-bit unsigned integer. The function should take an unsigned integer as input and return the reversed bits as an unsigned integer. For example, the reverse of 00000010100101000001111010011100 is 00111001011100001010010100000000. The input is guaranteed to be a 32-bit unsigned integer, so it will be in the range [0, 2^32 - 1]. The function should be efficient and should not use any built-in functions to reverse the bits.

## Approach
The algorithm uses bitwise operations to reverse the bits of the input integer. It iterates over each bit in the integer, checks if the bit is set, and if so, sets the corresponding bit in the result. The approach involves shifting the bits to the left and right to achieve the reversal.

## Complexity
- Time: O(1)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

unsigned int reverseBits(unsigned int n) {
    unsigned int result = 0;
    for (int i = 0; i < 32; i++) {
        // Check if the current bit is set
        if (n & 1) {
            // Set the corresponding bit in the result
            result |= 1 << (31 - i);
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
- Use bitwise operations to manipulate individual bits in an integer.
- Iterate over each bit in the input integer to reverse the bits.
- Use shifting operations to move bits to the left and right.