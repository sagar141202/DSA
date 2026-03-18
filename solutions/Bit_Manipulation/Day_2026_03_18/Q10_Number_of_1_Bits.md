# Number of 1 Bits

## Problem Statement
Write a function that takes an unsigned integer as input and returns the number of 1 bits in its binary representation. The input integer is guaranteed to be within the range of unsigned 32-bit integers. For example, the binary representation of 9 is 1001, so the function should return 2. The binary representation of 15 is 1111, so the function should return 4.

## Approach
The algorithm uses bit manipulation to count the number of 1 bits in the binary representation of the input integer. It works by shifting the bits of the integer to the right and checking the least significant bit. The process is repeated until all bits have been checked. This approach takes advantage of the properties of binary numbers and bit shifting operations.

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
Input: 15
Output: 4
```

## Key Takeaways
- Bit manipulation can be used to efficiently count the number of 1 bits in a binary representation.
- The algorithm has a time complexity of O(log n) due to the shifting operation.
- The space complexity is O(1) since only a constant amount of space is used.