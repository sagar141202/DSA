# Reverse Bits

## Problem Statement
Reverse the bits of a given 32-bit unsigned integer. The function should take an unsigned integer as input and return the reversed bits as an unsigned integer. For example, if the input is 43261596 (which is 00000010100101000001111010011100 in binary), the output should be 964176192 (which is 11101011010000100010100100000000 in binary). The input is guaranteed to be a 32-bit unsigned integer.

## Approach
The approach is to iterate over each bit in the input number, and append it to the result. We can use bitwise operations to achieve this. We will use a loop to iterate over each bit, and in each iteration, we will left shift the result and add the current bit to it.

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
        // left shift the result by 1 bit and add the current bit to it
        result = (result << 1) | (n & 1);
        // right shift the input number by 1 bit
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
- Use bitwise operations to reverse the bits of a number.
- Iterate over each bit in the input number using a loop.
- Use left shift and right shift operators to manipulate the bits.