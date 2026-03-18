# Valid Anagram

## Problem Statement
Given two strings `s` and `t`, write a function to determine if `t` is an anagram of `s`. An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once. The function should return `true` if `t` is an anagram of `s`, and `false` otherwise. The strings may contain any ASCII characters, and the function should be case-sensitive. For example, given `s = "listen"` and `t = "silent"`, the function should return `true`, while given `s = "hello"` and `t = "world"`, the function should return `false`.

## Approach
The approach is to use a hash table to count the frequency of each character in both strings and compare the resulting hash tables. If the hash tables are equal, then `t` is an anagram of `s`. This approach works because anagrams are simply rearrangements of the original string, so the frequency of each character must be the same.

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

        // Create a hash table to count the frequency of each character in the first string
        unordered_map<char, int> s_count;
        for (char c : s) {
            s_count[c]++;
        }

        // Create a hash table to count the frequency of each character in the second string
        unordered_map<char, int> t_count;
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
- A hash table can be used to count the frequency of each character in a string.
- Two strings are anagrams if and only if they have the same frequency of each character.