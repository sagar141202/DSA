# Bitwise AND of Numbers Range

## Problem Statement
Given a range of numbers [left, right], find the bitwise AND of all numbers in this range. The range is inclusive, and left and right are non-negative integers. For example, given the range [5, 7], the bitwise AND of all numbers in this range is 5 & 6 & 7 = 4. The range is 0 <= left <= right <= 2^31 - 1.

## Approach
To find the bitwise AND of all numbers in a given range, we can find the common prefix of the binary representation of the left and right numbers. This common prefix will be the bitwise AND of all numbers in the range. We can use bit manipulation to achieve this.

## Complexity
- Time: O(log n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int rangeBitwiseAnd(int left, int right) {
        // find the common prefix by shifting right
        int shift = 0;
        while (left < right) {
            left >>= 1;
            right >>= 1;
            shift++;
        }
        // return the common prefix
        return left << shift;
    }
};

int main() {
    Solution solution;
    cout << solution.rangeBitwiseAnd(5, 7) << endl;  // Output: 4
    return 0;
}
```

## Test Cases
```
Input: left = 5, right = 7
Output: 4
Input: left = 2, right = 3
Output: 2
```

## Key Takeaways
- The bitwise AND of all numbers in a range can be found by finding the common prefix of the binary representation of the left and right numbers.
- Bit manipulation can be used to find the common prefix by shifting right.
- The time complexity of this solution is O(log n), where n is the maximum possible value of the input numbers.