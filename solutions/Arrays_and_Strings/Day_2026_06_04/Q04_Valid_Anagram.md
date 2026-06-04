# Valid Anagram

## Problem Statement
Given two strings `s` and `t`, write a function to determine if `t` is an anagram of `s`. An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once. The function should return `true` if `t` is an anagram of `s`, and `false` otherwise. The strings `s` and `t` contain only lowercase letters and have a length of at most 5 * 10^4. For example, "anagram" and "nagaram" are anagrams, while "rat" and "car" are not.

## Approach
The approach is to sort both strings and compare them. If they are equal, then `t` is an anagram of `s`. Alternatively, we can use a frequency count array to count the occurrences of each character in both strings and compare the counts.

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
        // If the strings have different lengths, they cannot be anagrams
        if (s.length() != t.length()) {
            return false;
        }
        
        // Create frequency count arrays for both strings
        int count[26] = {0};
        
        // Count the occurrences of each character in the first string
        for (char c : s) {
            count[c - 'a']++;
        }
        
        // Subtract the occurrences of each character in the second string
        for (char c : t) {
            count[c - 'a']--;
        }
        
        // If all counts are zero, then the strings are anagrams
        for (int i = 0; i < 26; i++) {
            if (count[i] != 0) {
                return false;
            }
        }
        
        return true;
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
- We can use sorting or frequency count arrays to determine if two strings are anagrams.
- The time complexity of the sorting approach is O(n log n), while the time complexity of the frequency count array approach is O(n).