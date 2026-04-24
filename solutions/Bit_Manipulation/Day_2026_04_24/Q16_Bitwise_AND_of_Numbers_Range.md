# Bitwise AND of Numbers Range

## Problem Statement
Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive. For example, if the input is [5, 7], the output should be 4 because the bitwise AND of 5, 6, and 7 is 4 (5 = 101, 6 = 110, 7 = 111, so 101 & 110 & 111 = 100 which is 4). The constraints are that m and n are integers and 0 <= m <= n <= 2147483647.

## Approach
The algorithm is based on finding the common prefix of the binary representation of m and n. The bitwise AND of all numbers in the range [m, n] will be the common prefix of m and n, padded with zeros to the right. This is because any bit that is different between m and n will have at least one number in the range where that bit is zero, so the bitwise AND of all numbers will have that bit as zero.

## Complexity
- Time: O(log n)
- Space: O(1)

## C++ Solution
```cpp
class Solution {
public:
    int rangeBitwiseAnd(int m, int n) {
        // find the common prefix of m and n
        int shift = 0;
        while (m < n) {
            m >>= 1;
            n >>= 1;
            shift++;
        }
        // return the common prefix padded with zeros
        return m << shift;
    }
};
```

## Test Cases
```
Input: m = 5, n = 7
Output: 4
Input: m = 0, n = 0
Output: 0
Input: m = 1, n = 2
Output: 0
```

## Key Takeaways
- The bitwise AND of all numbers in a range [m, n] can be found by finding the common prefix of the binary representation of m and n.
- The common prefix can be found by shifting m and n to the right until they are equal.
- The result can be obtained by shifting the common prefix to the left by the number of shifts performed.