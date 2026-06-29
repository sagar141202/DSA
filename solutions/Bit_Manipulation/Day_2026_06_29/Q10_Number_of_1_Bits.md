# Number of 1 Bits

## Problem Statement
Write a function that takes an unsigned integer as input and returns the number of 1 bits in its binary representation. The input integer is guaranteed to be within the range of unsigned 32-bit integers (0 to 2^32 - 1). For example, the binary representation of 11 is 1011, so the function should return 3.

## Approach
The approach is to use bit manipulation to iterate over each bit in the binary representation of the input integer. We can use a loop to shift the bits of the integer to the right and check the least significant bit. If the least significant bit is 1, we increment the count of 1 bits.

## Complexity
- Time: O(log n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int hammingWeight(uint32_t n) {
        int count = 0;
        while (n) {
            // check the least significant bit
            count += n & 1;
            // shift the bits to the right
            n >>= 1;
        }
        return count;
    }
};
```

## Test Cases
```
Input: 11
Output: 3
Input: 128
Output: 1
```

## Key Takeaways
- Use bit manipulation to iterate over each bit in the binary representation of the input integer.
- Use a loop to shift the bits of the integer to the right and check the least significant bit.
- The time complexity is O(log n) because we are shifting the bits to the right in each iteration, effectively dividing the number of bits by 2.