# Gray Code

## Problem Statement
The Gray code is a binary numeral system where two successive values differ in only one bit. Given a non-negative integer `n` representing the number of bits in the code, find all `n`-bit Gray codes in ascending order. For example, for `n = 2`, the output should be `["00", "01", "11", "10"]`. The constraints are `1 <= n <= 16`.

## Approach
The approach to solve this problem is to use recursion and backtracking. We start with the base case where `n` is 1, and then recursively generate the Gray codes for `n` bits by reflecting and prefixing the codes for `n-1` bits.

## Complexity
- Time: O(2^n)
- Space: O(2^n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> grayCode(int n) {
        vector<int> result;
        for (int i = 0; i < (1 << n); i++) {
            // Calculate the Gray code using bitwise XOR
            int gray = i ^ (i >> 1);
            result.push_back(gray);
        }
        return result;
    }
};
```

## Test Cases
```
Input: n = 2
Output: [0, 1, 3, 2]
```

## Key Takeaways
- The Gray code can be generated using a simple bitwise XOR operation.
- The time complexity is exponential due to the recursive nature of the problem.
- The space complexity is also exponential as we need to store all the generated Gray codes.