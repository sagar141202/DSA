# Number of 1 Bits

## Problem Statement
The problem requires writing a function that takes an unsigned integer as input and returns the number of 1 bits in its binary representation. The input integer is guaranteed to be within the range of unsigned 32-bit integers. For example, given the input 9 (which is 1001 in binary), the function should return 2, because there are two 1 bits in the binary representation of 9.

## Approach
The algorithm uses bit manipulation to iterate over each bit in the binary representation of the input number. It checks each bit to see if it is 1, and if so, increments a counter. The function returns the total count of 1 bits. This approach works by utilizing the bitwise AND operator (&) and the right shift operator (>>).

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
            // Right shift the number to move to the next bit
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
- The right shift operator (>>) can be used to move to the next bit in the binary representation.
- The time complexity is O(log n) because in the worst case, we need to iterate over all bits in the binary representation of the input number.