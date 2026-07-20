# Valid Anagram

## Problem Statement
Given two strings `s` and `t`, write a function to determine if `t` is an anagram of `s`. An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once. The function should return `true` if `t` is an anagram of `s`, and `false` otherwise. The strings may contain any ASCII characters, and the function should be case-sensitive. For example, given `s = "listen"` and `t = "silent"`, the function should return `true`, while given `s = "hello"` and `t = "world"`, the function should return `false`. The length of the strings will not exceed 10^5 characters.

## Approach
The algorithm uses a hash table to count the frequency of each character in both strings. It then compares the two hash tables to determine if they are equal, indicating that the strings are anagrams. This approach has a linear time complexity and is suitable for large inputs. The intuition is to use the hash table to normalize the strings, allowing for efficient comparison.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool isAnagram(string s, string t) {
        // If the strings are not the same length, they cannot be anagrams
        if (s.length() != t.length()) {
            return false;
        }
        
        // Create a hash table to count the frequency of each character
        unordered_map<char, int> count;
        
        // Count the frequency of each character in the first string
        for (char c : s) {
            count[c]++;
        }
        
        // Subtract the frequency of each character in the second string
        for (char c : t) {
            count[c]--;
            // If the count is negative, the strings are not anagrams
            if (count[c] < 0) {
                return false;
            }
        }
        
        // If all counts are zero, the strings are anagrams
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
- Use a hash table to count the frequency of each character in the strings.
- Compare the hash tables to determine if the strings are anagrams.
- The function should be case-sensitive and should handle ASCII characters.