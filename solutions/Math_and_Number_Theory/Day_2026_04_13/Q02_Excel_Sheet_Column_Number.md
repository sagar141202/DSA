# Excel Sheet Column Number

## Problem Statement
Given a string `s` which represents a column title in an Excel sheet, return its corresponding column number. The column title is in the range `[A, Z]` where `A` represents 1, `B` represents 2, and so on. The title can be a combination of characters, for example, `AB` represents 28. The input string will always be a valid column title.

## Approach
The problem can be solved by treating the column title as a base-26 number, where each character represents a digit in the base-26 system. We iterate through the string from left to right, and for each character, we calculate its corresponding value and add it to the total.

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
            // calculate the value of the current character
            int value = c - 'A' + 1;
            // add the value to the total
            result = result * 26 + value;
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
- The problem can be solved using a base-26 number system.
- We iterate through the string from left to right to calculate the total value.
- The time complexity is O(n), where n is the length of the input string.