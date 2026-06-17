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
A number can have any number of digits. The input string will not contain 0 or 1.

## Approach
The approach to solve this problem is to use recursion and backtracking. We will create a recursive function that generates all possible combinations of letters for a given number. For each digit in the number, we will iterate over all possible letters that it can represent and recursively generate combinations for the remaining digits.

## Complexity
- Time: O(4^n) where n is the number of digits in the input number, as in the worst case (for digit 7 or 9), we have 4 possibilities for each digit.
- Space: O(n) for the recursion stack.

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
        
        function<void(int, string)> backtrack = [&](int index, string current) {
            if (index == digits.size()) {
                result.push_back(current);
                return;
            }
            
            string letters = phone[digits[index] - '0'];
            for (char letter : letters) {
                backtrack(index + 1, current + letter);
            }
        };
        
        backtrack(0, "");
        return result;
    }
};
```

## Test Cases
```
Input: "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
```

## Key Takeaways
- Use recursion and backtracking to generate all possible combinations of letters for a given number.
- Create a recursive function that generates combinations for the remaining digits.
- Use a vector to store the result and a function to perform the backtracking.