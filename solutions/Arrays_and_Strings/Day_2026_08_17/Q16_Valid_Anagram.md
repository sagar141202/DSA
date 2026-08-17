# Valid Anagram

## Problem Statement
Given two strings `s` and `t`, write a function to determine if `t` is an anagram of `s`. An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once. The function should return `true` if `t` is an anagram of `s`, and `false` otherwise. The input strings may contain any ASCII characters, and the function should be case-sensitive. For example, "listen" and "silent" are anagrams, but "listen" and "tins" are not.

## Approach
The algorithm uses sorting to compare the two input strings. It first checks if the lengths of the two strings are equal, then sorts the characters in each string and compares the sorted strings. If the sorted strings are equal, then the original strings are anagrams of each other.

## Complexity
- Time: O(n log n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool isAnagram(string s, string t) {
        // If the lengths of the two strings are not equal, they cannot be anagrams
        if (s.length() != t.length()) {
            return false;
        }
        
        // Sort the characters in each string
        sort(s.begin(), s.end());
        sort(t.begin(), t.end());
        
        // Compare the sorted strings
        return s == t;
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
- An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
- The function should be case-sensitive and should return `false` if the input strings contain any non-ASCII characters.
- The time complexity of the solution is O(n log n) due to the sorting operation, where n is the length of the input strings.