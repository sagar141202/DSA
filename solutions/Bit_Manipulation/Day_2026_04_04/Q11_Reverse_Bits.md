# Reverse Bits

## Problem Statement
Reverse the bits of a given 32-bit unsigned integer. The input integer will be represented as a sequence of 32 bits, and the output should also be a sequence of 32 bits. The problem can be solved by iterating over each bit of the input integer and appending it to the result. For example, the binary representation of the decimal number 43261596 is 10101000000000000000000000010100, and its reverse is 00101000000000000000000001010101, which is the binary representation of the decimal number 964176192.

## Approach
The approach to solve this problem is to use bitwise operations to iterate over each bit of the input integer and append it to the result. We can achieve this by using a loop that runs 32 times, and in each iteration, we check the least significant bit of the input integer and append it to the result.

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
        // Check the least significant bit of the input integer
        result = (result << 1) | (n & 1);
        // Right shift the input integer by 1 bit
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
- Use bitwise operations to iterate over each bit of the input integer.
- Use a loop that runs 32 times to cover all bits of the input integer.
- Use the left shift operator to append the least significant bit of the input integer to the result.