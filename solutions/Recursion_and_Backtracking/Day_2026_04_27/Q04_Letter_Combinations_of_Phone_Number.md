# Letter Combinations of Phone Number

## Problem Statement
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. The mapping of digits to letters is as follows: 
- 2: 'a', 'b', 'c'
- 3: 'd', 'e', 'f'
- 4: 'g', 'h', 'i'
- 5: 'j', 'k', 'l'
- 6: 'm', 'n', 'o'
- 7: 'p', 'q', 'r', 's'
- 8: 't', 'u', 'v'
- 9: 'w', 'x', 'y', 'z'
A number will always have at least one digit and may have up to 10 digits, and the digits will always be from 2-9. For example, if the input is "23", the output should be ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

## Approach
This problem can be solved using recursion and backtracking by iterating over each digit in the input string and exploring all possible letter combinations. The base case for the recursion is when the input string is empty, at which point we add the current combination to the result list. We use a mapping of digits to letters to generate the combinations.

## Complexity
- Time: O(4^n) where n is the number of digits in the input string, since in the worst case (when the input string contains only 7s and 9s), each digit can map to 4 letters.
- Space: O(n) for the recursion stack and O(4^n) for storing the result.

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<string> letterCombinations(string digits) {
        // Create a mapping of digits to letters
        unordered_map<char, string> phone = {
            {'2', "abc"},
            {'3', "def"},
            {'4', "ghi"},
            {'5', "jkl"},
            {'6', "mno"},
            {'7', "pqrs"},
            {'8', "tuv"},
            {'9', "wxyz"}
        };

        vector<string> output;
        if (digits.empty()) return output;

        // Recursive function to generate combinations
        function<void(int, string)> backtrack = [&](int index, string path) {
            if (index == digits.size()) {
                output.push_back(path);
                return;
            }
            for (char c : phone[digits[index]]) {
                backtrack(index + 1, path + c);
            }
        };

        backtrack(0, "");
        return output;
    }
};
```

## Test Cases
```
Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
```

## Key Takeaways
- The problem can be solved using recursion and backtracking by exploring all possible letter combinations for each digit in the input string.
- A mapping of digits to letters is used to generate the combinations.
- The time complexity is O(4^n) due to the worst-case scenario where each digit maps to 4 letters, and the space complexity is O(n) for the recursion stack and O(4^n) for storing the result.