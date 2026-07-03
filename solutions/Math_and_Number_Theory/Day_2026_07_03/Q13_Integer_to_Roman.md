# Integer to Roman

## Problem Statement
The problem requires converting an integer to its corresponding Roman numeral representation. The integer is within the range of 1 to 3999. The Roman numerals are represented using the following symbols: I (1), V (5), X (10), L (50), C (100), D (500), and M (1000). The constraints are that the input integer should be between 1 and 3999, and the output should be a string representing the Roman numeral. For example, the integer 4 should be converted to "IV", and the integer 9 should be converted to "IX".

## Approach
The algorithm uses a greedy approach to construct the Roman numeral representation. It starts with the largest possible Roman numeral and subtracts it from the number as many times as possible, then moves to the next smaller numeral. This process continues until the number becomes 0. The Roman numerals are appended to the result string in the order they are subtracted from the number.

## Complexity
- Time: O(log n)
- Space: O(log n)

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
- The greedy approach is suitable for this problem because the Roman numerals have a predictable and consistent pattern.
- The use of two arrays, one for values and one for symbols, simplifies the code and makes it easier to understand.
- The time complexity is O(log n) because the number of iterations is proportional to the number of digits in the input number.