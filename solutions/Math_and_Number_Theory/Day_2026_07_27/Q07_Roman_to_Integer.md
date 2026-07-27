# Roman to Integer

## Problem Statement
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M, which represent the numbers 1, 5, 10, 50, 100, 500 and 1000 respectively. The problem is to convert a Roman numeral to an integer. For example, III is 3, IV is 4, IX is 9, LVIII is 58, MCMXCIV is 1994. The input will be a string containing only the characters I, V, X, L, C, D and M. The string will be between 1 and 15 characters long.

## Approach
The algorithm will iterate over the input string from left to right, adding the value of each numeral to a running total. If the current numeral is less than the next one, it will subtract the current numeral's value instead of adding it, because in Roman numerals, a smaller numeral placed before a larger one means subtraction.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int romanToInt(string s) {
    unordered_map<char, int> roman = {{'I', 1}, {'V', 5}, {'X', 10}, {'L', 50}, {'C', 100}, {'D', 500}, {'M', 1000}};
    int result = 0;
    for (int i = 0; i < s.length(); i++) {
        if (i > 0 && roman[s[i]] > roman[s[i - 1]]) {
            result += roman[s[i]] - 2 * roman[s[i - 1]];
        } else {
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
- Use an unordered map to store the values of Roman numerals for easy lookup.
- Iterate over the input string from left to right, keeping track of the running total.
- If the current numeral is less than the next one, subtract its value from the total instead of adding it.