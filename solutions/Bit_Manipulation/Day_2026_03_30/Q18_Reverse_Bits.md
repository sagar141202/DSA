# Reverse Bits

## Problem Statement
The problem requires writing a function that takes an unsigned 32-bit integer as input and returns the integer with its bits reversed. For example, if the input is 43261596 (represented as 00000010100101000001111010011100 in binary), the output should be 964176192 (represented as 00111001011110000010100100000000 in binary). The function should be able to handle integers of any size up to 32 bits.

## Approach
The algorithm involves using bitwise operations to reverse the bits of the input integer. This can be achieved by iterating over each bit in the integer, appending it to the result, and then shifting the result to the left to make space for the next bit. The process continues until all 32 bits have been reversed.

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
        // Append the least significant bit of n to result
        result = (result << 1) | (n & 1);
        // Right shift n by 1 bit
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
- The function uses bitwise operations to reverse the bits of the input integer.
- The time complexity is O(1) because the number of operations is constant, regardless of the size of the input.
- The space complexity is O(1) because the function only uses a constant amount of space to store the result and temporary variables.