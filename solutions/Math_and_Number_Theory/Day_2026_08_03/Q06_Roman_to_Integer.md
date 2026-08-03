# Roman to Integer

## Problem Statement
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M, which represent the numbers 1, 5, 10, 50, 100, 500 and 1000 respectively. The problem is to convert a Roman numeral to an integer. The input will be a string of Roman numerals and the output should be the corresponding integer. For example, the input "III" should return 3, "IV" should return 4, "IX" should return 9, "LVIII" should return 58, "MCMXCIV" should return 1994. The input string will only contain the characters I, V, X, L, C, D and M.

## Approach
The algorithm works by iterating over the input string from left to right. If the current numeral is less than the next one, we subtract its value, otherwise we add it. This way, we can correctly handle cases where a smaller numeral appears before a larger one, which means subtraction in Roman numerals.

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
    // Iterate over the input string
    for (int i = 0; i < s.length(); i++) {
        // If the current numeral is less than the next one, subtract its value
        if (i < s.length() - 1 && roman[s[i]] < roman[s[i + 1]]) {
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
- The key to solving this problem is to correctly handle cases where a smaller numeral appears before a larger one.
- Using a map to store the values of Roman numerals makes the code more readable and easier to understand.
- The time complexity is O(n), where n is the length of the input string, because we are iterating over the string once.