# Valid Anagram

## Problem Statement
Given two strings `s` and `t`, write a function to determine if `t` is an anagram of `s`. An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once. The function should return `true` if `t` is an anagram of `s`, and `false` otherwise. The strings may contain any ASCII characters, and the function should be case-sensitive. For example, given `s = "listen"` and `t = "silent"`, the function should return `true`, while given `s = "hello"` and `t = "world"`, the function should return `false`.

## Approach
The approach to solve this problem is to use a hash table to count the frequency of each character in both strings and compare the resulting hash tables. If the hash tables are equal, then `t` is an anagram of `s`. This approach works because anagrams have the same characters with the same frequencies.

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
        unordered_map<char, int> count_s;
        unordered_map<char, int> count_t;

        // Count the frequency of each character in string s
        for (char c : s) {
            count_s[c]++;
        }

        // Count the frequency of each character in string t
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
- Compare the resulting hash tables to determine if the two strings are anagrams.
- The time complexity of this solution is O(n), where n is the length of the input strings.