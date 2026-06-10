# Reverse Bits

## Problem Statement
Reverse the bits of a given 32-bit unsigned integer. The input integer will be in the range [0, 2^32 - 1] and the output should also be in the same range. For example, if the input is 43261596 (which is 00000010100101000001111010011100 in binary), the output should be 964176192 (which is 00111001011110000010100100000000 in binary).

## Approach
The approach is to use bit manipulation to reverse the bits of the input number. We will iterate through each bit of the input number from right to left, and append it to the result. This can be achieved by using bitwise shift operators to move the bits to their correct positions.

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
        // append the least significant bit of n to result
        result = (result << 1) | (n & 1);
        // remove the least significant bit of n
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
- Use bitwise shift operators to move bits to their correct positions.
- Iterate through each bit of the input number from right to left to reverse the bits.
- The time complexity is O(1) because we are iterating a fixed number of times (32 times for a 32-bit integer).