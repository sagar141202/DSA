# Bitwise AND of Numbers Range

## Problem Statement
Given a range of numbers from `left` to `right` (inclusive), find the bitwise AND of all numbers in this range. The range is defined by two integers, `left` and `right`, where `1 <= left <= right <= 2^31 - 1`. For example, if the range is from 5 to 7, the bitwise AND of all numbers in this range would be the result of `5 & 6 & 7`.

## Approach
The algorithm works by finding the common prefix of the binary representation of `left` and `right`. This common prefix represents the bits that are the same in both `left` and `right`, which will also be the bits that are the same in all numbers in the range.

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
        // find the common prefix by shifting both numbers to the right
        // until they are equal
        int shift = 0;
        while (left < right) {
            left >>= 1;
            right >>= 1;
            shift++;
        }
        
        // the common prefix is the bitwise AND of the shifted numbers
        // shifted back to the left by the number of shifts
        return left << shift;
    }
};
```

## Test Cases
```
Input: left = 5, right = 7
Output: 4
```

## Key Takeaways
- The bitwise AND operation has a property where `a & b` will result in a number that has only the bits set that are common to both `a` and `b`.
- By shifting both numbers to the right until they are equal, we can find the common prefix of their binary representation.
- The common prefix represents the bits that are the same in all numbers in the range, and can be used to find the bitwise AND of all numbers in the range.