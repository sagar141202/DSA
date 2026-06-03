# Roman to Integer

## Problem Statement
Roman numerals are represented by seven different symbols: I, V, X, L, C, D, and M. Each symbol has a specific integer value: I = 1, V = 5, X = 10, L = 50, C = 100, D = 500, and M = 1000. The problem requires converting a Roman numeral string to an integer. The input string will only contain the symbols I, V, X, L, C, D, and M, and the string will be valid, i.e., it will not contain any invalid Roman numerals. For example, "III" = 3, "IV" = 4, "IX" = 9, "LVIII" = 58, "MCMXCIV" = 1994.

## Approach
The solution involves iterating over the Roman numeral string and adding or subtracting the value of each symbol based on whether it is less than the next symbol. If the current symbol is less than the next one, we subtract its value; otherwise, we add it. This approach works because in Roman numerals, a smaller symbol placed before a larger one means subtraction.

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
        {'I', 1}, {'V', 5}, {'X', 10}, {'L', 50}, {'C', 100}, {'D', 500}, {'M', 1000}
    };

    int result = 0;
    // Iterate over the string
    for (int i = 0; i < s.length(); i++) {
        // If the current symbol is not the last one and its value is less than the next one
        if (i < s.length() - 1 && romanValues[s[i]] < romanValues[s[i + 1]]) {
            // Subtract the value of the current symbol
            result -= romanValues[s[i]];
        } else {
            // Add the value of the current symbol
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
- The solution uses a simple iteration over the string to calculate the integer value.
- A map is used to store the values of Roman numerals for easy lookup.
- The key to the solution is to compare each symbol with the next one to determine whether to add or subtract its value.