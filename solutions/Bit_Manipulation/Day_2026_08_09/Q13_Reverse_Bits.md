# Reverse Bits

## Problem Statement
Reverse the bits of a given 32-bit unsigned integer. The input integer will be represented as a decimal number, and the output should also be a decimal number. For example, if the input is 43261596 (which is 00000010100101000001111010011100 in binary), the output should be 964176192 (which is 00111001011110000010100100000000 in binary). The function should take an unsigned integer as input and return the decimal equivalent of the reversed binary representation.

## Approach
The approach involves converting the integer to binary, reversing the binary string, and then converting it back to decimal. We can achieve this using bitwise operations. We will iterate through each bit of the input number, and for each bit, we will append it to the result after shifting the current result to the left.

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
        // append the last bit of n to the result
        result = (result << 1) | (n & 1);
        // remove the last bit from n
        n = n >> 1;
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
- The left shift operator (`<<`) is used to shift the bits of the result to the left, making space for the new bit.
- The bitwise AND operator (`&`) is used to extract the last bit of the input number.
- The right shift operator (`>>`) is used to remove the last bit from the input number.