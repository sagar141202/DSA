# Integer to Roman

## Problem Statement
The problem requires converting an integer to its corresponding Roman numeral representation. The input integer will be in the range [1, 3999]. The Roman numerals use seven symbols: I, V, X, L, C, D, and M, representing 1, 5, 10, 50, 100, 500, and 1000 respectively. The Roman numeral system is based on a set of rules where a smaller number in front of a larger one means subtraction, otherwise, it means addition. For example, IV represents 4 (5 - 1), and VI represents 6 (5 + 1).

## Approach
The algorithm uses a greedy approach by iterating over the Roman numerals from largest to smallest and subtracting the largest possible Roman numeral value from the integer until it becomes 0. This ensures the resulting Roman numeral representation is the most efficient.

## Complexity
- Time: O(1)
- Space: O(1)

## C++ Solution
```cpp
#include <string>
using namespace std;

string intToRoman(int num) {
    int values[] = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
    string roman[] = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
    string result = "";
    
    for (int i = 0; i < 13; i++) {
        while (num >= values[i]) {
            result += roman[i];
            num -= values[i];
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
- The greedy approach ensures the most efficient Roman numeral representation.
- The use of two arrays, one for values and one for corresponding Roman numerals, simplifies the conversion process.
- The algorithm iterates over the values and Roman numerals in descending order to prioritize larger values.