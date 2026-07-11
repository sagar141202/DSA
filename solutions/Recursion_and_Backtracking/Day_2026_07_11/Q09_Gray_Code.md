# Gray Code

## Problem Statement
The Gray code is a binary numeral system where two successive values differ in only one bit. Given a non-negative integer `n` representing the number of bits, generate all the Gray code sequences of length `n`. For example, if `n = 2`, the output should be `["00", "01", "11", "10"]`. The generated sequences can be in any order.

## Approach
The algorithm uses recursion and backtracking to generate all possible Gray code sequences. It starts with an initial sequence and then recursively generates the next sequence by changing one bit at a time. The key insight is to use the property of Gray code that two successive values differ in only one bit.

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
            // Calculate the Gray code using the XOR operation
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
- The Gray code can be generated using the XOR operation and bit shifting.
- The time complexity is O(2^n) because there are 2^n possible Gray code sequences of length n.
- The space complexity is O(2^n) because we need to store all the generated sequences.