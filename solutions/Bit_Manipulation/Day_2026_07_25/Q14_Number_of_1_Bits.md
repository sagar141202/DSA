# Number of 1 Bits

## Problem Statement
Write a function that takes an unsigned integer as input and returns the number of 1 bits in its binary representation. The input integer is guaranteed to be within the range of unsigned 32-bit integers. For example, the binary representation of 9 is 1001, so the function should return 2. The binary representation of 15 is 1111, so the function should return 4.

## Approach
The approach to solve this problem is to use bit manipulation techniques. We can use the bitwise AND operator (&) and the bitwise right shift operator (>>) to iterate through each bit in the binary representation of the input integer. If the current bit is 1, we increment the count of 1 bits.

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
            // if the current bit is 1, increment the count
            count += n & 1;
            // right shift the bits by 1
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
- The bitwise AND operator (&) is used to check if a bit is 1.
- The bitwise right shift operator (>>) is used to iterate through each bit in the binary representation of the input integer.
- The time complexity is O(log n) because we are iterating through each bit in the binary representation of the input integer, and the number of bits is proportional to the logarithm of the input integer.