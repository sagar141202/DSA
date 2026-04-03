# Integer to Roman

## Problem Statement
The problem requires converting an integer to its corresponding Roman numeral representation. The Roman numerals use seven letters: I, V, X, L, C, D, and M, which represent the numbers 1, 5, 10, 50, 100, 500, and 1000 respectively. The conversion should follow the standard Roman numeral rules, where a smaller number in front of a larger one means subtraction, and the numbers should be arranged in descending order. For example, 4 is represented as IV (5-1), 9 is represented as IX (10-1), and 13 is represented as XIII (10+1+1+1). The input integer should be between 1 and 3999.

## Approach
The solution involves using a mapping of Roman numerals to their integer values and iterating through the mapping in descending order to construct the Roman numeral representation. We subtract the largest possible Roman numeral value from the number and append the corresponding numeral to the result, repeating this process until the number becomes 0.

## Complexity
- Time: O(1)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

string intToRoman(int num) {
    int values[] = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
    string roman[] = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
    string result = "";
    for (int i = 0; i < 13; i++) {
        while (num >= values[i]) {
            num -= values[i];
            result += roman[i];
        }
    }
    return result;
}
```

## Test Cases
```
Input: 3
Output: III
Input: 4
Output: IV
Input: 9
Output: IX
Input: 13
Output: XIII
Input: 44
Output: XLIV
Input: 1000
Output: M
```

## Key Takeaways
- Use a mapping of Roman numerals to their integer values for efficient conversion.
- Iterate through the mapping in descending order to construct the Roman numeral representation.
- Subtract the largest possible Roman numeral value from the number and append the corresponding numeral to the result, repeating this process until the number becomes 0.