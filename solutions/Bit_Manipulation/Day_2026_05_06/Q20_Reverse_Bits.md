# Reverse Bits

## Problem Statement
The problem requires reversing the bits of a given 32-bit unsigned integer. The integer is represented as a sequence of 32 bits (0s and 1s). The task is to reverse the order of these bits, i.e., the bit at position 0 should be moved to position 31, the bit at position 1 should be moved to position 30, and so on. The function should take an unsigned integer as input and return the reversed integer. For example, the reverse of 00000000000000000000000000001011 is 11010000000000000000000000000000.

## Approach
The approach involves using bitwise operations to extract and reverse the bits of the input integer. We can use a loop to iterate through each bit of the integer, extract the bit, and append it to the result.

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
        // extract the least significant bit of n
        result = (result << 1) | (n & 1);
        // right shift n by 1 bit
        n = n >> 1;
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
- Use bitwise operations to manipulate bits of an integer.
- The expression `n & 1` extracts the least significant bit of `n`.
- The expression `n >> 1` right shifts the bits of `n` by 1 position.