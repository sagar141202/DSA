# Reverse Bits

## Problem Statement
Reverse the bits of a given 32-bit unsigned integer. The input integer will be represented as a binary string of 32 bits, with leading zeros if necessary. The output should also be a binary string of 32 bits. For example, the input "00000000000000000000000000001011" should be reversed to "11010000000000000000000000000000". The input will always be a valid 32-bit unsigned integer.

## Approach
The approach to solve this problem is to use bit manipulation to reverse the bits of the input integer. We can achieve this by shifting the bits to the left and right and using bitwise operators to construct the reversed binary string.

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
        // shift the current result to the left by 1 bit
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
Output: 3221225471
```

## Key Takeaways
- Bit manipulation can be used to reverse the bits of an integer.
- The left shift operator (<<) can be used to shift the bits to the left, and the right shift operator (>>) can be used to shift the bits to the right.
- The bitwise OR operator (|) can be used to construct the reversed binary string.