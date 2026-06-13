# Reorganize String

## Problem Statement
Given a string `s`, reorganize the characters in the string such that no two adjacent characters are the same. If it is not possible to reorganize the string, return an empty string. The string consists of lowercase English letters and the length of the string is in the range [1, 50000]. For example, given the string "aab", the function should return "aba". If the string "aa" is given, the function should return an empty string because it is not possible to reorganize the string.

## Approach
We can use a max heap to store the frequency of each character in the string. Then, we can pop the two most frequent characters from the heap, add them to the result string, and push them back into the heap with their frequencies decremented. This process continues until the heap is empty or it is not possible to reorganize the string.

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
        unordered_map<char, int> freq;
        for (char c : s) {
            freq[c]++;
        }
        
        // Create a max heap
        priority_queue<pair<int, char>> maxHeap;
        for (auto& it : freq) {
            maxHeap.push({it.second, it.first});
        }
        
        string result;
        while (!maxHeap.empty()) {
            // Get the two most frequent characters
            pair<int, char> first = maxHeap.top();
            maxHeap.pop();
            if (maxHeap.empty()) {
                // If there is only one character left and its frequency is more than 1, return an empty string
                if (first.first > 1) {
                    return "";
                } else {
                    result += first.second;
                    break;
                }
            }
            pair<int, char> second = maxHeap.top();
            maxHeap.pop();
            
            // Add the characters to the result string
            result += first.second;
            result += second.second;
            
            // Decrement the frequencies and push back into the heap if necessary
            if (first.first > 1) {
                maxHeap.push({first.first - 1, first.second});
            }
            if (second.first > 1) {
                maxHeap.push({second.first - 1, second.second});
            }
        }
        return result;
    }
};
```

## Test Cases
```
Input: "aab"
Output: "aba"
Input: "aa"
Output: ""
```

## Key Takeaways
- Use a max heap to store the frequency of each character in the string.
- Pop the two most frequent characters from the heap, add them to the result string, and push them back into the heap with their frequencies decremented.
- If it is not possible to reorganize the string, return an empty string.