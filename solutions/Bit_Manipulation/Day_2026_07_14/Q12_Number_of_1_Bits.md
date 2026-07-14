# Number of 1 Bits

## Problem Statement
Write a function that takes an unsigned integer as input and returns the number of 1 bits in its binary representation. The input integer is guaranteed to be within the range of unsigned 32-bit integers. For example, the binary representation of 11 is 1011, so the function should return 3.

## Approach
The approach is to use bit manipulation to count the number of 1 bits in the binary representation of the input integer. We can achieve this by using a while loop to iterate through each bit of the integer and a bitwise AND operation to check if the current bit is 1.

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
            // use bitwise AND to check if the least significant bit is 1
            count += n & 1;
            // use bitwise right shift to move to the next bit
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
- Use bitwise operations to manipulate individual bits of an integer.
- The bitwise AND operator (&) can be used to check if a bit is 1.
- The bitwise right shift operator (>>) can be used to move to the next bit.