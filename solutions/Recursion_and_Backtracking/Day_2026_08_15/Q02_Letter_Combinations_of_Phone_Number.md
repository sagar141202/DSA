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
A number can have any number of digits, and the input will not be empty. For example, if the input is "23", the output should be ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

## Approach
We can solve this problem using recursion and backtracking. The idea is to generate all possible combinations by recursively trying each possible letter for the current digit. We will use a helper function to perform the recursion.

## Complexity
- Time: O(4^n) where n is the number of digits in the input string, because in the worst case, each digit can have 4 possible letters.
- Space: O(n) for the space required by the recursion stack.

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
    string digits = "23";
    vector<string> result = solution.letterCombinations(digits);
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
```

## Key Takeaways
- Use recursion and backtracking to generate all possible combinations.
- Create a helper function to perform the recursion.
- Use a vector to store the result and pass it by reference to the helper function.