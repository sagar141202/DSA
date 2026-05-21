# Gray Code

## Problem Statement
The Gray code is a binary numeral system where two successive values differ in only one bit. Given a non-negative integer n representing the number of bits in the Gray code, return a list of all possible Gray codes of that length. For example, for n = 2, the output should be ["00", "01", "11", "10"]. The constraints are 1 <= n <= 16.

## Approach
The problem can be solved using recursion and backtracking by generating all possible binary numbers of length n and then filtering out the ones that do not meet the Gray code condition. However, a more efficient approach is to use the property of Gray codes that the first half of the Gray codes of length n are the same as the Gray codes of length n-1, and the second half are the same but with the bits reversed.

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
            // calculate the gray code for the current number
            int gray = i ^ (i >> 1);
            result.push_back(gray);
        }
        return result;
    }
};
```

## Test Cases
```
Input: 2
Output: [0, 1, 3, 2]
Input: 3
Output: [0, 1, 3, 2, 6, 7, 5, 4]
```

## Key Takeaways
- The Gray code can be generated using the property that the first half of the Gray codes of length n are the same as the Gray codes of length n-1, and the second half are the same but with the bits reversed.
- The XOR operator can be used to calculate the Gray code for a given number.
- The time complexity of the solution is O(2^n) because there are 2^n possible Gray codes of length n.