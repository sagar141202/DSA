# Reverse Bits

## Problem Statement
Reverse the bits of a given 32-bit unsigned integer. The function should take an unsigned integer as input and return the integer with its bits reversed. For example, if the input is 43261596 (which is 00000010100101000001111010011100 in binary), the output should be 964176192 (which is 00111001011110000010100101000000 in binary). The input integer is guaranteed to be a 32-bit unsigned integer.

## Approach
The approach is to use bit manipulation to reverse the bits of the input integer. We can achieve this by iterating over each bit of the input integer and appending it to the result. We will use bitwise shift operators to achieve this.

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
Input: 4294967293
Output: 3221225471
```

## Key Takeaways
- Use bitwise shift operators to manipulate bits.
- Iterate over each bit of the input integer to reverse its bits.
- Use bitwise AND operator to get the least significant bit of the input integer.