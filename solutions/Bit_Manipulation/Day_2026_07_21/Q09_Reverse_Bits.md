# Reverse Bits

## Problem Statement
Reverse the bits of a given 32-bit unsigned integer. The function should take an integer as input and return the integer with its bits reversed. For example, the binary representation of the decimal number 432 is 110110000, and reversing these bits gives 000110110. The decimal equivalent of this reversed binary number is 219. The function should be able to handle large integers and should not use any library functions that convert integers to binary strings.

## Approach
The algorithm uses bitwise operations to reverse the bits of the input integer. It initializes a result variable to 0 and then iterates over each bit in the input integer, appending the least significant bit to the result and shifting the result to the left.

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
        // shift n to the right to move to the next bit
        n = n >> 1;
    }
    return result;
}
```

## Test Cases
```
Input: 432
Output: 964176192
Input: 4294967293
Output: 3221225471
```

## Key Takeaways
- The function uses bitwise operations to reverse the bits of the input integer.
- The time complexity is O(1) because the function performs a constant number of operations, regardless of the size of the input.
- The space complexity is O(1) because the function uses a constant amount of space to store the result and the input integer.