# Bitwise AND of Numbers Range

## Problem Statement
Given a range of numbers [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive. The input values m and n are integers. For example, if the input is m = 5 and n = 7, the output should be 4, because the bitwise AND of 5, 6, and 7 is 4 (5 = 101, 6 = 110, 7 = 111, so 101 & 110 & 111 = 100, which is 4).

## Approach
The algorithm finds the common prefix of the binary representation of m and n, then appends zeros to get the result. This works because the bitwise AND operation will result in zeros for any bits that differ between m and n. We can find the common prefix length by counting the number of leading zeros in the XOR of m and n.

## Complexity
- Time: O(log n)
- Space: O(1)

## C++ Solution
```cpp
class Solution {
public:
    int rangeBitwiseAnd(int m, int n) {
        // count the number of leading zeros in the XOR of m and n
        int shift = 0;
        while (m < n) {
            m >>= 1;
            n >>= 1;
            shift++;
        }
        // append zeros to the common prefix to get the result
        return m << shift;
    }
};
```

## Test Cases
```
Input: m = 5, n = 7
Output: 4
Input: m = 1, n = 2
Output: 0
```

## Key Takeaways
- The bitwise AND of a range of numbers can be found by finding the common prefix of the binary representation of the numbers.
- The common prefix length can be found by counting the number of leading zeros in the XOR of the numbers.
- We can use bitwise shift to efficiently find the common prefix and append zeros to get the result.