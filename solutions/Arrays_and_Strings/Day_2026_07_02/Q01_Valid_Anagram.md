# Valid Anagram

## Problem Statement
Given two strings `s` and `t`, write a function to determine if `t` is an anagram of `s`. An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once. The function should return `true` if `t` is an anagram of `s`, and `false` otherwise. The strings may contain any ASCII characters, and the function should be case-sensitive.

## Approach
The approach is to use a hash table to count the frequency of each character in both strings, and then compare the two hash tables. If the two hash tables are equal, then `t` is an anagram of `s`. This approach takes advantage of the fact that anagrams have the same characters with the same frequencies.

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
        
        // Create a hash table to count the frequency of each character in s
        unordered_map<char, int> count_s;
        for (char c : s) {
            count_s[c]++;
        }
        
        // Create a hash table to count the frequency of each character in t
        unordered_map<char, int> count_t;
        for (char c : t) {
            count_t[c]++;
        }
        
        // Compare the two hash tables
        return count_s == count_t;
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
- Use a hash table to count the frequency of each character in both strings.
- Compare the two hash tables to determine if the two strings are anagrams.
- The function should be case-sensitive and should handle any ASCII characters.