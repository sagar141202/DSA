# Integer to Roman

## Problem Statement
The problem requires converting an integer to its corresponding Roman numeral representation. The integer is within the range of 1 to 3999. The Roman numerals are represented using seven symbols: I, V, X, L, C, D, and M, which correspond to the decimal values 1, 5, 10, 50, 100, 500, and 1000 respectively. For example, the integer 4 is represented as IV, 9 as IX, and 13 as XIII.

## Approach
The algorithm uses a greedy approach to construct the Roman numeral representation by subtracting the largest possible Roman numeral value from the integer until it becomes 0. This is done by using a vector of pairs to store the decimal and Roman numeral values.

## Complexity
- Time: O(1)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

string intToRoman(int num) {
    vector<pair<int, string>> values = {{1000, "M"}, {900, "CM"}, {500, "D"}, {400, "CD"}, {100, "C"}, {90, "XC"}, {50, "L"}, {40, "XL"}, {10, "X"}, {9, "IX"}, {5, "V"}, {4, "IV"}, {1, "I"}};
    string result = "";
    for (auto& value : values) {
        while (num >= value.first) {
            num -= value.first;
            result += value.second;
        }
    }
    return result;
}

int main() {
    int num = 2024;
    cout << intToRoman(num) << endl;
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
- The greedy approach is used to construct the Roman numeral representation.
- A vector of pairs is used to store the decimal and Roman numeral values.
- The time complexity is O(1) because the number of operations is constant, and the space complexity is also O(1) because the space used does not grow with the size of the input.