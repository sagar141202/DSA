# Number of 1 Bits

## Problem Statement
Write a function that takes an unsigned integer as input and returns the number of 1 bits in its binary representation. The input integer is in the range [0, 2^32 - 1]. For example, the binary representation of 11 is 1011, so the function should return 3.

## Approach
The approach is to use bit manipulation to count the number of 1 bits in the binary representation of the input integer. We can use the bitwise AND operator (&) and the bitwise right shift operator (>>) to achieve this. The idea is to keep shifting the bits to the right and count the number of 1 bits.

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
            // if the least significant bit is 1, increment count
            count += n & 1;
            // right shift by 1 bit
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
- Use bitwise operators to manipulate bits in the binary representation of an integer.
- The bitwise AND operator (&) can be used to check if a bit is 1.
- The bitwise right shift operator (>>) can be used to shift bits to the right.