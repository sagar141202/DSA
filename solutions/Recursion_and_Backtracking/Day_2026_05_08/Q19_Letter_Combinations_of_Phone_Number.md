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
A number can have any number of digits, and each digit can map to multiple letters. For example, the input "23" can be represented as ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

## Approach
We will use a recursive approach with backtracking to generate all possible combinations. The algorithm will iterate through each digit in the input string and recursively generate combinations for the remaining digits.

## Complexity
- Time: O(4^n) where n is the number of digits in the input string, as each digit can have up to 4 possible mappings.
- Space: O(n) for the recursive call stack.

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
        vector<string> phone = {"", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
        
        backtrack(result, phone, digits, 0, "");
        return result;
    }
    
    void backtrack(vector<string>& result, vector<string>& phone, string& digits, int index, string current) {
        if (index == digits.size()) {
            result.push_back(current);
            return;
        }
        
        // Get the possible letters for the current digit
        string letters = phone[digits[index] - '0'];
        
        // Recursively generate combinations for each letter
        for (char letter : letters) {
            backtrack(result, phone, digits, index + 1, current + letter);
        }
    }
};

int main() {
    Solution solution;
    string input = "23";
    vector<string> result = solution.letterCombinations(input);
    
    // Print the result
    for (const auto& combination : result) {
        cout << combination << " ";
    }
    cout << endl;
    
    return 0;
}
```

## Test Cases
```
Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
```

## Key Takeaways
- Use recursion and backtracking to generate all possible combinations of letters for a given phone number.
- Define a mapping of digits to letters to simplify the generation process.
- The time complexity is O(4^n) due to the recursive nature of the algorithm, where n is the number of digits in the input string.