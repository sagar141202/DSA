# Gray Code

## Problem Statement
The Gray code is a binary numeral system where two successive values differ in only one bit. Given a non-negative integer `n` representing the number of bits in the code, find the sequence of Gray code of `n` bits. The sequence should be in the form of a list of integers, where each integer is represented by `n` bits. For example, if `n = 2`, the output should be `[0, 1, 3, 2]`, which corresponds to the binary numbers `00, 01, 11, 10`.

## Approach
The Gray code sequence can be generated using recursion and backtracking. We can start with the base case of `n = 1` and then recursively generate the sequence for `n` bits by reflecting and prefixing the sequence for `n-1` bits. The reflection involves reversing the sequence, and the prefixing involves adding a `0` or `1` to the beginning of each number in the sequence.

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
            // calculate the gray code using bitwise XOR operation
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
- The Gray code sequence can be generated using a simple bitwise XOR operation.
- The time complexity of the solution is O(2^n) due to the iteration over all possible binary numbers of `n` bits.
- The space complexity is also O(2^n) as we need to store the entire Gray code sequence.