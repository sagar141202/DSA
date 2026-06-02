# Excel Sheet Column Number

## Problem Statement
Given a string `s` representing the column title of an Excel sheet, return its corresponding column number. The column title is in the range `[A, Z]` where `A` represents `1`, `B` represents `2`, and so on. The title can contain multiple characters, and the column number can be greater than `26`. For example, `AB` corresponds to `(1 * 26) + 2 = 28`, and `ZY` corresponds to `(26 * 26) + 26 = 702`. The input string `s` will only contain uppercase letters.

## Approach
The algorithm iterates over the input string from left to right, calculating the column number by multiplying the current number by `26` and adding the value of the current character. The value of the character is determined by subtracting the ASCII value of `A` (64) from the ASCII value of the character and adding `1`. This approach takes advantage of the fact that Excel sheet column titles are base-26 numbers.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int titleToNumber(string s) {
        int result = 0;
        for (char c : s) {
            // calculate the value of the current character
            int value = c - 'A' + 1;
            // multiply the current number by 26 and add the value of the current character
            result = result * 26 + value;
        }
        return result;
    }
};
```

## Test Cases
```
Input: "A"
Output: 1
Input: "AB"
Output: 28
Input: "ZY"
Output: 702
```

## Key Takeaways
- The Excel sheet column title can be treated as a base-26 number.
- The value of each character can be calculated by subtracting the ASCII value of `A` (64) from the ASCII value of the character and adding `1`.
- The algorithm has a time complexity of O(n), where n is the length of the input string.