# Integer to Roman

## Problem Statement
The problem requires converting an integer to its corresponding Roman numeral representation. The integer is within the range of 1 to 3999. Roman numerals use seven symbols: I, V, X, L, C, D, and M, which represent the numbers 1, 5, 10, 50, 100, 500, and 1000, respectively. The Roman numeral system is based on a set of rules where each digit in the number is replaced by its corresponding Roman numeral symbol. For example, the number 4 is represented as IV, which is 5 - 1, and the number 9 is represented as IX, which is 10 - 1.

## Approach
The approach to solve this problem involves using a mapping of decimal values to their corresponding Roman numerals and then iterating over the decimal values in descending order to construct the Roman numeral representation. This is done by repeatedly subtracting the largest possible decimal value from the number and appending its corresponding Roman numeral symbol to the result.

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
- The solution uses a mapping of decimal values to their corresponding Roman numerals.
- It iterates over the decimal values in descending order to construct the Roman numeral representation.
- The time complexity is O(1) because the number of iterations is constant, and the space complexity is O(1) because the space used does not change with the size of the input.