# Excel Sheet Column Number

## Problem Statement
The problem requires converting Excel sheet column titles to their corresponding column numbers. The column titles are in the format of uppercase English letters, where 'A' represents the first column, 'B' represents the second column, and so on. The task is to write a function that takes a string representing the column title as input and returns the corresponding column number. For example, the input "A" should return 1, "B" should return 2, "Z" should return 26, "AA" should return 27, and "AZ" should return 52.

## Approach
The algorithm involves treating the Excel column title as a base-26 number, where 'A' represents 1, 'B' represents 2, and so on. The function iterates over the input string from left to right, calculating the column number based on the position and value of each character. The result is the sum of the values of all characters, taking into account the base-26 representation.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <string>

class Solution {
public:
    int titleToNumber(std::string s) {
        int result = 0;
        for (char c : s) {
            // Calculate the value of the current character and add it to the result
            result = result * 26 + (c - 'A' + 1);
        }
        return result;
    }
};
```

## Test Cases
```
Input: "A"
Output: 1
Input: "Z"
Output: 26
Input: "AA"
Output: 27
Input: "AZ"
Output: 52
```

## Key Takeaways
- The problem can be solved by treating the Excel column title as a base-26 number.
- The function iterates over the input string, calculating the column number based on the position and value of each character.
- The time complexity is O(n), where n is the length of the input string, and the space complexity is O(1), as only a constant amount of space is used.