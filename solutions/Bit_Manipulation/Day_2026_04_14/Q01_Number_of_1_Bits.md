# Number of 1 Bits

## Problem Statement
Write a function that takes an unsigned integer as input and returns the number of 1 bits in its binary representation. The input integer is guaranteed to be within the range of unsigned 32-bit integers. For example, the binary representation of 9 is 1001, so the function should return 2. The binary representation of 15 is 1111, so the function should return 4.

## Approach
The approach is to use bitwise operations to count the number of 1 bits in the binary representation of the input integer. We can use a loop to iterate over each bit in the integer and check if it is 1. The algorithm will use bitwise AND operation with 1 to check if the least significant bit is 1, and then right shift the integer to move to the next bit.

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
            // check if the least significant bit is 1
            count += n & 1;
            // right shift to move to the next bit
            n >>= 1;
        }
        return count;
    }
};
```

## Test Cases
```
Input: 9
Output: 2
Input: 15
Output: 4
```

## Key Takeaways
- Use bitwise operations to efficiently count the number of 1 bits in an integer's binary representation.
- The time complexity is O(log n) because we are iterating over each bit in the integer, and the number of bits in an integer is proportional to the logarithm of the integer's value.
- The space complexity is O(1) because we are using a constant amount of space to store the count of 1 bits.