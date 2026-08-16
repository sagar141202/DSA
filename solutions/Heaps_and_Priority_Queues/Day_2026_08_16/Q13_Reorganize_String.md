# Reorganize String

## Problem Statement
Given a string `s`, reorganize the characters in the string such that no two adjacent characters are the same. If it is impossible to reorganize the string, return an empty string. The string consists of lowercase English letters and has a length of at most 100. For example, given the string "aab", the reorganized string would be "aba". If the string "aaab" is given, it is impossible to reorganize the string, so an empty string is returned.

## Approach
The solution utilizes a max heap to store the frequency of each character. The max heap is used to ensure that the most frequent character is always processed first. The algorithm iterates over the max heap, appending the most frequent character to the result string and updating the frequency of the character.

## Complexity
- Time: O(N log N)
- Space: O(N)

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

        // Create a max heap to store the frequency of characters
        priority_queue<pair<int, char>> maxHeap;
        for (auto& it : freq) {
            maxHeap.push({it.second, it.first});
        }

        string result;
        while (!maxHeap.empty()) {
            // Get the most frequent character
            pair<int, char> first = maxHeap.top();
            maxHeap.pop();

            // If the result string is not empty and the last character is the same as the most frequent character
            if (!result.empty() && result.back() == first.second) {
                // If the max heap is empty, it is impossible to reorganize the string
                if (maxHeap.empty()) {
                    return "";
                }

                // Get the second most frequent character
                pair<int, char> second = maxHeap.top();
                maxHeap.pop();

                // Append the second most frequent character to the result string
                result.push_back(second.second);

                // Decrement the frequency of the second most frequent character
                second.first--;

                // If the frequency of the second most frequent character is greater than 0, push it back to the max heap
                if (second.first > 0) {
                    maxHeap.push(second);
                }

                // Push the most frequent character back to the max heap
                maxHeap.push(first);
            } else {
                // Append the most frequent character to the result string
                result.push_back(first.second);

                // Decrement the frequency of the most frequent character
                first.first--;

                // If the frequency of the most frequent character is greater than 0, push it back to the max heap
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
Input: "aab"
Output: "aba"
Input: "aaab"
Output: ""
```

## Key Takeaways
- The use of a max heap to store the frequency of characters ensures that the most frequent character is always processed first.
- The algorithm iterates over the max heap, appending the most frequent character to the result string and updating the frequency of the character.
- If the result string is not empty and the last character is the same as the most frequent character, the algorithm uses the second most frequent character to ensure that no two adjacent characters are the same.