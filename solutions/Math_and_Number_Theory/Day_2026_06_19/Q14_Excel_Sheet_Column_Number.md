# Excel Sheet Column Number

## Problem Statement
Given a string `s` representing the column title of an Excel sheet, return its corresponding column number. The column title is in the range `[A, Z]` where `A` represents 1, `B` represents 2, and so on. For example, `ZY` would be `701` because `Z` represents 26 and `Y` represents 25, then `26 * 26 + 25 = 701`. The input string `s` consists only of uppercase English letters and has a length of at least 1.

## Approach
The algorithm involves treating the Excel column title as a base-26 number system, where each character represents a digit in this system. We iterate through the string from left to right, calculating the value of each character and adding it to a running total after multiplying it by the appropriate power of 26.

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
- We need to iterate through the string and calculate the value of each character based on its position and the base-26 system.
- The time complexity is linear with respect to the length of the input string, and the space complexity is constant.