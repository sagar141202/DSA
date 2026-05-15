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
For example, input "23" should return ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

## Approach
This problem can be solved using recursion and backtracking. We iterate over each digit, and for each digit, we iterate over its corresponding letters. We use a helper function to generate all combinations recursively.

## Complexity
- Time: O(4^n) where n is the number of digits, because in the worst case, each digit can have 4 corresponding letters.
- Space: O(n) for the recursion stack.

## C++ Solution
```cpp
#include <vector>
#include <string>

class Solution {
public:
    vector<string> letterCombinations(string digits) {
        vector<string> result;
        if (digits.empty()) return result;
        
        vector<string> phone = {"", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
        backtrack(result, phone, digits, 0, "");
        return result;
    }
    
    void backtrack(vector<string>& result, vector<string>& phone, string& digits, int index, string current) {
        if (index == digits.size()) {
            result.push_back(current);
            return;
        }
        
        for (char c : phone[digits[index] - '0']) {
            backtrack(result, phone, digits, index + 1, current + c);
        }
    }
};
```

## Test Cases
```
Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
```

## Key Takeaways
- Recursion and backtracking can be used to generate all possible combinations of letters.
- We use a helper function to generate combinations recursively.
- The time complexity is exponential in the number of digits due to the recursive nature of the solution.