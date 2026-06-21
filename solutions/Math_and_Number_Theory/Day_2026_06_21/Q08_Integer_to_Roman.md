# Integer to Roman

## Problem Statement
The problem requires converting an integer to its corresponding Roman numeral representation. The integer can range from 1 to 3999. The Roman numerals use seven letters: I, V, X, L, C, D, and M, which represent the numbers 1, 5, 10, 50, 100, 500, and 1000, respectively. The goal is to write a function that takes an integer as input and returns its Roman numeral equivalent. For example, the integer 4 is represented as IV, 9 as IX, 13 as XIII, 44 as XLIV, and 1000 as M.

## Approach
The algorithm involves using a map to store the decimal and Roman numeral values, then iterating over the map to construct the Roman numeral representation. We start with the largest decimal value and subtract it from the input number as many times as possible, appending the corresponding Roman numeral to the result each time.

## Complexity
- Time: O(1)
- Space: O(1)

## C++ Solution
```cpp
#include <string>
#include <vector>
#include <algorithm>

class Solution {
public:
    string intToRoman(int num) {
        vector<int> values = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
        vector<string> romanLiterals = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
        
        string result = "";
        for (int i = 0; i < values.size(); i++) {
            while (num >= values[i]) {
                result += romanLiterals[i];
                num -= values[i];
            }
        }
        return result;
    }
};
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
- The problem can be solved using a greedy approach, where we always choose the largest possible Roman numeral value that does not exceed the remaining number.
- We use a vector of decimal values and their corresponding Roman numeral literals to simplify the construction of the result.
- The time complexity is O(1) because the number of iterations is constant and does not depend on the input size.