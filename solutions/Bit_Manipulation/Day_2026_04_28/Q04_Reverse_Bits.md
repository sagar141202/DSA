# Reverse Bits

## Problem Statement
Reverse the bits of a given 32-bit unsigned integer. The input integer will be in the range [0, 2^32 - 1]. The function should return the decimal value of the reversed bits. For example, if the input is 43261596 (represented as 00000010100101000001111010011100 in binary), the output will be 964176192 (represented as 00111001011101000010100100000000 in binary).

## Approach
The approach is to use bit manipulation to reverse the bits of the input integer. This can be done by using bitwise shift operators to move the bits to their correct positions. We will iterate over each bit in the input integer, shift it to its correct position, and then combine it with the result.

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
        // shift the current bit to its correct position
        result = (result << 1) | (n & 1);
        // remove the least significant bit from the input number
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
Output: 3221225471
```

## Key Takeaways
- Bit manipulation can be used to efficiently reverse the bits of an integer.
- The use of bitwise shift operators allows us to move bits to their correct positions.
- The time complexity of this solution is constant because we are only iterating over a fixed number of bits (32).