# Integer to Roman

## Problem Statement
The problem requires converting an integer to a Roman numeral. The integer is in the range [1, 3999]. The Roman numerals use seven symbols: I, V, X, L, C, D, and M, which represent 1, 5, 10, 50, 100, 500, and 1000 respectively. The Roman numeral system is based on a set of rules where a smaller number in front of a larger number means subtraction, otherwise, it means addition. For example, IV represents 4 (5 - 1), IX represents 9 (10 - 1), and so on. The goal is to write a function that takes an integer as input and returns the corresponding Roman numeral as a string.

## Approach
We can solve this problem by using a greedy approach, where we subtract the largest possible Roman numeral value from the integer at each step. This approach ensures that we use the minimum number of Roman numerals to represent the integer. We will use a map or an array to store the Roman numerals and their corresponding integer values.

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
- The greedy approach is suitable for this problem because it allows us to use the minimum number of Roman numerals to represent the integer.
- We can use an array or a map to store the Roman numerals and their corresponding integer values, making it easy to access and compare them.
- The time complexity is O(1) because we are using a fixed number of iterations to convert the integer to a Roman numeral, regardless of the input size.