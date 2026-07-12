# Valid Anagram

## Problem Statement
Given two strings `s` and `t`, write a function to determine if `t` is an anagram of `s`. An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once. The function should return `true` if `t` is an anagram of `s`, and `false` otherwise. The strings may contain any ASCII characters, and the function should be case-sensitive.

## Approach
The approach is to use a frequency count array to count the occurrences of each character in both strings. Then, compare the two frequency count arrays to determine if they are equal. If they are equal, then `t` is an anagram of `s`. This approach works because anagrams have the same characters with the same frequencies.

## Complexity
- Time: O(n)
- Space: O(1)

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
        int count[256] = {0};
        
        // Count the occurrences of each character in the first string
        for (char c : s) {
            count[(int)c]++;
        }
        
        // Subtract the occurrences of each character in the second string
        for (char c : t) {
            count[(int)c]--;
            // If the count of any character is negative, the strings are not anagrams
            if (count[(int)c] < 0) {
                return false;
            }
        }
        
        // If we have not returned false by now, the strings are anagrams
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
- Use a frequency count array to count the occurrences of each character in both strings.
- Compare the two frequency count arrays to determine if they are equal.
- The function should return `true` if the two strings are anagrams, and `false` otherwise.