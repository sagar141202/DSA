# Integer to Roman

## Problem Statement
The problem requires converting an integer to its corresponding Roman numeral representation. The integer is within the range of 1 to 3999. The Roman numerals use seven letters: I, V, X, L, C, D, and M, which represent the numbers 1, 5, 10, 50, 100, 500, and 1000, respectively. The task is to write a function that takes an integer as input and returns its Roman numeral equivalent. For example, the integer 4 is represented as IV, 9 as IX, 13 as XIII, 44 as XLIV, and 1000 as M.

## Approach
The algorithm uses a greedy approach to construct the Roman numeral representation. It iterates over a list of Roman numerals and their corresponding integer values in descending order, subtracting the largest possible value from the input integer and appending the corresponding Roman numeral to the result.

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
- The greedy approach is suitable for this problem because the Roman numeral system has a consistent and predictable structure.
- Using a list of predefined Roman numerals and their corresponding integer values simplifies the implementation and improves readability.
- The time complexity is O(1) because the number of iterations is constant and does not depend on the input size.