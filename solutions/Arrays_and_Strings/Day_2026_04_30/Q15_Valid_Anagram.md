# Valid Anagram

## Problem Statement
Given two strings `s` and `t`, write a function to determine if `t` is an anagram of `s`. An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once. The function should return `true` if `t` is an anagram of `s`, and `false` otherwise. The input strings only contain lowercase English letters and have a length of at most 5 * 10^4.

## Approach
The approach is to use a sorting algorithm to sort both strings and compare them. Alternatively, we can use a frequency count array to count the occurrences of each character in both strings and compare the arrays. This approach takes advantage of the fact that anagrams have the same characters with the same frequencies. We can also use an unordered_map to store the frequency of characters in the strings.

## Complexity
- Time: O(n log n) for sorting, O(n) for frequency count array or unordered_map approach
- Space: O(n) for sorting, O(1) for frequency count array, O(n) for unordered_map approach

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool isAnagram(string s, string t) {
        // Check if the lengths of the strings are equal
        if (s.length() != t.length()) {
            return false;
        }
        
        // Create a frequency count array
        int count[26] = {0};
        
        // Count the occurrences of each character in the first string
        for (int i = 0; i < s.length(); i++) {
            count[s[i] - 'a']++;
        }
        
        // Subtract the occurrences of each character in the second string
        for (int i = 0; i < t.length(); i++) {
            count[t[i] - 'a']--;
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
- An anagram must have the same characters with the same frequencies.
- We can use a frequency count array or an unordered_map to count the occurrences of each character in the strings.
- The time complexity of the solution depends on the approach used, with the frequency count array or unordered_map approach being more efficient than the sorting approach.