# Roman to Integer

## Problem Statement
Roman numerals are represented by seven different symbols: I, V, X, L, C, D, and M. Each symbol has a specific integer value: I = 1, V = 5, X = 10, L = 50, C = 100, D = 500, and M = 1000. The problem requires converting a Roman numeral to its corresponding integer value. The input will be a string containing only the characters I, V, X, L, C, D, and M. The string will be between 1 and 15 characters long. For example, the Roman numeral "III" corresponds to the integer 3, and "IV" corresponds to 4.

## Approach
The solution involves iterating through the input string and adding or subtracting the value of each Roman numeral based on whether it is less than or greater than the next numeral. If the current numeral is less than the next one, its value is subtracted; otherwise, it is added.

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
        // If the current numeral is less than the next one, subtract its value
        if (i < s.length() - 1 && romanValues[s[i]] < romanValues[s[i + 1]]) {
            result -= romanValues[s[i]];
        } else {
            // Otherwise, add its value
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
- Use a map to store the values of Roman numerals for efficient lookup.
- Iterate through the input string, comparing each numeral with the next one to determine whether to add or subtract its value.
- Handle the edge case where the input string has only one character.