# Reorganize String

## Problem Statement
Given a string with characters and their frequencies, reorganize the string such that no two adjacent characters are the same. The string can be reorganized using a priority queue or a max heap to store the characters and their frequencies. If the string cannot be reorganized, return an empty string. The input string will contain only lowercase English letters and will have a length between 1 and 10^5. The frequency of each character will be between 1 and 10^5.

## Approach
The algorithm uses a max heap to store characters and their frequencies, then constructs the reorganized string by popping the most frequent characters from the heap and appending them to the result string. If at any point the most frequent character is the same as the last character in the result string, the second most frequent character is used instead.

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
        // Create a frequency map for the input string
        unordered_map<char, int> freq;
        for (char c : s) {
            freq[c]++;
        }

        // Create a max heap to store characters and their frequencies
        priority_queue<pair<int, char>> maxHeap;
        for (auto& pair : freq) {
            maxHeap.push({pair.second, pair.first});
        }

        // Initialize the result string and a variable to store the last character
        string result;
        char lastChar = '\0';

        while (!maxHeap.empty()) {
            // Get the most frequent character from the max heap
            pair<int, char> top = maxHeap.top();
            maxHeap.pop();

            // If the most frequent character is the same as the last character, use the second most frequent character
            if (top.second == lastChar && maxHeap.empty()) {
                return "";
            } else if (top.second == lastChar) {
                pair<int, char> second = maxHeap.top();
                maxHeap.pop();
                result.push_back(second.second);
                if (--second.first > 0) {
                    maxHeap.push(second);
                }
                lastChar = second.second;
            } else {
                result.push_back(top.second);
                if (--top.first > 0) {
                    maxHeap.push(top);
                }
                lastChar = top.second;
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
- Use a max heap or priority queue to store characters and their frequencies for efficient reorganization.
- Keep track of the last character in the result string to avoid adjacent characters being the same.
- Handle edge cases where the most frequent character is the same as the last character in the result string.