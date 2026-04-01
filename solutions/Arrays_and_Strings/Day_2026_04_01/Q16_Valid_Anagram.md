# Valid Anagram

## Problem Statement
Given two strings `s` and `t`, write a function to determine if `t` is an anagram of `s`. An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once. The function should return `true` if `t` is an anagram of `s`, and `false` otherwise. The strings `s` and `t` contain only lowercase letters and have a length of at most 5 * 10^4. For example, "anagram" and "nagaram" are anagrams, while "rat" and "car" are not.

## Approach
The algorithm involves sorting both strings and comparing the results. If the sorted strings are equal, then the original strings are anagrams. This approach works because anagrams are simply rearrangements of the original string, so sorting the characters will produce the same result for anagrams.

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
        
        // Sort both strings and compare the results
        sort(s.begin(), s.end());
        sort(t.begin(), t.end());
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
- Sorting the characters in a string can be used to determine if two strings are anagrams.
- This solution has a time complexity of O(n log n) due to the sorting operation.