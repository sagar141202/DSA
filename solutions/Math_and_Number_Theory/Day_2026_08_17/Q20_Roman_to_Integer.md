# Roman to Integer

## Problem Statement
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M, which represent the numbers 1, 5, 10, 50, 100, 500 and 1000 respectively. The problem requires converting a Roman numeral to an integer. The input will be a string containing only the characters I, V, X, L, C, D and M. The string will be between 1 and 15 characters long. For example, the Roman numeral "III" represents the integer 3, and "IV" represents the integer 4. The Roman numeral "MMXXI" represents the integer 2021.

## Approach
The algorithm uses a dictionary to map Roman numerals to their integer values and then iterates over the input string, adding or subtracting the values based on the rules of Roman numerals. If the current numeral is less than the next one, it means that the current numeral should actually be subtracted from the total (because in Roman numerals, a smaller numeral placed before a larger one means subtraction).

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int romanToInt(string s) {
    // Create a dictionary to map Roman numerals to their integer values
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
        if (i + 1 < s.length() && roman[s[i]] < roman[s[i + 1]]) {
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
Input: "MMXXI"
Output: 2021
```

## Key Takeaways
- Use a dictionary to map Roman numerals to their integer values for efficient lookups.
- Iterate over the input string and apply the rules of Roman numerals to calculate the integer value.
- Handle cases where a smaller numeral appears before a larger one by subtracting its value.