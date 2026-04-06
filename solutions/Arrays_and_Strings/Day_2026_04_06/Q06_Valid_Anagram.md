# Valid Anagram

## Problem Statement
Given two strings `s` and `t`, write a function to determine if `t` is an anagram of `s`. An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once. The function should return `true` if `t` is an anagram of `s`, and `false` otherwise. The strings only contain lowercase English letters and have a length of at most 5 * 10^4. For example, "anagram" and "nagaram" are anagrams, while "rat" and "car" are not.

## Approach
The algorithm sorts both strings and checks if they are equal. This approach works because anagrams are simply rearrangements of the original string, so sorting the characters in each string will result in the same sequence if they are anagrams. Alternatively, a frequency count of characters can be used to determine if two strings are anagrams.

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
        
        // Sort both strings and compare
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
- Sorting the characters in two strings can be used to determine if they are anagrams.
- Alternatively, a frequency count of characters can be used to determine if two strings are anagrams, which can be more efficient than sorting.