# Valid Anagram

## Problem Statement
Given two strings `s` and `t`, write a function to determine if `t` is an anagram of `s`. An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once. The function should return `true` if `t` is an anagram of `s`, and `false` otherwise. The strings `s` and `t` consist of lowercase English letters, and the length of both strings is between 1 and 10^4. For example, "anagram" and "nagaram" are anagrams, but "rat" and "car" are not.

## Approach
The algorithm involves sorting both strings and comparing the results. If the sorted strings are equal, then the original strings are anagrams. This approach works because anagrams are simply rearrangements of the original string, so sorting the characters will produce the same result for anagrams.

## Complexity
- Time: O(n log n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

bool isAnagram(string s, string t) {
    // If the lengths of the strings are not equal, they cannot be anagrams
    if (s.length() != t.length()) {
        return false;
    }

    // Sort the characters in both strings
    sort(s.begin(), s.end());
    sort(t.begin(), t.end());

    // Compare the sorted strings
    return s == t;
}
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
- The time complexity of sorting a string of length n is O(n log n), which dominates the overall time complexity of this solution.