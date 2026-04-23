# Letter Combinations of Phone Number

## Problem Statement
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. The mapping of digits to letters is as follows: 
2 -> 'a', 'b', 'c'
3 -> 'd', 'e', 'f'
4 -> 'g', 'h', 'i'
5 -> 'j', 'k', 'l'
6 -> 'm', 'n', 'o'
7 -> 'p', 'q', 'r', 's'
8 -> 't', 'u', 'v'
9 -> 'w', 'x', 'y', 'z'
A number (e.g., "23") can represent multiple combinations (e.g., ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]).

## Approach
We will use recursion and backtracking to generate all possible combinations. The algorithm will iterate over each digit in the input string, and for each digit, it will recursively generate all possible combinations of the remaining digits.

## Complexity
- Time: O(4^n) where n is the length of the input string, as in the worst case (when the input string consists of only 7's and 9's), we have 4 possible letters for each digit.
- Space: O(n) for the recursion stack, as the maximum depth of the recursion tree is equal to the length of the input string.

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<string> letterCombinations(string digits) {
        vector<string> result;
        if (digits.empty()) return result;
        
        // mapping of digits to letters
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
        
        // recursive function to generate combinations
        function<void(int, string)> backtrack = [&](int index, string path) {
            if (index == digits.size()) {
                result.push_back(path);
                return;
            }
            
            for (char c : phone[digits[index]]) {
                backtrack(index + 1, path + c);
            }
        };
        
        backtrack(0, "");
        return result;
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
- Use recursion and backtracking to generate all possible combinations of letters that a phone number could represent.
- Use an unordered map to store the mapping of digits to letters for easy lookup.
- The time complexity is O(4^n) due to the worst-case scenario where the input string consists of only 7's and 9's.