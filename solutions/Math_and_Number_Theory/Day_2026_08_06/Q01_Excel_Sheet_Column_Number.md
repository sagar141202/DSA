# Excel Sheet Column Number

## Problem Statement
Given a string columnTitle representing the column title as it appears in an Excel sheet, return its corresponding column number. The column title is in the range [A, Z] where 'A' represents the 1st column, 'B' represents the 2nd column, and so on. For example, given columnTitle = "A", the output should be 1. Given columnTitle = "AB", the output should be 28.

## Approach
The approach is to treat the Excel column title as a base-26 number, where 'A' represents 1, 'B' represents 2, and so on. We iterate over the string from left to right, calculate the value of each character, and add it to the total value after shifting the current total value to the left by one place (i.e., multiplying by 26).

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int titleToNumber(string columnTitle) {
        int result = 0;
        for (char c : columnTitle) {
            // calculate the value of the current character
            int value = c - 'A' + 1;
            // add the value to the total after shifting the current total
            result = result * 26 + value;
        }
        return result;
    }
};
```

## Test Cases
```
Input: columnTitle = "A"
Output: 1
Input: columnTitle = "AB"
Output: 28
Input: columnTitle = "ZY"
Output: 701
```

## Key Takeaways
- The Excel column title can be treated as a base-26 number.
- We can calculate the column number by iterating over the string and shifting the current total value to the left by one place (multiplying by 26) in each iteration.
- The time complexity of this solution is linear with respect to the length of the input string.