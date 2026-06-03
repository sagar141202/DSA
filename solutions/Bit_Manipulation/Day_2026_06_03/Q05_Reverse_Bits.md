# Reverse Bits

## Problem Statement
Reverse the bits of a given 32-bit unsigned integer. The function should take an unsigned integer as input and return the integer with its bits reversed. For example, if the input is 43261596 (which is 00000010100101000001111010011100 in binary), the output should be 964176192 (which is 00111001011110000010100101000000 in binary). The input integer is guaranteed to be a 32-bit unsigned integer.

## Approach
The algorithm uses bit manipulation to reverse the bits of the input integer. It iterates over each bit in the integer, checks if the bit is set, and if so, sets the corresponding bit in the result. The approach involves shifting the bits to the left and right to achieve the reversal.

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
        if (n & 1) {
            // Set the corresponding bit in the result
            result |= (1 << (31 - i));
        }
        // Right shift the input integer to move to the next bit
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
- The problem can be solved using bit manipulation techniques.
- The time complexity is O(1) because the number of operations is constant, regardless of the input size.
- The space complexity is O(1) because the space used does not grow with the size of the input.