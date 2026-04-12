# Valid Anagram

## Problem Statement
Given two strings `s` and `t`, write a function to determine if `t` is an anagram of `s`. An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once. The function should return `true` if `t` is an anagram of `s`, and `false` otherwise. The strings only contain lowercase English letters and have a length of at most 5 * 10^4. For example, given `s = "anagram"` and `t = "nagaram"`, the function should return `true`. Given `s = "rat"` and `t = "car"`, the function should return `false`.

## Approach
The algorithm uses a sorting approach to check if two strings are anagrams. It sorts both strings and compares them. If they are equal, then they are anagrams. Alternatively, it can use a frequency count approach to compare the frequency of characters in both strings.

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

        // Sort both strings and compare them
        sort(s.begin(), s.end());
        sort(t.begin(), t.end());
        return s == t;
    }

    // Alternative solution using frequency count
    bool isAnagramAlt(string s, string t) {
        if (s.length() != t.length()) {
            return false;
        }

        // Create a frequency count array for the characters in the strings
        int count[26] = {0};
        for (char c : s) {
            count[c - 'a']++;
        }
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
Input: s = "anagram", t = "nagaram"
Output: true
Input: s = "rat", t = "car"
Output: false
```

## Key Takeaways
- An anagram is a word or phrase formed by rearranging the letters of a different word or phrase.
- The sorting approach has a time complexity of O(n log n) due to the sorting operation.
- The frequency count approach has a time complexity of O(n) and is more efficient for large strings.