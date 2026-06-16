# Bitwise AND of Numbers Range

## Problem Statement
Given a range of numbers, find the bitwise AND of all numbers in the range [left, right] (inclusive). The range is defined by two integers, left and right, where 0 <= left <= right <= 2^31 - 1. For example, given left = 5 and right = 7, the bitwise AND of all numbers in the range is 4 (5 & 6 & 7 = 4).

## Approach
The algorithm involves shifting both numbers to the right until they are equal, then shifting the result back to the left. This approach works because the bitwise AND operation will preserve the common prefix of the binary representations of the numbers. The number of shifts required is the number of bits that differ between the two numbers.

## Complexity
- Time: O(log N)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int rangeBitwiseAnd(int left, int right) {
        int shift = 0;
        // shift to the right until left and right are equal
        while (left < right) {
            left >>= 1;
            right >>= 1;
            shift++;
        }
        // shift the result back to the left
        return left << shift;
    }
};
```

## Test Cases
```
Input: left = 5, right = 7
Output: 4
Input: left = 1, right = 2
Output: 0
```

## Key Takeaways
- The bitwise AND operation can be used to find the common prefix of the binary representations of two numbers.
- Shifting numbers to the right can be used to remove the differing bits and preserve the common prefix.
- The number of shifts required is equal to the number of bits that differ between the two numbers.