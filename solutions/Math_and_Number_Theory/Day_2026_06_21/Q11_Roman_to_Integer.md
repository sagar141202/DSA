# Roman to Integer

## Problem Statement
Roman numerals are represented by seven different symbols: I, V, X, L, C, D, and M, which represent the numbers 1, 5, 10, 50, 100, 500, and 1000 respectively. The task is to convert a Roman numeral to an integer. The input will be a string containing only the characters I, V, X, L, C, D, and M. The string will be between 1 and 15 characters long. For example, "III" represents 3, "IV" represents 4, and "IX" represents 9.

## Approach
The algorithm works by iterating over the input string from left to right, adding the value of each numeral to a running total. If the current numeral is less than the next one, we subtract its value instead, because in Roman numerals, a smaller numeral placed before a larger one means subtraction. This approach ensures that the conversion is done correctly according to the rules of Roman numerals.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int romanToInt(string s) {
    // Create a map to store the values of Roman numerals
    unordered_map<char, int> roman_values = {
        {'I', 1},
        {'V', 5},
        {'X', 10},
        {'L', 50},
        {'C', 100},
        {'D', 500},
        {'M', 1000}
    };

    int result = 0;
    for (int i = 0; i < s.length(); i++) {
        // If the current numeral is less than the next one, subtract its value
        if (i < s.length() - 1 && roman_values[s[i]] < roman_values[s[i + 1]]) {
            result -= roman_values[s[i]];
        } else {
            // Otherwise, add its value
            result += roman_values[s[i]];
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
- The key to solving this problem is understanding the rules of Roman numerals, especially the rule about subtracting a smaller numeral's value when it appears before a larger one.
- Using a map to store the values of Roman numerals simplifies the code and makes it more readable.
- The time complexity is O(n), where n is the length of the input string, because we make a single pass over the string.