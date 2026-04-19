# Reverse Bits

## Problem Statement
Reverse the bits of a given 32-bit unsigned integer. The input integer will be represented as an array of 32 bits, with each bit being either 0 or 1. The output should be the reversed array of bits. For example, if the input is [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0], the output should be [0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1]. The function should take an unsigned integer as input and return the reversed unsigned integer.

## Approach
The approach is to use bitwise operations to reverse the bits of the input integer. We can achieve this by shifting the bits to the left and right and using bitwise XOR operation to swap the bits. The algorithm will iterate over each bit in the input integer and swap it with the corresponding bit from the end.

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
        // shift the input to the right to move to the next bit
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
- Use bitwise operations to reverse the bits of an integer.
- Iterate over each bit in the input integer and swap it with the corresponding bit from the end.
- Use bitwise shift operators to move the bits to the left and right.