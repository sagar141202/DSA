# Reverse Bits

## Problem Statement
The problem requires reversing the bits of a given 32-bit unsigned integer. The integer is represented in binary form, and we need to reverse the order of its bits. For example, if the input is 43261596 (represented as 00000010100101000001111010011100 in binary), the output should be 964176192 (represented as 00111001011110000010100100000000 in binary). The constraints are that the input integer will be between 0 and 2^32 - 1.

## Approach
We can solve this problem by using bitwise operations to reverse the bits of the input integer. The idea is to iterate over each bit of the input integer from right to left, and append it to the result.

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
        // append the current bit of n to the result
        result = (result << 1) | (n & 1);
        // remove the current bit from n
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
- We can use bitwise operations to reverse the bits of an integer.
- The time complexity is O(1) because we are iterating over a fixed number of bits (32).
- The space complexity is O(1) because we are using a constant amount of space to store the result.