# Integer to Roman

## Problem Statement
The problem requires converting an integer to a Roman numeral. The integer is within the range of 1 to 3999. Roman numerals are represented by seven different symbols: I, V, X, L, C, D, and M, which represent the numbers 1, 5, 10, 50, 100, 500, and 1000 respectively. The conversion should be done in a way that the resulting Roman numeral is as short as possible.

## Approach
The algorithm uses a greedy approach to construct the Roman numeral by iterating over the given integer from largest to smallest values, subtracting the largest possible Roman numeral value at each step.

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
    int num;
    cout << "Enter an integer: ";
    cin >> num;
    cout << "Roman numeral: " << intToRoman(num) << endl;
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
- The greedy approach is used to ensure the resulting Roman numeral is as short as possible.
- The algorithm iterates over the given integer from largest to smallest values.
- The use of arrays for Roman numeral values and symbols simplifies the implementation.