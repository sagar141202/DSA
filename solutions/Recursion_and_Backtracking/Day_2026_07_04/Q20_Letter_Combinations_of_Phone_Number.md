# Letter Combinations of Phone Number

## Problem Statement
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. The mapping of digits to letters is as follows: 
2 -> 'a', 'b', 'c', 
3 -> 'd', 'e', 'f', 
4 -> 'g', 'h', 'i', 
5 -> 'j', 'k', 'l', 
6 -> 'm', 'n', 'o', 
7 -> 'p', 'q', 'r', 's', 
8 -> 't', 'u', 'v', 
9 -> 'w', 'x', 'y', 'z'. 
Note that 1 and 0 are not mapped. 
Example: Input: "23", Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"].

## Approach
The problem can be solved using recursion and backtracking. We create a recursive function that tries all possible letters for each digit and backtracks when a combination is found. 
The base case for the recursion is when the input string is empty, at which point we add the current combination to the result.
We use a map to store the mapping of digits to letters.

## Complexity
- Time: O(4^n) where n is the length of the input string, as in the worst case, each digit can have 4 possible letters.
- Space: O(n) for the recursion stack.

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<string> letterCombinations(string digits) {
        // Create a map to store the mapping of digits to letters
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

        // Recursive function to generate all combinations
        function<void(int, string)> backtrack = [&](int index, string path) {
            if (path.size() == digits.size()) {
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
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Input: ""
Output: []
Input: "2"
Output: ["a","b","c"]
```

## Key Takeaways
- Use recursion and backtracking to solve problems that require trying all possible combinations.
- Use a map to store the mapping of digits to letters for easy lookup.
- The base case for the recursion is when the input string is empty, at which point we add the current combination to the result.