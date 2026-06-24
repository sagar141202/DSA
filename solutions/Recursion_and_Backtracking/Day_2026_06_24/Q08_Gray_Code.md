# Gray Code

## Problem Statement
The Gray Code is a sequence of binary numbers where only one bit is changed between consecutive numbers. Given an integer `n`, generate all `n`-bit Gray Code sequences. For example, for `n = 2`, the Gray Code sequence is `["00", "01", "11", "10"]`. The sequence should be generated in lexicographical order.

## Approach
The Gray Code sequence can be generated using a recursive approach, where each `n`-bit sequence is constructed from the `(n-1)`-bit sequence by prefixing `0` and `1` to the `(n-1)`-bit sequence in a specific order. This ensures that only one bit is changed between consecutive numbers.

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
            // Calculate the Gray Code using XOR and right shift
            int gray = i ^ (i >> 1);
            result.push_back(gray);
        }
        return result;
    }
};

// Alternative recursive solution
class SolutionRecursive {
public:
    vector<string> grayCode(int n) {
        if (n == 1) {
            return {"0", "1"};
        }
        vector<string> prev = grayCode(n - 1);
        vector<string> result;
        for (const auto& code : prev) {
            result.push_back("0" + code);
        }
        for (auto it = prev.rbegin(); it != prev.rend(); ++it) {
            result.push_back("1" + *it);
        }
        return result;
    }
};
```

## Test Cases
```
Input: n = 2
Output: ["00", "01", "11", "10"]
Input: n = 3
Output: ["000", "001", "011", "010", "110", "111", "101", "100"]
```

## Key Takeaways
- The Gray Code sequence can be generated using a recursive approach or using bitwise operations.
- The time complexity is O(2^n) because there are 2^n possible binary numbers of length `n`.
- The space complexity is O(2^n) because we need to store all the generated Gray Code sequences.