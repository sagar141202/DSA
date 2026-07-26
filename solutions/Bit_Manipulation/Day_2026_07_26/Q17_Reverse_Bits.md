# Reverse Bits

## Problem Statement
Reverse the bits of a given 32-bit unsigned integer. The input integer will be in the range [0, 2^32 - 1]. The output should also be in the same range. For example, the binary representation of the decimal number 432 is 110110000, and the binary representation of the decimal number 964176192 is 11100100000000000000000000000000. The function should reverse the bits of the input integer and return the resulting decimal number.

## Approach
The algorithm involves using bitwise operations to reverse the bits of the input integer. We can achieve this by shifting the bits to the right and left, and using bitwise OR operation to store the result. The time complexity of this approach is O(1) because we are performing a constant number of operations.

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
            // shift the bits of the result to the left
            result <<= 1;
            // check the least significant bit of n
            result |= n & 1;
            // shift the bits of n to the right
            n >>= 1;
        }
        return result;
    }
};
```

## Test Cases
```
Input: 432
Output: 964176192
Input: 4294967293
Output: 3221225471
```

## Key Takeaways
- Use bitwise operations to reverse the bits of an integer.
- Shift the bits to the left and right using the << and >> operators.
- Use the bitwise OR operator to store the result.