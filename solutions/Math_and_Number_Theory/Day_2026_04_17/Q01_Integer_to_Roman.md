# Integer to Roman

## Problem Statement
The problem requires converting an integer to its corresponding Roman numeral representation. The integer is within the range of 1 to 3999. The Roman numerals use seven symbols: I, V, X, L, C, D, and M, which represent the numbers 1, 5, 10, 50, 100, 500, and 1000, respectively. The conversion should follow the standard Roman numeral rules, where a smaller number in front of a larger one means subtraction, and the same number repeated means addition.

## Approach
The algorithm involves looping through the integer from largest to smallest Roman numeral values, subtracting the value from the integer, and appending the corresponding Roman numeral to the result as many times as possible. This process continues until the integer becomes 0.

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
- Use a loop to iterate through the Roman numeral values and symbols in descending order.
- Use a while loop to subtract the current Roman numeral value from the integer and append the corresponding symbol to the result as many times as possible.
- The solution has a constant time complexity because the loop iterates through a fixed number of Roman numeral values.