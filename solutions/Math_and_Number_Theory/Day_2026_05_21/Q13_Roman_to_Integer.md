# Roman to Integer

## Problem Statement
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M, which represent the numbers 1, 5, 10, 50, 100, 500 and 1000 respectively. The problem requires converting a Roman numeral to an integer. For example, IV represents 4, IX represents 9, LVIII represents 58, MCMXCIV represents 1994. The input will be a string of Roman numerals and the output should be the corresponding integer. The string will only contain the characters I, V, X, L, C, D and M, and will be between 1 and 15 characters long.

## Approach
The approach to this problem is to create a mapping of Roman numerals to their integer values and then iterate over the input string. If the current numeral is less than the next one, subtract its value, otherwise add it. This way, we can handle cases like IV (4) and IX (9) correctly.

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
        if (i < s.length() - 1 && romanMap[s[i]] < romanMap[s[i + 1]]) {
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
- Create a mapping of Roman numerals to their integer values for easy lookup
- Iterate over the input string and compare each numeral with the next one to handle cases like IV and IX correctly
- Use a variable to keep track of the result and update it accordingly based on the comparison of the current and next numerals.