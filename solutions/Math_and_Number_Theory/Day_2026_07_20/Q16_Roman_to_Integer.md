# Roman to Integer

## Problem Statement
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M, which represent the numbers 1, 5, 10, 50, 100, 500 and 1000 respectively. The problem requires us to write a function that takes a string of Roman numerals as input and returns its integer equivalent. For example, the Roman numeral "III" represents the integer 3, and "IV" represents the integer 4. The input string will only contain the characters I, V, X, L, C, D and M, and the length of the string will not exceed 15 characters.

## Approach
The algorithm uses a hash map to store the values of the Roman numerals and then iterates over the input string, adding or subtracting the values based on the rules of Roman numerals. If the current numeral is less than the next one, we subtract its value, otherwise we add it.

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
- Use a hash map to store the values of the Roman numerals for efficient lookup.
- Iterate over the input string and apply the rules of Roman numerals to calculate the integer equivalent.
- Handle the cases where a smaller numeral appears before a larger one, which means subtraction.