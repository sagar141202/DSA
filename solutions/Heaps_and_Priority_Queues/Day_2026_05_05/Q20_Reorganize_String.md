# Reorganize String

## Problem Statement
Given a string `s`, reorganize the characters in the string such that no two adjacent characters are the same. If it's impossible to reorganize the string, return an empty string. The string consists of lowercase English letters and the length of the string is in the range [1, 50000]. For example, given `s = "aab"`, the output should be `"aba"`. However, for `s = "aaab"`, the output should be an empty string because it's impossible to reorganize the string.

## Approach
We can use a max heap to store the frequency of each character. We pop the character with the highest frequency from the heap, append it to the result string, and then push it back into the heap with a decreased frequency. This process is repeated until the heap is empty or the last character in the result string is the same as the character we want to append.

## Complexity
- Time: O(n log n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    string reorganizeString(string s) {
        // Create a frequency map
        map<char, int> freq;
        for (char c : s) {
            freq[c]++;
        }

        // Create a max heap
        priority_queue<pair<int, char>> maxHeap;
        for (auto& it : freq) {
            maxHeap.push({it.second, it.first});
        }

        string result = "";
        while (!maxHeap.empty()) {
            // Get the character with the highest frequency
            pair<int, char> first = maxHeap.top();
            maxHeap.pop();

            // If the last character in the result string is the same as the current character
            if (result.length() > 0 && result.back() == first.second) {
                // If the heap is empty, it's impossible to reorganize the string
                if (maxHeap.empty()) {
                    return "";
                }

                // Get the character with the next highest frequency
                pair<int, char> second = maxHeap.top();
                maxHeap.pop();

                // Append the character with the next highest frequency to the result string
                result += second.second;

                // Decrease the frequency of the character with the next highest frequency
                second.first--;

                // Push the character with the next highest frequency back into the heap
                if (second.first > 0) {
                    maxHeap.push(second);
                }

                // Push the character with the highest frequency back into the heap
                maxHeap.push(first);
            } else {
                // Append the character with the highest frequency to the result string
                result += first.second;

                // Decrease the frequency of the character with the highest frequency
                first.first--;

                // Push the character with the highest frequency back into the heap
                if (first.first > 0) {
                    maxHeap.push(first);
                }
            }
        }

        return result;
    }
};
```

## Test Cases
```
Input: s = "aab"
Output: "aba"
Input: s = "aaab"
Output: ""
```

## Key Takeaways
- Use a max heap to store the frequency of each character.
- Always try to append the character with the highest frequency to the result string.
- If the last character in the result string is the same as the character we want to append, use the character with the next highest frequency instead.