# Valid Anagram

## Problem Statement
Given two strings `s` and `t`, write a function to determine if `t` is an anagram of `s`. An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once. The function should return `true` if `t` is an anagram of `s`, and `false` otherwise. The input strings only contain lowercase English letters and have a length of at most 5 * 10^4. For example, given `s = "anagram"` and `t = "nagaram"`, the function should return `true`, while given `s = "hello"` and `t = "world"`, the function should return `false`.

## Approach
The approach to solve this problem is to use a sorting algorithm to sort both strings and compare the results. Alternatively, we can use a hash table to count the frequency of each character in both strings and compare the results. This approach ensures that the function returns the correct result in an efficient manner.

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

        // Sort the two strings and compare the results
        sort(s.begin(), s.end());
        sort(t.begin(), t.end());

        // Return true if the sorted strings are equal, false otherwise
        return s == t;
    }
};
```

## Test Cases
```
Input: s = "anagram", t = "nagaram"
Output: true
Input: s = "hello", t = "world"
Output: false
```

## Key Takeaways
- An anagram is a word or phrase formed by rearranging the letters of a different word or phrase.
- The problem can be solved using a sorting algorithm or a hash table to compare the frequency of characters in the two strings.
- The time complexity of the solution using sorting is O(n log n), while the space complexity is O(n).