# Integer to Roman

## Problem Statement
The problem requires converting an integer to its Roman numeral representation. The integer is in the range [1, 3999]. The Roman numerals are represented using seven symbols: I, V, X, L, C, D, and M, which represent the numbers 1, 5, 10, 50, 100, 500, and 1000 respectively. The constraints are that the input integer will be between 1 and 3999, and the output should be a string representing the Roman numeral equivalent of the input integer. For example, the integer 3 is represented as "III" and 4 is represented as "IV".

## Approach
The algorithm involves using a mapping of integers to their corresponding Roman numerals and subtracting the largest possible Roman numeral value from the number until it becomes 0. This approach ensures that the resulting Roman numeral is the most efficient representation of the input integer.

## Complexity
- Time: O(1)
- Space: O(1)

## C++ Solution
```cpp
#include <string>
using namespace std;

string intToRoman(int num) {
    int values[] = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
    string symbols[] = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
    string result = "";
    for (int i = 0; i < 13; i++) {
        while (num >= values[i]) {
            num -= values[i];
            result += symbols[i];
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
- Use a mapping of integers to Roman numerals for efficient conversion.
- Subtract the largest possible Roman numeral value from the number until it becomes 0.
- The resulting Roman numeral is the most efficient representation of the input integer.