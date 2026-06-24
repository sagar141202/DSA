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
A number can have multiple combinations, and the order of combinations does not matter. For example, if the input is "23", the output should be ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

## Approach
The problem can be solved using recursion and backtracking, where we try all possible combinations of letters for each digit. We will use a recursive function to generate all combinations. The base case for the recursion is when the input string is empty. 

## Complexity
- Time: O(4^n) where n is the length of the input string, as in the worst case, each digit can have 4 possible letters (for digit 7 and 9).
- Space: O(n) for the recursive call stack.

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<string> letterCombinations(string digits) {
        // Define the mapping of digits to letters
        vector<string> phone = {"", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
        vector<string> output;
        
        // Base case: if the input string is empty
        if (digits.empty()) {
            return output;
        }
        
        // Recursive function to generate combinations
        backtrack(output, phone, digits, 0, "");
        return output;
    }
    
    void backtrack(vector<string>& output, vector<string>& phone, string& digits, int index, string current) {
        // Base case: if we have processed all digits
        if (index == digits.size()) {
            output.push_back(current);
            return;
        }
        
        // Get the possible letters for the current digit
        string letters = phone[digits[index] - '0'];
        
        // Try all possible letters
        for (char letter : letters) {
            // Recursively generate combinations for the remaining digits
            backtrack(output, phone, digits, index + 1, current + letter);
        }
    }
};

int main() {
    Solution solution;
    string input = "23";
    vector<string> output = solution.letterCombinations(input);
    for (string combination : output) {
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
- Use recursion and backtracking to generate all possible combinations of letters for a given phone number.
- Define a base case to stop the recursion, such as when the input string is empty or when all digits have been processed.
- Use a recursive function to try all possible combinations of letters for each digit.