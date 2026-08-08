# Reverse Bits

## Problem Statement
The problem requires writing a function that takes an unsigned 32-bit integer as input and returns the integer with its bits reversed. For example, if the input is 43261596 (which is 00000010100101000001111010011100 in binary), the function should return 964176192 (which is 00111001011100000010100101000000 in binary). The function should be able to handle integers of up to 32 bits.

## Approach
The algorithm involves using bitwise operations to reverse the bits of the input integer. We can achieve this by shifting the bits to the left and right, and using bitwise OR operation to combine the reversed bits. The process is repeated 32 times to cover all bits in the integer.

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
- The algorithm involves shifting and bitwise OR operations to achieve the reversal.
- The solution has a time complexity of O(1) and space complexity of O(1) as it only involves a fixed number of operations.