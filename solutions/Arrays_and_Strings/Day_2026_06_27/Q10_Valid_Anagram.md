# Valid Anagram

## Problem Statement
Given two strings `s` and `t`, write a function to determine if `t` is an anagram of `s`. An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once. The function should return `true` if `t` is an anagram of `s`, and `false` otherwise. The input strings only contain lowercase English letters and have a length of at most 100 characters.

## Approach
The approach is to use a sorting algorithm to sort both strings and then compare them. Alternatively, we can use a frequency count array to count the occurrences of each character in both strings and compare the count arrays.

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
        // If the two strings have different lengths, they cannot be anagrams
        if (s.length() != t.length()) {
            return false;
        }
        
        // Create a frequency count array
        int count[26] = {0};
        
        // Count the occurrences of each character in string s
        for (char c : s) {
            count[c - 'a']++;
        }
        
        // Subtract the occurrences of each character in string t
        for (char c : t) {
            count[c - 'a']--;
        }
        
        // If all counts are zero, the two strings are anagrams
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
- We can use a sorting algorithm or a frequency count array to determine if two strings are anagrams.
- The time complexity of the sorting approach is O(n log n), while the time complexity of the frequency count approach is O(n).