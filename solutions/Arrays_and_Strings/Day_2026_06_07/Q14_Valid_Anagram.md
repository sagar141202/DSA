# Valid Anagram

## Problem Statement
Given two strings `s` and `t`, write a function to determine if `t` is an anagram of `s`. An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once. The function should return `true` if `t` is an anagram of `s`, and `false` otherwise. The strings `s` and `t` may contain any ASCII characters, and the function should be case-sensitive. For example, "listen" and "silent" are anagrams, while "hello" and "world" are not.

## Approach
The approach to solving this problem is to use a sorting algorithm to sort the characters in both strings and then compare the sorted strings. Alternatively, we can use a frequency counting approach to count the occurrences of each character in both strings and then compare the frequency counts. This approach has a time complexity of O(n log n) due to the sorting, or O(n) using the frequency counting approach.

## Complexity
- Time: O(n log n) or O(n)
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

        // Create frequency count arrays for both strings
        int count[256] = {0}; // assuming ASCII characters

        // Count the frequency of each character in string s
        for (char c : s) {
            count[c]++;
        }

        // Subtract the frequency of each character in string t
        for (char c : t) {
            count[c]--;
            // If the count goes below 0, it means t has more occurrences of c than s
            if (count[c] < 0) {
                return false;
            }
        }

        // If we reach this point, it means t is an anagram of s
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
- An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
- The time complexity of the sorting approach is O(n log n), while the frequency counting approach has a time complexity of O(n).
- The space complexity of both approaches is O(n), where n is the length of the input strings.