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
The input will be a string of length 1 to 4. For example, if the input is "23", the output should be ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

## Approach
We use recursion and backtracking to generate all possible combinations of letters. We define a recursive function that takes the current combination and the remaining digits as arguments. We iterate over the possible letters for the current digit and recursively call the function with the updated combination and remaining digits.

## Complexity
- Time: O(4^n) where n is the length of the input string
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
        
        vector<string> phone = {"", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
        backtrack(result, phone, digits, 0, "");
        return result;
    }
    
    void backtrack(vector<string>& result, vector<string>& phone, string& digits, int index, string current) {
        if (index == digits.size()) {
            result.push_back(current);
            return;
        }
        
        string letters = phone[digits[index] - '0'];
        for (char letter : letters) {
            backtrack(result, phone, digits, index + 1, current + letter);
        }
    }
};

int main() {
    Solution solution;
    vector<string> result = solution.letterCombinations("23");
    for (string str : result) {
        cout << str << " ";
    }
    return 0;
}
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
- Recursion and backtracking can be used to solve problems that require generating all possible combinations.
- The time complexity of the solution is exponential in the length of the input string.
- The space complexity is linear in the length of the input string due to the recursive call stack.