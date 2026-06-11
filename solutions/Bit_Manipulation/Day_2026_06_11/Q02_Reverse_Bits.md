# Reverse Bits

## Problem Statement
The problem requires writing a function that takes an unsigned 32-bit integer as input and returns the integer with its bits reversed. The function should be able to handle large integers and optimize for performance. For example, given the integer 43261596 (represented as 00000010100101000001111010011100 in binary), the function should return 964176192 (represented as 00111001011100000010100101000000 in binary). The input integer will be in the range [0, 2^32 - 1].

## Approach
The algorithm uses bitwise operations to reverse the bits of the input integer. It iterates over each bit in the integer, checks if the bit is set, and if so, sets the corresponding bit in the result. The approach relies on the properties of bitwise shift operators to achieve this.

## Complexity
- Time: O(1)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        uint32_t result = 0;
        for (int i = 0; i < 32; i++) {
            // Check if the current bit is set in the input integer
            if (n & 1) {
                // If set, set the corresponding bit in the result
                result |= 1 << (31 - i);
            }
            // Right shift the input integer to move to the next bit
            n >>= 1;
        }
        return result;
    }
};
```

## Test Cases
```
Input: 43261596
Output: 964176192
Input: 4294967293
Output: 3221225471
```

## Key Takeaways
- Use bitwise shift operators to iterate over each bit in the integer.
- Employ bitwise AND operator to check if a bit is set in the input integer.
- Utilize bitwise OR operator to set the corresponding bit in the result.