# Letter Combinations of Phone Number

## Problem Statement
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. The mapping of digits to letters is as follows: 
- 2: 'a', 'b', 'c'
- 3: 'd', 'e', 'f'
- 4: 'g', 'h', 'i'
- 5: 'j', 'k', 'l'
- 6: 'm', 'n', 'o'
- 7: 'p', 'q', 'r', 's'
- 8: 't', 'u', 'v'
- 9: 'w', 'x', 'y', 'z'
Each digit can only map to the letters shown in the mapping. For example, if the input is "23", the output should be ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

## Approach
The solution utilizes recursion and backtracking to generate all possible combinations. It iterates over each digit in the input string, and for each digit, it iterates over the corresponding letters. The algorithm builds the combinations by appending each letter to the current combination and recursively calling the function for the next digit.

## Complexity
- Time: O(4^n) where n is the length of the input string, as in the worst case, each digit can map to 4 letters (e.g., digit 7 or 9)
- Space: O(n) for the recursion stack and to store the result

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<string> letterCombinations(string digits) {
        // Mapping of digits to letters
        vector<string> phone = {"", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
        vector<string> result;
        
        // Base case: if input string is empty, return an empty vector
        if (digits.empty()) return result;
        
        // Recursive function to generate combinations
        backtrack(result, phone, digits, 0, "");
        return result;
    }
    
    void backtrack(vector<string>& result, vector<string>& phone, string& digits, int index, string current) {
        // Base case: if the current combination has the same length as the input string, add it to the result
        if (index == digits.size()) {
            result.push_back(current);
            return;
        }
        
        // Get the letters corresponding to the current digit
        string letters = phone[digits[index] - '0'];
        
        // For each letter, append it to the current combination and recursively call the function for the next digit
        for (char letter : letters) {
            backtrack(result, phone, digits, index + 1, current + letter);
        }
    }
};

int main() {
    Solution solution;
    string input = "23";
    vector<string> result = solution.letterCombinations(input);
    for (const string& combination : result) {
        cout << combination << " ";
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
- Use recursion and backtracking to generate all possible combinations of letters for a given phone number.
- Utilize a mapping of digits to letters to determine the possible letters for each digit.
- The time complexity is O(4^n) in the worst case, where n is the length of the input string.