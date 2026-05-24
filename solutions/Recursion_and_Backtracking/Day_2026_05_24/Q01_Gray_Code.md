# Gray Code

## Problem Statement
The Gray code is a binary numeral system where two successive values differ in only one bit. Given a non-negative integer `n` representing the number of bits in the Gray code, return a list of all possible Gray code sequences of length `n`. For example, if `n = 2`, the output should be `["00", "01", "11", "10"]`. If `n = 1`, the output should be `["0", "1"]`. The constraint is `1 <= n <= 15`.

## Approach
The algorithm uses recursion and backtracking to generate all possible Gray code sequences. It starts with the base case where `n = 1` and then recursively generates the sequences for `n > 1` by prefixing `0` and `1` to the sequences of `n - 1`. The key insight is to reverse the second half of the sequences for `n - 1` when prefixing `1` to ensure that the Gray code property is maintained.

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
Input: n = 1
Output: [0, 1]
```

## Key Takeaways
- The Gray code can be generated using a simple XOR and right shift operation.
- The time complexity is exponential in the number of bits `n`.
- The space complexity is also exponential in the number of bits `n` due to the storage of the result.