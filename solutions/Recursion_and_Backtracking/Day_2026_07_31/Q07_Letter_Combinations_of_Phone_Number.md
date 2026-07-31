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
A number can have any number of digits, and each digit can have any number of letters associated with it. The solution should be able to handle numbers of any length and return all possible combinations. For example, given the input "23", the output should be ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

## Approach
The problem can be solved using recursion and backtracking, where each digit is recursively replaced by its corresponding letters. We use a dictionary to map each digit to its corresponding letters, and then recursively generate all possible combinations. The base case for the recursion is when the input string is empty, at which point we add the current combination to the result list.

## Complexity
- Time: O(4^n) where n is the number of digits in the input string, as in the worst case, each digit can have 4 corresponding letters.
- Space: O(n) for the recursion stack.

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<string> letterCombinations(string digits) {
        // Dictionary to map digits to letters
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
            if (path.size() == digits.size()) {
                output.push_back(path);
                return;
            }

            // Get the letters corresponding to the current digit
            for (char c : phone[digits[index]]) {
                // Recursively generate combinations for the next digit
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
Input: ""
Output: []
Input: "2"
Output: ["a", "b", "c"]
```

## Key Takeaways
- The problem can be solved using recursion and backtracking, where each digit is recursively replaced by its corresponding letters.
- A dictionary is used to map each digit to its corresponding letters, making it easy to generate all possible combinations.
- The time complexity is O(4^n) due to the worst-case scenario where each digit has 4 corresponding letters.