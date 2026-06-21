# Reverse Bits

## Problem Statement
Reverse the bits of a given 32-bit unsigned integer. The function should take an unsigned integer as input and return the unsigned integer with its bits reversed. For example, the binary representation of the number 43261596 is 00000000000000000000000010101011, and the binary representation of the reversed number is 11010100000000000000000000000000, which is 964176192 in decimal. The input is guaranteed to be a 32-bit unsigned integer.

## Approach
The approach involves using bitwise operations to reverse the bits of the input number. We can achieve this by shifting the bits to the left and right and using bitwise OR operation to combine the bits. The algorithm iterates 32 times to reverse all the bits.

## Complexity
- Time: O(1)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

unsigned int reverseBits(unsigned int n) {
    unsigned int result = 0;
    for (int i = 0; i < 32; i++) {
        // shift the current bit to the left and add it to the result
        result = (result << 1) | (n & 1);
        // shift the input number to the right
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
- Use bitwise operations to manipulate individual bits of a number.
- The left shift operator (<<) shifts the bits to the left and fills the vacant positions with zeros.
- The right shift operator (>>) shifts the bits to the right and fills the vacant positions with zeros for unsigned integers.