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
A number could represent multiple letters and each letter can only be used once in a combination. For example, given the input "23", the output should be ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

## Approach
The problem can be solved using recursion and backtracking. We create a mapping of digits to their corresponding letters and then use a recursive function to generate all possible combinations. The base case for the recursion is when the input string is empty, at which point we add the current combination to the result.

## Complexity
- Time: O(4^n) where n is the length of the input string, since each digit can have at most 4 possible letters.
- Space: O(n) for the recursion stack.

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<string> letterCombinations(string digits) {
        vector<string> result;
        if (digits.empty()) return result;
        
        // Mapping of digits to letters
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
        
        // Recursive function to generate combinations
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
- Use recursion and backtracking to generate all possible combinations.
- Create a mapping of digits to letters to simplify the problem.
- Use a recursive function to generate combinations and add them to the result when the base case is reached.