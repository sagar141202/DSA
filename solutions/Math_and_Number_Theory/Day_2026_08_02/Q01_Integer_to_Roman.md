# Integer to Roman

## Problem Statement
The problem requires converting an integer to its corresponding Roman numeral representation. The integer can range from 1 to 3999. The Roman numerals use seven letters: I, V, X, L, C, D, and M, which represent the numbers 1, 5, 10, 50, 100, 500, and 1000, respectively. The conversion should follow the standard Roman numeral rules, where a smaller number placed before a larger number means subtraction, and a smaller number placed after a larger number means addition. For example, the integer 4 is represented as IV (5 - 1), and the integer 9 is represented as IX (10 - 1).

## Approach
The solution involves using a greedy approach to construct the Roman numeral representation by iterating through the integer from largest to smallest place value. We use an array to map the decimal values to their corresponding Roman numerals. The algorithm iterates through the array, subtracting the largest possible decimal value from the integer and appending the corresponding Roman numeral to the result.

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
- The greedy approach is suitable for this problem because the Roman numeral system has a consistent and predictable pattern.
- Using an array to map decimal values to Roman numerals simplifies the implementation and improves readability.
- The time complexity is O(1) because the number of iterations is constant, regardless of the input size.