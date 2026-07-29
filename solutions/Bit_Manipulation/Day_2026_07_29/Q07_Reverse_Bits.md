# Reverse Bits

## Problem Statement
Reverse the bits of a given 32-bit unsigned integer. The input integer will be represented as a binary string of 32 bits, with leading zeros if necessary. The output should also be an integer, represented as a binary string of 32 bits. For example, the input 43261596 (represented as 00000010100111000001111010011100 in binary) should be reversed to 964176192 (represented as 11101001110111100000011010000100 in binary). The constraints are 0 <= n <= 2^32 - 1.

## Approach
The algorithm involves iterating over each bit of the input integer from right to left and appending it to the result. This can be achieved by using bitwise shift operators to extract and append the bits. The process is repeated for all 32 bits of the input integer.

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
        // extract the least significant bit of n
        result = (result << 1) | (n & 1);
        // right shift n by 1 bit
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
- Bitwise shift operators can be used to extract and append bits.
- The process of reversing bits can be achieved in constant time complexity by iterating over the bits of the input integer.
- The space complexity is constant as it only involves a fixed number of variables.