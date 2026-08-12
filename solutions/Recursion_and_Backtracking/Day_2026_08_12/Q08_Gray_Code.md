# Gray Code

## Problem Statement
The Gray code is a binary numeral system where two successive values differ in only one bit. Given a non-negative integer `n` representing the number of bits in the code, find all the Gray code sequences of length `n`. The output should be a list of integers in the Gray code sequence. For example, for `n = 2`, the output should be `[0, 1, 3, 2]`, which corresponds to the binary sequences `00`, `01`, `11`, and `10`.

## Approach
The Gray code sequence can be generated using recursion and backtracking. We start with the base case where `n = 1`, and then recursively generate the sequence for `n > 1` by reflecting and prefixing the sequence for `n - 1`. This approach ensures that each successive value in the sequence differs in only one bit.

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
- The Gray code sequence has a simple and efficient recursive structure.
- The `^` operator is used to compute the Gray code for each number `i`.
- The time and space complexity are exponential in `n`, which is inherent to the problem.