# Bitwise AND of Numbers Range

## Problem Statement
Given a range of integers [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive. The bitwise AND of a range is the bitwise AND of all numbers from m to n. For example, given the range [5, 7], the bitwise AND is 5 & 6 & 7 = 4, and given the range [2, 4], the bitwise AND is 2 & 3 & 4 = 0.

## Approach
The approach is to find the common prefix of the binary representation of m and n. We can do this by shifting both m and n to the right until they are equal. The number of shifts required is the number of bits that are different between m and n. We can then shift 1 to the left by the number of common prefix bits and subtract 1 to get the bitwise AND of the range.

## Complexity
- Time: O(log n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int rangeBitwiseAnd(int m, int n) {
        // find the number of shifts required
        int shift = 0;
        while (m != n) {
            m >>= 1;
            n >>= 1;
            shift++;
        }
        // shift 1 to the left by the number of common prefix bits and subtract 1
        return m << shift;
    }
};
```

## Test Cases
```
Input: m = 5, n = 7
Output: 4
Input: m = 2, n = 4
Output: 0
```

## Key Takeaways
- The bitwise AND of a range can be found by finding the common prefix of the binary representation of the numbers in the range.
- We can use bit shifting to find the common prefix.
- The number of shifts required is the number of bits that are different between the numbers in the range.