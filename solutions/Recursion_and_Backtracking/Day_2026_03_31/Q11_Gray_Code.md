# Gray Code

## Problem Statement
The Gray code is a binary numeral system where two successive values differ in only one bit. Given a non-negative integer `n` representing the number of bits in the Gray code, return a list of all possible Gray code sequences of length `n`. The output should be in the form of a list of integers, where each integer is represented by its binary value. For example, given `n = 2`, the output should be `[0, 1, 3, 2]`, which corresponds to the binary values `00`, `01`, `11`, and `10`.

## Approach
The problem can be solved using recursion and backtracking. We start with a base case of `n = 1`, where the only possible Gray code sequences are `0` and `1`. For larger values of `n`, we can construct the Gray code sequences by reflecting and prefixing the sequences of the previous length.

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
- The Gray code sequence can be generated using the formula `gray = i ^ (i >> 1)`, where `i` is the decimal value and `gray` is the corresponding Gray code value.
- The time complexity of the solution is O(2^n) because we need to generate all possible Gray code sequences of length `n`.
- The space complexity of the solution is O(2^n) because we need to store all the generated Gray code sequences.