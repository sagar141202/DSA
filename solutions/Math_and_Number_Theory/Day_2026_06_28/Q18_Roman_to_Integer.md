# Roman to Integer

## Problem Statement
Roman numerals are represented by seven different symbols: I, V, X, L, C, D, and M, which represent the numbers 1, 5, 10, 50, 100, 500, and 1000, respectively. The integer value of a Roman numeral is determined by adding the values of its symbols, with the exception that a smaller symbol placed before a larger symbol means subtraction. For example, IV represents 4 (5 - 1) and IX represents 9 (10 - 1). Given a Roman numeral as a string, convert it to an integer. The input will be a string containing only the characters I, V, X, L, C, D, and M. The string will not be empty and will contain at most 15 characters. For example, input "III" should return 3, input "IV" should return 4, and input "IX" should return 9.

## Approach
The approach to solve this problem is to iterate over the string from left to right, adding the value of the current symbol to the total. If the current symbol is less than the next symbol, subtract its value instead. This way, we correctly handle cases where a smaller symbol appears before a larger one. We use a map to store the values of the Roman numerals for easy lookup.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int romanToInt(string s) {
    // Create a map to store the values of Roman numerals
    unordered_map<char, int> roman = {
        {'I', 1},
        {'V', 5},
        {'X', 10},
        {'L', 50},
        {'C', 100},
        {'D', 500},
        {'M', 1000}
    };

    int result = 0;
    // Iterate over the string
    for (int i = 0; i < s.length(); i++) {
        // If the current symbol is less than the next symbol, subtract its value
        if (i + 1 < s.length() && roman[s[i]] < roman[s[i + 1]]) {
            result -= roman[s[i]];
        } else {
            // Otherwise, add its value
            result += roman[s[i]];
        }
    }
    return result;
}
```

## Test Cases
```
Input: "III"
Output: 3
Input: "IV"
Output: 4
Input: "IX"
Output: 9
Input: "LVIII"
Output: 58
Input: "MCMXCIV"
Output: 1994
```

## Key Takeaways
- Use a map to store the values of Roman numerals for easy lookup.
- Iterate over the string from left to right, adding or subtracting the value of the current symbol based on whether it's less than the next symbol.
- Handle edge cases where the input string is empty or contains more than 15 characters.