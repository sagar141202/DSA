# Gray Code

## Problem Statement
The Gray code is a binary numeral system where two successive values differ in only one bit. Given a non-negative integer `n`, generate all the Gray code of `n` bits. For example, if `n = 2`, the Gray code is `["00", "01", "11", "10"]`. The output should be in any order.

## Approach
The algorithm uses recursion and backtracking to generate the Gray code. It starts with the base case of `n = 1` and then recursively generates the Gray code for `n` bits by reflecting and prefixing the Gray code for `n-1` bits.

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
            // Calculate the Gray code using XOR and right shift
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
Input: n = 3
Output: [0, 1, 3, 2, 6, 7, 5, 4]
```

## Key Takeaways
- The Gray code can be generated using a simple XOR and right shift operation.
- The time complexity is O(2^n) because there are 2^n possible Gray codes for `n` bits.
- The space complexity is also O(2^n) because we need to store all the Gray codes in the result vector.