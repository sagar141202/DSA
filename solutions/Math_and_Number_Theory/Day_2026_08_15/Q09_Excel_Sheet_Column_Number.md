# Excel Sheet Column Number

## Problem Statement
Given a string `s` representing the column title of an Excel sheet, return its corresponding column number. The column title is in the range `[A, Z]` where `A` represents the first column, `B` represents the second column, and so on. The column title can contain multiple characters, for example, "AA" represents the 27th column, "AB" represents the 28th column, and "AZ" represents the 52nd column. The input string `s` will always be a valid Excel column title.

## Approach
The problem can be solved by treating the Excel column title as a base-26 number, where each character in the string represents a digit in the base-26 system. We can then convert this base-26 number to a decimal number, which represents the column number. The algorithm involves iterating over the input string from left to right and calculating the column number based on the position and value of each character.

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
Input: "AZ"
Output: 52
Input: "AA"
Output: 27
```

## Key Takeaways
- The problem can be solved by treating the Excel column title as a base-26 number.
- The time complexity of the solution is O(n), where n is the length of the input string.
- The space complexity of the solution is O(1), as it only uses a constant amount of space to store the result and temporary variables.