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
The input will be a string of length 1 to 4. 
Example: Input: "23", Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"].

## Approach
We can solve this problem by using recursion and backtracking. We will create a recursive function that tries all possible letters for each digit and adds them to the result if they are valid combinations. The function will stop recursing when it has processed all digits.

## Complexity
- Time: O(4^n) where n is the number of digits in the input string
- Space: O(n) for the recursion stack

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
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Input: ""
Output: []
Input: "2"
Output: ["a","b","c"]
```

## Key Takeaways
- Recursion and backtracking can be used to solve problems that involve generating all possible combinations of something.
- The key to solving these types of problems is to define a recursive function that tries all possible options and adds them to the result if they are valid.
- It's also important to consider the base case for the recursion, which is when there are no more options to try.