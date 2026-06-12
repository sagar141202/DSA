# Roman to Integer

## Problem Statement
Roman numerals are represented by seven different symbols: I, V, X, L, C, D, and M. Each symbol has a specific integer value: I = 1, V = 5, X = 10, L = 50, C = 100, D = 500, and M = 1000. The problem requires converting a Roman numeral to its corresponding integer value. For example, III is 3, IV is 4, IX is 9, LVIII is 58, and MCMXCIV is 1994. The input will be a string containing only Roman numerals, and the output should be the integer equivalent.

## Approach
The algorithm involves iterating over the input string and adding or subtracting the value of each Roman numeral based on whether it is less than or greater than the next numeral. This approach ensures that the correct integer value is calculated.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int romanToInt(string s) {
    // Create a map to store the integer values of Roman numerals
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
- Use a map to store the integer values of Roman numerals for efficient lookup.
- Iterate over the input string and apply the rules of Roman numerals to calculate the integer value.
- Handle cases where a smaller numeral appears before a larger one, indicating subtraction.