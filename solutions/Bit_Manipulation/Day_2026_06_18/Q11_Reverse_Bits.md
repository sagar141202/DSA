# Reverse Bits

## Problem Statement
Reverse the bits of a given 32-bit unsigned integer. The function should take an unsigned integer as input and return the reversed bits as an unsigned integer. For example, if the input is 43261596 (representing 00000010100111000001111010011100 in binary), the output should be 964176192 (representing 00111010011100000011001100000000 in binary). The input integer is guaranteed to be a 32-bit unsigned integer.

## Approach
The algorithm involves iterating over each bit in the input integer, checking if it's set, and setting the corresponding bit in the result integer from right to left. This is done by shifting the bits to the left and using bitwise OR operation to set the bits in the result.

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
- Use bitwise shift operators to move bits to the left or right.
- Use bitwise AND operator (&) to check if a bit is set.
- Use bitwise OR operator (|) to set a bit in the result.