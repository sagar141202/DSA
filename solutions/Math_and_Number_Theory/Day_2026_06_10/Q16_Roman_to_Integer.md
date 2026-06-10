# Roman to Integer

## Problem Statement
Roman numerals are represented by seven different symbols: I, V, X, L, C, D, and M. Each symbol represents a different integer value: I = 1, V = 5, X = 10, L = 50, C = 100, D = 500, and M = 1000. The problem requires writing a function that takes a string of Roman numerals as input and returns the integer equivalent. The input string will only contain the symbols I, V, X, L, C, D, and M, and the function should handle cases where the input string is empty or null. For example, the Roman numeral "III" represents the integer 3, "IV" represents 4, and "IX" represents 9.

## Approach
The approach to solve this problem is to use a dictionary to map Roman numerals to their integer equivalents and then iterate over the input string, adding or subtracting the values based on the rules of Roman numerals. If the current numeral is less than the next one, subtract its value; otherwise, add it.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int romanToInt(string s) {
    // Create a dictionary to map Roman numerals to their integer equivalents
    unordered_map<char, int> romanNumerals = {
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
        if (i < s.length() - 1 && romanNumerals[s[i]] < romanNumerals[s[i + 1]]) {
            result -= romanNumerals[s[i]];
        } else {
            // Otherwise, add its value
            result += romanNumerals[s[i]];
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
- Use a dictionary to map Roman numerals to their integer equivalents for efficient lookup.
- Iterate over the input string, applying the rules of Roman numerals to determine whether to add or subtract the value of each numeral.
- Handle edge cases, such as an empty or null input string, to ensure the function is robust.