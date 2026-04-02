# Valid Anagram

## Problem Statement
Given two strings `s` and `t`, write a function to determine if `t` is an anagram of `s`. An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once. The function should return `true` if `t` is an anagram of `s`, and `false` otherwise. The input strings may contain any ASCII characters, and the function should be case-sensitive. For example, given `s = "listen"` and `t = "silent"`, the function should return `true`, while given `s = "hello"` and `t = "world"`, the function should return `false`.

## Approach
The approach to solve this problem is to use a hash table to count the frequency of each character in both strings and compare the resulting hash tables. If the two hash tables are equal, then `t` is an anagram of `s`. This approach works because anagrams are simply rearrangements of the original string, so the character frequencies must be the same.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool isAnagram(string s, string t) {
        // If the two strings have different lengths, they cannot be anagrams
        if (s.length() != t.length()) {
            return false;
        }
        
        // Create two hash tables to count the frequency of each character
        unordered_map<char, int> s_count;
        unordered_map<char, int> t_count;
        
        // Count the frequency of each character in string s
        for (char c : s) {
            s_count[c]++;
        }
        
        // Count the frequency of each character in string t
        for (char c : t) {
            t_count[c]++;
        }
        
        // Compare the two hash tables
        return s_count == t_count;
    }
};
```

## Test Cases
```
Input: s = "listen", t = "silent"
Output: true
Input: s = "hello", t = "world"
Output: false
```

## Key Takeaways
- An anagram is a word or phrase formed by rearranging the letters of a different word or phrase.
- The key to solving this problem is to compare the character frequencies of the two input strings.
- Using a hash table to count the frequency of each character is an efficient way to solve this problem.