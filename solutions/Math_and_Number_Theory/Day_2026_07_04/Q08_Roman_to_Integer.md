# Roman to Integer

## Problem Statement
Roman numerals are represented by seven different symbols: I, V, X, L, C, D, and M, which represent the numbers 1, 5, 10, 50, 100, 500, and 1000, respectively. The problem requires converting a Roman numeral to an integer. For example, "III" represents 3, "IV" represents 4, "IX" represents 9, "LVIII" represents 58, "MCMXCIV" represents 1994. The input will be a string containing only the characters I, V, X, L, C, D, and M. The string will be between 1 and 15 characters long.

## Approach
The solution involves iterating over the input string and adding or subtracting the value of each Roman numeral based on whether it is less than the next numeral. If the current numeral is less than the next one, it means that the current numeral should actually be subtracted from the total (because in Roman numerals, a smaller numeral placed before a larger one means subtraction).

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int romanToInt(string s) {
        unordered_map<char, int> roman = {{'I', 1}, {'V', 5}, {'X', 10}, {'L', 50}, {'C', 100}, {'D', 500}, {'M', 1000}};
        int result = 0;
        for (int i = 0; i < s.length() - 1; i++) {
            if (roman[s[i]] < roman[s[i + 1]]) {
                result -= roman[s[i]];
            } else {
                result += roman[s[i]];
            }
        }
        result += roman[s[s.length() - 1]];
        return result;
    }
};
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
- Understand the rules of Roman numerals and how to represent numbers using them.
- Recognize that the solution involves iterating over the input string and applying the rules of Roman numerals to calculate the integer value.
- Note that the time complexity is O(n), where n is the length of the input string, because we only need to iterate over the string once.