# Bitwise AND of Numbers Range

## Problem Statement
Given a range of numbers from `left` to `right` (inclusive), find the bitwise AND of all numbers in this range. The input range is guaranteed to be non-empty and `left` is less than or equal to `right`. The range is defined as `[left, right]`. For example, given `left = 5` and `right = 7`, the bitwise AND of all numbers in this range is `5 & 6 & 7 = 4`.

## Approach
The algorithm starts by finding the common prefix of the binary representation of `left` and `right`. It then constructs the result by appending zeros to this common prefix. The intuition is that the bitwise AND operation will result in zeros for all bits where `left` and `right` have different values.

## Complexity
- Time: O(log n)
- Space: O(1)

## C++ Solution
```cpp
class Solution {
public:
    int rangeBitwiseAnd(int left, int right) {
        // find the number of common prefix bits
        int shift = 0;
        while (left < right) {
            left >>= 1;
            right >>= 1;
            shift++;
        }
        // append zeros to the common prefix
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
- The bitwise AND operation can be simplified by finding the common prefix of the binary representation of the input numbers.
- Right shifting both numbers until they are equal helps to find the common prefix.
- The result can be constructed by appending zeros to the common prefix.