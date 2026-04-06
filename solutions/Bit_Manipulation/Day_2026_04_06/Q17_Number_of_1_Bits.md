# Number of 1 Bits

## Problem Statement
Write a function that takes an unsigned integer as input and returns the number of 1 bits in its binary representation. The input integer will be in the range [0, 2^32 - 1]. For example, the binary representation of 9 is 1001, so the function should return 2. The binary representation of 15 is 1111, so the function should return 4.

## Approach
The approach is to use bitwise operations to iterate over each bit in the input integer. We will use a while loop to repeatedly right shift the input integer and check the least significant bit. If the least significant bit is 1, we will increment the count of 1 bits.

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
            // Check the least significant bit
            count += n & 1;
            // Right shift the input integer
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
- The time complexity is O(log n) because we are iterating over each bit in the input integer.
- The space complexity is O(1) because we are only using a constant amount of space to store the count of 1 bits.
- The bitwise AND operator (&) is used to check the least significant bit of the input integer.