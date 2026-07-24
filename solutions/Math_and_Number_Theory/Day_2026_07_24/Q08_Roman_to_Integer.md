# Roman to Integer

## Problem Statement
Roman numerals are represented by seven different symbols: I, V, X, L, C, D, and M, which represent the numbers 1, 5, 10, 50, 100, 500, and 1000, respectively. The problem requires converting a Roman numeral to an integer. The input is a string containing a valid Roman numeral, and the output should be the corresponding integer value. For example, "III" should return 3, "IV" should return 4, and "IX" should return 9. The constraints are that the input string will only contain the characters I, V, X, L, C, D, and M, and the length of the string will be between 1 and 15.

## Approach
The algorithm uses a hash map to store the values of the Roman numerals and then iterates over the input string, adding or subtracting the values based on whether the current numeral is less than the next one. This approach allows for efficient conversion of Roman numerals to integers in a single pass.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int romanToInt(string s) {
    // Create a hash map to store the values of the Roman numerals
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
- Use a hash map to store the values of the Roman numerals for efficient lookup.
- Iterate over the input string and add or subtract the values based on whether the current numeral is less than the next one.
- The time complexity is O(n), where n is the length of the input string, and the space complexity is O(1) since the hash map has a fixed size.