# Number of 1 Bits

## Problem Statement
Write a function that takes an unsigned integer as input and returns the number of 1 bits in its binary representation. The input integer is guaranteed to be within the range of unsigned 32-bit integers. For example, the binary representation of 9 is 1001, so the function should return 2. The binary representation of 15 is 1111, so the function should return 4.

## Approach
The approach is to use bitwise operations to count the number of 1 bits in the binary representation of the input integer. We can use a loop to iterate over each bit in the integer. In each iteration, we check if the current bit is 1 and increment the count if it is. We can use the bitwise AND operator (&) to check if a bit is 1 and the bitwise right shift operator (>>) to move to the next bit.

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
            // If the least significant bit is 1, increment the count
            count += n & 1;
            // Right shift the bits to move to the next bit
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
- The bitwise right shift operator (>>) can be used to move to the next bit in an integer.
- The time complexity of this solution is O(log n) because we are iterating over each bit in the binary representation of the input integer.