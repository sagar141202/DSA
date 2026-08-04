# Gray Code

## Problem Statement
The Gray code is a binary numeral system where two successive values differ in only one bit. Given a non-negative integer `n`, generate all the Gray code of `n` bits. The output should be in ascending order. For example, if `n = 2`, the output should be `["00", "01", "11", "10"]`. If `n = 1`, the output should be `["0", "1"]`.

## Approach
The Gray code can be generated using recursion and backtracking. We can start with the base case where `n = 1` and then recursively generate the Gray code for `n` bits by reflecting and prefixing the Gray code for `n-1` bits.

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
            // XOR operation to generate Gray code
            result.push_back(i ^ (i >> 1));
        }
        return result;
    }
};
```

## Test Cases
```
Input: n = 2
Output: [0, 1, 3, 2]
Input: n = 1
Output: [0, 1]
```

## Key Takeaways
- The Gray code can be generated using a simple XOR operation.
- The time complexity is O(2^n) because we are generating all possible binary numbers of `n` bits.
- The space complexity is O(2^n) because we are storing all the generated Gray codes.