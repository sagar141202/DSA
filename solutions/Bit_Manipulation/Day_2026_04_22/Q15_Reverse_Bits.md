# Reverse Bits

## Problem Statement
The problem requires reversing the bits of a given 32-bit unsigned integer. The integer is represented in binary form, and we need to reverse the order of its bits. For example, if the input is 43261596 (which is 00000010100101000001111010011100 in binary), the output should be 964176192 (which is 11101001100101000010100100000000 in binary). The constraints are that the input will always be a 32-bit unsigned integer.

## Approach
We can solve this problem by using bitwise operations to extract each bit from the input number and then append it to the result. We will use a loop to iterate over each bit in the input number.

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
        // extract the least significant bit from n and append it to result
        result = (result << 1) | (n & 1);
        // right shift n to remove the least significant bit
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
Output: 3221225471
```

## Key Takeaways
- Use bitwise operations to extract and append bits.
- The time complexity is constant (O(1)) because we are always iterating over 32 bits.
- The space complexity is constant (O(1)) because we are only using a fixed amount of space to store the result.