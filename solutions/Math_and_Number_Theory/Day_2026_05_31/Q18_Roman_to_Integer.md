# Roman to Integer

## Problem Statement
Roman numerals are represented by seven different symbols: I, V, X, L, C, D, and M. Each symbol has a specific integer value: I = 1, V = 5, X = 10, L = 50, C = 100, D = 500, and M = 1000. The problem requires converting a Roman numeral to an integer. The input is a string of Roman numerals, and the output is the corresponding integer value. For example, the Roman numeral "III" corresponds to the integer 3, and "IV" corresponds to 4. The constraints are that the input string only contains the seven Roman numeral symbols and that the input is a valid Roman numeral.

## Approach
The approach is to create a mapping of Roman numerals to their integer values and then iterate over the input string. If the current numeral is less than the next one, subtract its value; otherwise, add its value. This solution works because in Roman numerals, a smaller numeral placed before a larger one means subtraction.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int romanToInt(string s) {
    // Create a mapping of Roman numerals to their integer values
    unordered_map<char, int> romanMap = {
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
        if (i + 1 < s.length() && romanMap[s[i]] < romanMap[s[i + 1]]) {
            result -= romanMap[s[i]];
        } else {
            // Otherwise, add its value
            result += romanMap[s[i]];
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
- Use an unordered_map to store the mapping of Roman numerals to their integer values for efficient lookups.
- Iterate over the input string and apply the rules of Roman numerals to calculate the integer value.
- Handle edge cases where the input string is empty or contains invalid characters.