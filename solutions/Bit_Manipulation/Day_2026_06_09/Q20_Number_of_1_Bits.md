# Number of 1 Bits

## Problem Statement
Write a function that takes an unsigned integer as input and returns the number of 1 bits in its binary representation. The input integer is guaranteed to be within the range of unsigned 32-bit integers. For example, the binary representation of 9 is 1001, so the function should return 2. The binary representation of 15 is 1111, so the function should return 4.

## Approach
The approach is to use bit manipulation to iterate over each bit in the input integer. We can use the bitwise AND operator to check if a bit is 1 and the bitwise right shift operator to move to the next bit. The algorithm iterates until all bits have been checked.

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
Input: 9
Output: 2
Input: 15
Output: 4
```

## Key Takeaways
- The bitwise AND operator (&) can be used to check if a bit is 1.
- The bitwise right shift operator (>>) can be used to move to the next bit.
- The time complexity is O(log n) because we iterate over each bit in the input integer, and the number of bits in an unsigned 32-bit integer is 32.