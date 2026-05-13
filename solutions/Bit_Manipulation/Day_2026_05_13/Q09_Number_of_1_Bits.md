# Number of 1 Bits

## Problem Statement
Write a function that takes an unsigned integer as input and returns the number of 1 bits in its binary representation. The input will be in the range [0, 2^32 - 1]. For example, the binary representation of 9 is 1001, so the function should return 2. The binary representation of 15 is 1111, so the function should return 4.

## Approach
The approach is to use bit manipulation to count the number of 1 bits in the binary representation of the input number. We can achieve this by using a loop to iterate over each bit in the number and check if it is 1. We can use the bitwise AND operator (&) with 1 to check if a bit is 1.

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
            // use bitwise AND with 1 to check if the least significant bit is 1
            count += n & 1;
            // right shift by 1 to move to the next bit
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
- Use bit manipulation to solve problems related to binary representation.
- The bitwise AND operator (&) can be used to check if a bit is 1.
- The right shift operator (>>=) can be used to move to the next bit in the binary representation.