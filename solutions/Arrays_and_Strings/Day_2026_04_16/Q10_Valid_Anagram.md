# Valid Anagram

## Problem Statement
Given two strings `s` and `t`, write a function to determine if `t` is an anagram of `s`. An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once. The function should return `true` if `t` is an anagram of `s`, and `false` otherwise. The input strings only contain lowercase English letters and have a length of at most 5 * 10^4.

## Approach
The algorithm uses a sorting approach to check if the two strings are anagrams. If the sorted versions of the two strings are equal, then they are anagrams. Alternatively, a frequency counting approach can be used to achieve better time complexity.

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
        
        // Sort the two strings and compare them
        sort(s.begin(), s.end());
        sort(t.begin(), t.end());
        
        // If the sorted strings are equal, then the original strings are anagrams
        return s == t;
    }
};

// Alternatively, a frequency counting approach can be used
class Solution2 {
public:
    bool isAnagram(string s, string t) {
        // If the two strings have different lengths, they cannot be anagrams
        if (s.length() != t.length()) {
            return false;
        }
        
        // Initialize a frequency array to count the occurrences of each character
        int count[26] = {0};
        
        // Count the occurrences of each character in the first string
        for (char c : s) {
            count[c - 'a']++;
        }
        
        // Subtract the occurrences of each character in the second string
        for (char c : t) {
            count[c - 'a']--;
        }
        
        // If all counts are zero, then the two strings are anagrams
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
- The time complexity of the sorting approach is O(n log n), while the frequency counting approach has a time complexity of O(n).
- The space complexity of both approaches is O(n), where n is the length of the input strings.