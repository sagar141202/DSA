# Roman to Integer

## Problem Statement
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M, which represent the numbers 1, 5, 10, 50, 100, 500 and 1000 respectively. The problem requires converting a Roman numeral to an integer. For example, III is 3, IV is 4, IX is 9, LVIII is 58, MCMXCIV is 1994. The input will be a string of Roman numerals and the output should be the integer equivalent. The input string will be between 1 and 15 characters long and will only contain the characters I, V, X, L, C, D and M.

## Approach
The approach to solve this problem is to use a hashmap to store the values of the Roman numerals and then iterate over the input string, adding or subtracting the values based on the rules of Roman numerals. If the current numeral is less than the next one, we subtract its value, otherwise we add it.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int romanToInt(string s) {
    // Create a hashmap to store the values of the Roman numerals
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
- Use a hashmap to store the values of the Roman numerals for efficient lookup.
- Iterate over the input string, adding or subtracting the values based on the rules of Roman numerals.
- If the current numeral is less than the next one, subtract its value, otherwise add it.