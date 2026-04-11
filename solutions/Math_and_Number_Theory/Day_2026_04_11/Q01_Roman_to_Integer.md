# Roman to Integer

## Problem Statement
The problem requires converting a Roman numeral to an integer. Roman numerals are represented by seven different symbols: I, V, X, L, C, D, and M, which represent the numbers 1, 5, 10, 50, 100, 500, and 1000 respectively. The conversion should be done according to the standard Roman numeral rules, where a smaller numeral placed before a larger one means subtraction, and a smaller numeral placed after a larger one means addition. For example, IV represents 4 (5 - 1), and IX represents 9 (10 - 1). The input will be a string of Roman numerals, and the output should be the corresponding integer.

## Approach
The algorithm uses a hash map to store the values of the Roman numerals and then iterates through the input string, adding or subtracting the values based on the rules of Roman numerals. If the current numeral is less than the next one, it means subtraction, otherwise, it means addition.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int romanToInt(string s) {
    // Create a hash map to store the values of Roman numerals
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
    for (int i = 0; i < s.size(); i++) {
        // If the current numeral is less than the next one, subtract its value
        if (i < s.size() - 1 && roman[s[i]] < roman[s[i + 1]]) {
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
- Use a hash map to store the values of Roman numerals for efficient lookup.
- Iterate through the input string and apply the rules of Roman numerals to determine whether to add or subtract the value of each numeral.
- The time complexity is O(n), where n is the length of the input string, because we are iterating through the string once.