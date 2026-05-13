# Valid Anagram

## Problem Statement
Given two strings, determine if they are anagrams of each other. An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once. The strings may contain only lowercase letters and the comparison should be case-insensitive. For example, "listen" and "silent" are anagrams, while "hello" and "world" are not.

## Approach
The algorithm involves sorting the characters in both strings and comparing the results. If the sorted strings are equal, then the original strings are anagrams. This approach works because anagrams are simply rearrangements of the same characters.

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
        // If the strings are of different lengths, they cannot be anagrams
        if (s.length() != t.length()) {
            return false;
        }
        
        // Sort the characters in both strings
        sort(s.begin(), s.end());
        sort(t.begin(), t.end());
        
        // Compare the sorted strings
        return s == t;
    }
};

// Alternatively, we can use a frequency count approach
class Solution {
public:
    bool isAnagram(string s, string t) {
        // If the strings are of different lengths, they cannot be anagrams
        if (s.length() != t.length()) {
            return false;
        }
        
        // Create a frequency count array for the first string
        int count[26] = {0};
        for (char c : s) {
            count[c - 'a']++;
        }
        
        // Subtract the frequency count of the second string
        for (char c : t) {
            count[c - 'a']--;
        }
        
        // Check if all counts are zero
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
Input: s = "listen", t = "silent"
Output: true
Input: s = "hello", t = "world"
Output: false
```

## Key Takeaways
- Anagrams are simply rearrangements of the same characters, so we can compare them by sorting or counting the frequency of each character.
- The time complexity of the sorting approach is O(n log n) due to the sorting operation, while the frequency count approach has a time complexity of O(n).
- The space complexity of both approaches is O(n), where n is the length of the input strings.