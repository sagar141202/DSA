# Gray Code

## Problem Statement
The Gray code is a binary numeral system where two successive values differ in only one bit. Given a non-negative integer `n` representing the number of bits in the code, find all the Gray code sequences of length `n`. For example, if `n = 2`, the Gray code sequences are `["00", "01", "11", "10"]`. If `n = 1`, the Gray code sequences are `["0", "1"]`. The output should be a list of all possible Gray code sequences of length `n`.

## Approach
We can use recursion and backtracking to generate all possible Gray code sequences of length `n`. We will start with the base case where `n = 1` and then recursively generate the sequences for `n > 1` by prefixing `0` and `1` to the sequences of length `n - 1`.

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
            // Calculate the Gray code for the current number
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
- The Gray code sequence can be generated using the formula `gray = i ^ (i >> 1)`, where `i` is the current number.
- The time complexity of the solution is O(2^n) because we need to generate all possible Gray code sequences of length `n`.
- The space complexity of the solution is O(2^n) because we need to store all the generated Gray code sequences.