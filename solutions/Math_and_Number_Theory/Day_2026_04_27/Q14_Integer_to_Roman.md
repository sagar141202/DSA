# Integer to Roman

## Problem Statement
The problem requires converting an integer to its corresponding Roman numeral representation. The integer is within the range of 1 to 3999. The Roman numerals are represented using seven symbols: I, V, X, L, C, D, and M, which represent the values 1, 5, 10, 50, 100, 500, and 1000 respectively. The conversion should follow the standard rules of Roman numerals, where a smaller numeral placed before a larger one means subtraction, and a smaller numeral placed after a larger one means addition. For example, the integer 4 is represented as IV (5 - 1), and the integer 9 is represented as IX (10 - 1).

## Approach
The algorithm uses a greedy approach to construct the Roman numeral representation by iterating through the integer value from largest to smallest and appending the corresponding Roman numerals. This approach ensures that the resulting Roman numeral is the most efficient representation of the given integer. The solution uses a predefined mapping of integer values to their corresponding Roman numerals.

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
            result += roman[i];
            num -= values[i];
        }
    }
    return result;
}

int main() {
    int num = 2024;
    cout << "Roman numeral representation of " << num << ": " << intToRoman(num) << endl;
    return 0;
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
- The solution uses a greedy approach to construct the Roman numeral representation.
- A predefined mapping of integer values to their corresponding Roman numerals is used.
- The time complexity is O(1) because the number of iterations is constant, regardless of the input size.