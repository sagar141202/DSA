# Gray Code

## Problem Statement
The Gray code is a binary numeral system where two successive values differ in only one bit. Given a non-negative integer `n` representing the number of bits in the code, find all the Gray code sequences of length `n`. For example, if `n = 2`, the output should be `["00", "01", "11", "10"]`. The output sequences should be in ascending order.

## Approach
We will use recursion and backtracking to generate all possible Gray code sequences. The key idea is to start with the most significant bit and recursively generate all possible sequences for the remaining bits. We will use a helper function to reflect and prefix the sequences.

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

// Alternatively, recursive solution
class SolutionRecursive {
public:
    vector<string> grayCode(int n) {
        vector<string> result;
        helper(n, result);
        return result;
    }

    void helper(int n, vector<string>& result) {
        if (n == 0) {
            result.push_back("0");
            return;
        }
        if (n == 1) {
            result.push_back("0");
            result.push_back("1");
            return;
        }
        vector<string> temp;
        helper(n - 1, temp);
        // Reflect and prefix the sequences
        for (string str : temp) {
            result.push_back("0" + str);
        }
        reverse(temp.begin(), temp.end());
        for (string str : temp) {
            result.push_back("1" + str);
        }
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
- The Gray code sequence can be generated using recursion and backtracking.
- The key idea is to start with the most significant bit and recursively generate all possible sequences for the remaining bits.
- The `i ^ (i >> 1)` formula can be used to calculate the Gray code for a given number `i`.