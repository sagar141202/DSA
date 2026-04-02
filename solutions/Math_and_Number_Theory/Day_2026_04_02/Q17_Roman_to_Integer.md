# Roman to Integer

## Problem Statement
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M, which represent the numbers 1, 5, 10, 50, 100, 500 and 1000 respectively. The problem requires writing a function that takes a string of Roman numerals as input and returns its integer equivalent. The function should handle valid Roman numerals and return the correct integer value. For example, the Roman numeral III represents the integer 3, and the Roman numeral IV represents the integer 4. The input string will only contain the characters I, V, X, L, C, D and M, and the function should return an integer value between 1 and 3999.

## Approach
The approach to solve this problem involves iterating over the input string and adding or subtracting the values of the Roman numerals based on their positions. If the current numeral is less than the next one, we subtract its value; otherwise, we add it. This is because in Roman numerals, a smaller numeral placed before a larger one means subtraction, while a smaller numeral placed after a larger one means addition.

## Complexity
- Time: O(n), where n is the length of the input string
- Space: O(1), as we only use a constant amount of space to store the values of the Roman numerals and the result

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int romanToInt(string s) {
    // Create a map to store the values of the Roman numerals
    unordered_map<char, int> romanValues = {
        {'I', 1}, {'V', 5}, {'X', 10}, {'L', 50},
        {'C', 100}, {'D', 500}, {'M', 1000}
    };

    int result = 0;
    // Iterate over the input string
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
- Use a map to store the values of the Roman numerals for efficient lookup
- Iterate over the input string and add or subtract the values of the Roman numerals based on their positions
- Handle the case where a smaller numeral is placed before a larger one to correctly calculate the integer equivalent of the Roman numeral.