# Excel Sheet Column Number

## Problem Statement
Given a string `s` representing the column title of an Excel sheet, return its corresponding column number. The title is a string of uppercase letters, where 'A' represents the first column, 'B' represents the second column, and so on. The column number is calculated based on the base-26 number system, where 'A' is 1, 'B' is 2, and 'Z' is 26. For example, the column title "A" corresponds to column number 1, "B" corresponds to column number 2, "Z" corresponds to column number 26, "AA" corresponds to column number 27, and "AZ" corresponds to column number 52.

## Approach
The solution involves treating the Excel column title as a base-26 number, where each digit is represented by a letter from 'A' to 'Z'. We can then convert this base-26 number to a decimal number. The algorithm iterates over the input string from left to right, calculating the decimal value of each digit based on its position and the base-26 system.

## Complexity
- Time: O(n), where n is the length of the input string
- Space: O(1), as the space used does not grow with the size of the input string

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int titleToNumber(string s) {
        int result = 0;
        for (char c : s) {
            // Calculate the decimal value of the current digit
            int digit = c - 'A' + 1;
            // Update the result by shifting the current result to the left (multiplying by 26)
            // and adding the decimal value of the current digit
            result = result * 26 + digit;
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
- The Excel column title can be treated as a base-26 number, where each digit is represented by a letter from 'A' to 'Z'.
- The decimal value of each digit can be calculated based on its position in the input string and the base-26 system.
- The time complexity of the solution is O(n), where n is the length of the input string, as we only need to iterate over the input string once.