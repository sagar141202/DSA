# Palindromic Substrings

## Problem Statement
Given a string, find the total number of palindromic substrings in it. A palindromic substring is a substring that reads the same backward as forward. The string only contains lowercase English letters. The length of the string is between 1 and 1000 characters.

## Approach
The problem can be solved by expanding around the center of potential palindromes and counting the number of valid palindromic substrings. We will consider both odd-length and even-length palindromes. The algorithm iterates over the string, treating each character as a potential center of a palindrome.

## Complexity
- Time: O(n^2)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int countSubstrings(string s) {
        int count = 0;
        for (int i = 0; i < s.size(); i++) {
            // Odd length palindrome
            count += countPalindromes(s, i, i);
            // Even length palindrome
            count += countPalindromes(s, i, i + 1);
        }
        return count;
    }

    int countPalindromes(string s, int left, int right) {
        int count = 0;
        while (left >= 0 && right < s.size() && s[left] == s[right]) {
            count++;
            left--;
            right++;
        }
        return count;
    }
};

int main() {
    Solution solution;
    string input = "abc";
    cout << solution.countSubstrings(input) << endl;
    return 0;
}
```

## Test Cases
```
Input: "abc"
Output: 3
Input: "aaa"
Output: 6
```

## Key Takeaways
- Treat each character in the string as a potential center of a palindrome.
- Expand around the center to count the number of valid palindromic substrings.
- Consider both odd-length and even-length palindromes.