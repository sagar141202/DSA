# Number of 1 Bits

## Problem Statement
Write a function that takes an integer as input and returns the number of 1 bits in the binary representation of the integer. The integer is a 32-bit signed integer. For example, the binary representation of 9 is 1001, so the function should return 2. The function should handle integers with leading zeros.

## Approach
The approach is to use bit manipulation to iterate over each bit in the integer. We can use a while loop to keep shifting the bits to the right until the integer becomes zero. In each iteration, we check if the least significant bit is 1 and increment the count if it is.

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
- Bit manipulation can be used to solve problems that involve binary representation of integers.
- The time complexity of the solution depends on the number of bits in the integer, which is typically 32 for a 32-bit signed integer.
- The space complexity is O(1) because we only use a constant amount of space to store the count and the integer.