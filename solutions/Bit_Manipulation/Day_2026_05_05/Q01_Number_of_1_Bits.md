# Number of 1 Bits

## Problem Statement
Write a function that takes an unsigned integer as input and returns the number of 1 bits in its binary representation. The input will be an integer between 0 and 4294967295 (2^32 - 1). For example, the binary representation of 9 is 1001, so the function should return 2. The binary representation of 13 is 1101, so the function should return 3.

## Approach
The algorithm uses bit manipulation to count the number of 1 bits. It works by shifting the bits of the input number to the right and checking the least significant bit. If the least significant bit is 1, it increments the count. This process is repeated until all bits have been checked.

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
Input: 9
Output: 2
Input: 13
Output: 3
```

## Key Takeaways
- The algorithm uses bit manipulation to count the number of 1 bits in the binary representation of an integer.
- The time complexity is O(log n) because we are shifting the bits to the right until all bits have been checked.
- The space complexity is O(1) because we are only using a constant amount of space to store the count.