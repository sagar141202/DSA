# Excel Sheet Column Number

## Problem Statement
Given a string `s` which represents the column title of an Excel sheet, return its corresponding column number. The column title is in the range `[A, ZZ]`. For example, `A` corresponds to `1`, `B` corresponds to `2`, ..., `Z` corresponds to `26`, `AA` corresponds to `27`, and so on. The input string `s` will always be a valid column title.

## Approach
The algorithm involves treating the Excel column title as a base-26 number, where each character represents a digit in the range `[A, Z]`. We can then convert this base-26 number to a decimal number by iterating over the characters in the string and calculating the corresponding column number.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int titleToNumber(string s) {
        int result = 0;
        for (char c : s) {
            // Calculate the value of the current character and add it to the result
            result = result * 26 + (c - 'A' + 1);
        }
        return result;
    }
};
```

## Test Cases
```
Input: "A"
Output: 1
Input: "AB"
Output: 28
Input: "ZY"
Output: 701
```

## Key Takeaways
- The problem can be solved by treating the Excel column title as a base-26 number.
- We can use a simple iteration over the characters in the string to calculate the corresponding column number.
- The time complexity of the solution is linear, and the space complexity is constant.