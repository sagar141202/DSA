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
A number can represent multiple letters, and each letter can be used multiple times. For example, "23" can represent "ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf".

## Approach
We can solve this problem using recursion and backtracking by iterating over each possible letter for each digit. The algorithm will explore all possible combinations of letters for the given digits. We will use a helper function to perform the backtracking.

## Complexity
- Time: O(4^n) where n is the number of digits, as in the worst case, each digit can map to 4 letters.
- Space: O(n) for the recursion stack.

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<string> letterCombinations(string digits) {
        vector<string> result;
        if (digits.empty()) {
            return result;
        }
        
        vector<string> mapping = {"", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
        backtrack(result, "", digits, mapping, 0);
        return result;
    }
    
    void backtrack(vector<string>& result, string current, string digits, vector<string>& mapping, int index) {
        if (index == digits.size()) {
            result.push_back(current);
            return;
        }
        
        string letters = mapping[digits[index] - '0'];
        for (char letter : letters) {
            backtrack(result, current + letter, digits, mapping, index + 1);
        }
    }
};

int main() {
    Solution solution;
    string digits = "23";
    vector<string> result = solution.letterCombinations(digits);
    for (string combination : result) {
        cout << combination << " ";
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
- The problem can be solved using recursion and backtracking.
- We use a helper function to perform the backtracking.
- The time complexity is O(4^n) where n is the number of digits, and the space complexity is O(n) for the recursion stack.