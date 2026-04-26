# Roman to Integer

## Problem Statement
Roman numerals are represented by seven different symbols: I, V, X, L, C, D, and M. Each symbol has a specific integer value: I = 1, V = 5, X = 10, L = 50, C = 100, D = 500, and M = 1000. The problem requires converting a Roman numeral to an integer. The input will be a string containing only the characters I, V, X, L, C, D, and M. The string will be between 1 and 15 characters long. For example, the Roman numeral "III" represents the integer 3, and "IV" represents the integer 4.

## Approach
The approach involves iterating over the input string and adding or subtracting the value of each symbol based on whether it is less than the next symbol. If the current symbol is less than the next symbol, its value is subtracted from the total; otherwise, its value is added. This is because in Roman numerals, a smaller symbol placed before a larger symbol means subtraction.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int romanToInt(string s) {
    // Create a map to store the values of Roman numerals
    unordered_map<char, int> romanValues = {
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
        // If the current symbol is not the last symbol and its value is less than the next symbol's value
        if (i < s.length() - 1 && romanValues[s[i]] < romanValues[s[i + 1]]) {
            // Subtract the value of the current symbol from the result
            result -= romanValues[s[i]];
        } else {
            // Add the value of the current symbol to the result
            result += romanValues[s[i]];
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
- The solution uses a map to store the values of Roman numerals for efficient lookup.
- It iterates over the input string, adding or subtracting the value of each symbol based on whether it is less than the next symbol.
- The time complexity is O(n), where n is the length of the input string, and the space complexity is O(1) since the map has a constant size.