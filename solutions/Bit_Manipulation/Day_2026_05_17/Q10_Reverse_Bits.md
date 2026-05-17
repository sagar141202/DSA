# Reverse Bits

## Problem Statement
Reverse the bits of a given 32-bit unsigned integer. The function should take an unsigned integer as input and return the reversed bits as an unsigned integer. For example, the binary representation of the decimal number 432 is 110110000, and reversing the bits gives 000011011. The function should handle integers with leading zeros and should not use any built-in functions to reverse the bits. The input is guaranteed to be a 32-bit unsigned integer.

## Approach
We can solve this problem by using bitwise operations to extract each bit from the input number and append it to the result. We start from the least significant bit and move towards the most significant bit. The algorithm involves shifting the input number to the right to extract each bit and shifting the result to the left to append the extracted bit.

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
        // extract the least significant bit from n
        result = (result << 1) | (n & 1);
        // remove the least significant bit from n
        n = n >> 1;
    }
    return result;
}
```

## Test Cases
```
Input: 432
Output: 964176192
```

## Key Takeaways
- Use bitwise operations to extract and append bits.
- Shift the input number to the right to extract each bit.
- Shift the result to the left to append the extracted bit.
- The time complexity is O(1) because we are performing a constant number of operations (32 iterations).