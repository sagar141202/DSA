# Number of 1 Bits

## Problem Statement
Write a function that takes an unsigned integer as input and returns the number of 1 bits in its binary representation. The input integer is guaranteed to be within the range of 0 to 4294967295. For example, the binary representation of 9 is 1001, so the function should return 2. The binary representation of 15 is 1111, so the function should return 4.

## Approach
The approach is to use bit manipulation to count the number of 1 bits in the binary representation of the input integer. We can achieve this by using the bitwise AND operator and the right shift operator. The idea is to repeatedly clear the least significant 1 bit in the integer until all bits are 0.

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
            // clear the least significant 1 bit
            n &= (n - 1);
            count++;
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
- The bitwise AND operator (&) is used to clear the least significant 1 bit in the integer.
- The expression `n & (n - 1)` is used to clear the least significant 1 bit in the integer.
- The time complexity is O(log n) because in the worst case, we need to iterate log(n) times to clear all bits in the integer.