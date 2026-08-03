# Valid Anagram

## Problem Statement
Given two strings `s` and `t`, write a function to determine if `t` is an anagram of `s`. An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once. The function should return `true` if `t` is an anagram of `s`, and `false` otherwise. The strings `s` and `t` only contain lowercase English letters and have a length of at most 5 * 10^4. For example, "anagram" and "nagaram" are anagrams, while "rat" and "car" are not.

## Approach
We can solve this problem by sorting both strings and comparing the results. If the sorted strings are equal, then the original strings are anagrams. Alternatively, we can use a frequency count array to compare the frequency of each character in both strings.

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
        
        // Sort both strings and compare the results
        sort(s.begin(), s.end());
        sort(t.begin(), t.end());
        
        // If the sorted strings are equal, the original strings are anagrams
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
- We can solve this problem by sorting both strings and comparing the results, or by using a frequency count array to compare the frequency of each character in both strings.
- The time complexity of the sorting approach is O(n log n), while the time complexity of the frequency count approach is O(n).