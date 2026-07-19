# Bitwise AND of Numbers Range

## Problem Statement
Given a range of numbers, find the bitwise AND of all numbers in the range [left, right] (inclusive). The range is defined by two integers, left and right, where 0 <= left <= right <= 2^31 - 1. For example, given the range [5, 7], the bitwise AND of all numbers in this range is 5 & 6 & 7 = 4, and given the range [2, 4], the bitwise AND is 2 & 3 & 4 = 0.

## Approach
The algorithm finds the common prefix of the binary representation of the left and right numbers, then constructs the result by appending zeros to this prefix. This approach works because the bitwise AND operation will result in zeros for any bits that are different between the two numbers.

## Complexity
- Time: O(logN)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int rangeBitwiseAnd(int left, int right) {
        int shift = 0;
        // find the common prefix
        while (left < right) {
            left >>= 1;
            right >>= 1;
            shift++;
        }
        // construct the result
        return left << shift;
    }
};

int main() {
    Solution solution;
    cout << solution.rangeBitwiseAnd(5, 7) << endl;  // Output: 4
    cout << solution.rangeBitwiseAnd(2, 4) << endl;   // Output: 0
    return 0;
}
```

## Test Cases
```
Input: left = 5, right = 7
Output: 4
Input: left = 2, right = 4
Output: 0
```

## Key Takeaways
- The bitwise AND operation can be used to find the common prefix of the binary representation of two numbers.
- The common prefix can be found by shifting the numbers to the right until they are equal.
- The result can be constructed by appending zeros to the common prefix.