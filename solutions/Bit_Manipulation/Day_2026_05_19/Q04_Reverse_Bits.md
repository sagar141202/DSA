# Reverse Bits

## Problem Statement
Reverse the bits of a given 32-bit unsigned integer. The function should take an unsigned integer as input and return the reversed bits as an unsigned integer. For example, if the input is 43261596 (represented as 00000010100101000001111010011100 in binary), the output should be 964176192 (represented as 00111001011110000010100100000000 in binary). The input is guaranteed to be a 32-bit unsigned integer.

## Approach
The algorithm involves iterating over each bit in the input number, checking if it's set, and setting the corresponding bit in the result from right to left. This is done by shifting the bits to the left for the result and to the right for the input number.

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
        // Check if the current bit is set
        result = (result << 1) | (n & 1);
        // Move to the next bit
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
- Bit manipulation involves using bitwise operators to achieve specific operations on bits.
- The left shift operator (`<<`) shifts the bits to the left, effectively multiplying the number by 2.
- The right shift operator (`>>`) shifts the bits to the right, effectively dividing the number by 2.