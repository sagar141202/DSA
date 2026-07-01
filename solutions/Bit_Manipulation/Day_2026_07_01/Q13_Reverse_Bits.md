# Reverse Bits

## Problem Statement
The problem requires reversing the bits of a given 32-bit unsigned integer. The integer is represented as a sequence of 32 bits (0s and 1s). We need to reverse the order of these bits. For example, if the input is 43261596 (represented as 00000010100101000001111010011100 in binary), the output will be 964176192 (represented as 00111001011110000010100100000000 in binary). The constraints are that the input is a 32-bit unsigned integer.

## Approach
We will use bit manipulation to solve this problem. The idea is to iterate over each bit of the input number from right to left and append it to the result.

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
        // append the least significant bit of n to result
        result = (result << 1) | (n & 1);
        // remove the least significant bit of n
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
- Bit manipulation can be used to solve problems that involve binary representation of numbers.
- Use of bitwise operators (<<, >>, &, |) can simplify the solution and improve performance.
- Always consider the constraints of the problem and choose the most efficient approach accordingly.