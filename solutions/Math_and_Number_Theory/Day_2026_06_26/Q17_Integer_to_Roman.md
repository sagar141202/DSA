# Integer to Roman

## Problem Statement
The problem requires converting an integer to a Roman numeral. The integer is within the range of 1 to 3999. Roman numerals are represented by seven different symbols: I, V, X, L, C, D, and M, which represent the values 1, 5, 10, 50, 100, 500, and 1000 respectively. The conversion should follow the standard rules of Roman numerals, where a smaller number in front of a larger one means subtraction, and the same number repeated means addition.

## Approach
The algorithm uses a greedy approach, where it tries to subtract the largest possible Roman numeral value from the number at each step. This is done by maintaining a list of Roman numeral values and their corresponding symbols, and iterating over them from largest to smallest.

## Complexity
- Time: O(1)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

string intToRoman(int num) {
    int values[] = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
    string symbols[] = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
    string result = "";
    
    for (int i = 0; i < 13; i++) {
        while (num >= values[i]) {
            result += symbols[i];
            num -= values[i];
        }
    }
    
    return result;
}

int main() {
    int num;
    cout << "Enter a number: ";
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
- The greedy approach is suitable for this problem because the Roman numeral system is designed in a way that allows for efficient subtraction and addition of values.
- The use of two arrays, one for values and one for symbols, makes the code more readable and easier to maintain.
- The time complexity is O(1) because the number of iterations is constant, regardless of the input size.