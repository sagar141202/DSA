# Reverse Bits

## Problem Statement
The problem "Reverse Bits" involves reversing the order of bits in a given 32-bit unsigned integer. The function should take an unsigned integer as input and return the unsigned integer with its bits reversed. For example, the binary representation of the decimal number 432 is 110110000, and reversing the bits results in 000011011. The function should handle integers within the range of 0 to 2^32 - 1.

## Approach
The algorithm involves using bitwise operations to reverse the bits of the input integer. This can be achieved by shifting the bits to the left and right, and using bitwise OR operation to combine the reversed bits. The process is repeated until all bits are reversed.

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
Input: 432 (110110000)
Output: 964176192 (000011011)
Input: 4294967293 (11111111111111111111111111111111)
Output: 4294967293 (11111111111111111111111111111111)
```

## Key Takeaways
- The algorithm uses bitwise shift operators to reverse the bits of the input integer.
- The time complexity of the algorithm is O(1) because the number of operations is constant, regardless of the input size.
- The space complexity of the algorithm is O(1) because only a constant amount of space is used to store the result.