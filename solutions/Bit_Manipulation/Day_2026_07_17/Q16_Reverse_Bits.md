# Reverse Bits

## Problem Statement
Reverse the bits of a given 32-bit unsigned integer. The function should take an unsigned integer as input and return the reversed bits as an unsigned integer. For example, if the input is 43261596 (represented as 00000010100111000001111010011100 in binary), the output should be 964176192 (represented as 00111001011110000011100100000000 in binary). The input integer is guaranteed to be a 32-bit unsigned integer.

## Approach
The approach involves using bitwise operations to reverse the bits of the input integer. We can achieve this by shifting the bits to the left and right, and using bitwise OR operation to combine the bits. The algorithm iterates 32 times to reverse all the bits.

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
        // shift the result to the left by 1 bit
        result <<= 1;
        // check the least significant bit of n
        result |= (n & 1);
        // shift n to the right by 1 bit
        n >>= 1;
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
- Use bitwise operations to manipulate individual bits of an integer.
- The left shift operator <<= shifts the bits to the left and fills 0 on voids left as a result.
- The right shift operator >>= shifts the bits to the right and fills 0 on voids left as a result.