# Valid Anagram

## Problem Statement
Given two strings `s` and `t`, write a function to determine if `t` is an anagram of `s`. An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once. The function should return `true` if `t` is an anagram of `s`, and `false` otherwise. The strings `s` and `t` contain only lowercase letters and have a length of at most 5 * 10^4. For example, given `s = "anagram"` and `t = "nagaram"`, the function should return `true`. Given `s = "rat"` and `t = "car"`, the function should return `false`.

## Approach
The approach to solve this problem is to use sorting to compare the characters in the two strings. If the sorted strings are equal, then `t` is an anagram of `s`. Alternatively, we can use a frequency count array to compare the frequency of each character in the two strings.

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
        // If the lengths of the strings are not equal, they cannot be anagrams
        if (s.length() != t.length()) {
            return false;
        }
        
        // Sort the strings and compare them
        sort(s.begin(), s.end());
        sort(t.begin(), t.end());
        
        // If the sorted strings are equal, then t is an anagram of s
        return s == t;
    }
};
```

## Test Cases
```
Input: s = "anagram", t = "nagaram"
Output: true
Input: s = "rat", t = "car"
Output: false
```

## Key Takeaways
- An anagram is a word or phrase formed by rearranging the letters of a different word or phrase.
- We can use sorting to compare the characters in two strings and determine if one is an anagram of the other.
- Alternatively, we can use a frequency count array to compare the frequency of each character in the two strings.