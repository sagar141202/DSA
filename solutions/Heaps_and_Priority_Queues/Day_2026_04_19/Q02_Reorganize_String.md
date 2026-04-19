# Reorganize String

## Problem Statement
Given a string `s`, reorganize the characters in the string such that no two adjacent characters are the same. If it is impossible to reorganize the string, return an empty string. The string consists of lowercase English letters, and the length of the string is at most 100. For example, given `s = "aab"`, the output should be `"aba"`. However, for `s = "aaab"`, it is impossible to reorganize the string, so the output should be `""`.

## Approach
We can use a priority queue to store the frequency of each character in the string. We then pop the two characters with the highest frequency from the queue and append them to the result string. This approach ensures that no two adjacent characters are the same.

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
        // Create a frequency map of characters
        unordered_map<char, int> freq;
        for (char c : s) {
            freq[c]++;
        }
        
        // Create a priority queue to store characters and their frequencies
        priority_queue<pair<int, char>> pq;
        for (auto& it : freq) {
            pq.push({it.second, it.first});
        }
        
        string result;
        while (!pq.empty()) {
            // Get the two characters with the highest frequency
            pair<int, char> first = pq.top();
            pq.pop();
            if (pq.empty()) {
                // If there is only one character left, check if it can be appended to the result
                if (result.size() > 0 && result.back() == first.second) {
                    return "";
                }
                result += first.second;
                break;
            }
            pair<int, char> second = pq.top();
            pq.pop();
            
            // Append the characters to the result string
            result += first.second;
            result += second.second;
            
            // Update the frequencies and push back to the priority queue
            if (first.first > 1) {
                pq.push({first.first - 1, first.second});
            }
            if (second.first > 1) {
                pq.push({second.first - 1, second.second});
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
- Use a priority queue to store characters and their frequencies.
- Pop the two characters with the highest frequency from the queue and append them to the result string.
- Update the frequencies and push back to the priority queue if necessary.