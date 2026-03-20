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
A number can have 3 or 4 possible letters. For example, given the input "23", the output should be ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

## Approach
We use recursion and backtracking to solve this problem. The idea is to generate all possible combinations of letters for each digit in the input string. We iterate over each possible letter for a digit, add it to the current combination, and then recursively generate combinations for the remaining digits.

## Complexity
- Time: O(4^n) where n is the number of digits in the input string
- Space: O(n) for the recursive call stack

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
        
        backtrack(result, phone, digits, 0, "");
        return result;
    }
    
    void backtrack(vector<string>& result, unordered_map<char, string>& phone, string& digits, int index, string current) {
        if (index == digits.size()) {
            result.push_back(current);
            return;
        }
        
        // Get the letters for the current digit
        string letters = phone[digits[index]];
        
        // Iterate over each possible letter for the current digit
        for (char letter : letters) {
            // Add the letter to the current combination and recurse
            backtrack(result, phone, digits, index + 1, current + letter);
        }
    }
};

int main() {
    Solution solution;
    string digits = "23";
    vector<string> result = solution.letterCombinations(digits);
    
    // Print the result
    for (const string& combination : result) {
        cout << combination << endl;
    }
    
    return 0;
}
```

## Test Cases
```
Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
```

## Key Takeaways
- Use recursion and backtracking to generate all possible combinations of letters for each digit in the input string.
- Use an unordered map to store the mapping of digits to letters for efficient lookup.
- The time complexity is O(4^n) where n is the number of digits in the input string, and the space complexity is O(n) for the recursive call stack.