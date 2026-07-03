# Reverse Bits

## Problem Statement
Reverse the bits of a given 32-bit unsigned integer. The input integer will be represented as a binary string of 32 bits, with leading zeros if necessary. The output should also be a binary string of 32 bits, representing the reversed bits of the input integer. For example, the input "00000000000000000000000000001011" should return "11010000000000000000000000000000". The input integer will not be greater than 2^31 - 1.

## Approach
The approach to solve this problem is to use bit manipulation to reverse the bits of the input integer. We can achieve this by shifting the bits to the left and right, and using bitwise OR operation to combine the reversed bits. The algorithm will iterate over each bit in the input integer and reverse its position.

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
Input: 00000000000000000000000000001011
Output: 11010000000000000000000000000000
Input: 11111111111111111111111111111111
Output: 11111111111111111111111111111111
```

## Key Takeaways
- Bit manipulation can be used to reverse the bits of an integer.
- The algorithm should iterate over each bit in the input integer and reverse its position.
- The time complexity of the algorithm is O(1) because it only iterates over a fixed number of bits (32 bits in this case).