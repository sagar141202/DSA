# Valid Anagram

## Problem Statement
Given two strings `s` and `t`, write a function to determine if `t` is an anagram of `s`. An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once. The function should return `true` if `t` is an anagram of `s`, and `false` otherwise. The input strings only contain lowercase English letters and have a length of at most 5 * 10^4.

## Approach
The algorithm uses sorting to check if two strings are anagrams. If the sorted versions of the strings are equal, then they are anagrams. This approach works because anagrams are simply rearrangements of the same characters.

## Complexity
- Time: O(n log n)
- Space: O(n)

## C++ Solution
```cpp
#include <algorithm>
#include <string>
using namespace std;

bool isAnagram(string s, string t) {
    // If the lengths of the strings are not equal, they cannot be anagrams
    if (s.length() != t.length()) {
        return false;
    }
    
    // Sort the strings and compare them
    sort(s.begin(), s.end());
    sort(t.begin(), t.end());
    
    // If the sorted strings are equal, then they are anagrams
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
- Sorting can be used to check if two strings are anagrams.
- This approach has a time complexity of O(n log n) due to the sorting operation.