# Gray Code

## Problem Statement
The Gray code is a binary sequence where two successive values differ in only one bit. Given an integer `n`, generate all possible `n`-bit Gray codes. For example, for `n = 2`, the Gray codes are `00`, `01`, `11`, and `10`. The generated codes should be in ascending order.

## Approach
We will use recursion and backtracking to generate all possible Gray codes by reflecting and prefixing the codes for `n-1` bits. The base case is when `n` is 1, in which case the Gray codes are `0` and `1`.

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
            // calculate the Gray code using XOR and right shift
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
- The Gray code can be generated using the formula `gray = i ^ (i >> 1)`, where `i` is the binary number.
- The time complexity is O(2^n) because we are generating all possible `n`-bit binary numbers.
- The space complexity is also O(2^n) because we need to store all the generated Gray codes.