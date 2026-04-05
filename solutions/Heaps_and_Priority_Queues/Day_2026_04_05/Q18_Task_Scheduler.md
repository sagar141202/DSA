# Task Scheduler

## Problem Statement
Given a list of tasks and a cooling period, schedule the tasks such that the same task cannot be executed twice within the cooling period. The tasks are represented by characters, and the cooling period is an integer. The goal is to find the least number of time units required to schedule all tasks. The tasks are case-sensitive and there can be multiple tasks with the same character. For example, if the tasks are ["A","A","A","B","B","B"] and the cooling period is 2, the least number of time units required to schedule all tasks is 8.

## Approach
The algorithm uses a priority queue to store the frequency of each task and a queue to store the tasks that are cooling down. The task with the highest frequency is executed first, and then it is added to the cooling down queue. The time units are incremented until the cooling down queue is empty or the tasks are finished.

## Complexity
- Time: O(n log n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
        // Create a frequency map of tasks
        unordered_map<char, int> freq;
        for (char task : tasks) {
            freq[task]++;
        }
        
        // Find the maximum frequency
        int maxFreq = 0;
        for (auto& pair : freq) {
            maxFreq = max(maxFreq, pair.second);
        }
        
        // Calculate the number of tasks with maximum frequency
        int maxFreqCount = 0;
        for (auto& pair : freq) {
            if (pair.second == maxFreq) {
                maxFreqCount++;
            }
        }
        
        // Calculate the least number of time units required
        int timeUnits = (maxFreq - 1) * (n + 1) + maxFreqCount;
        return max((int)tasks.size(), timeUnits);
    }
};
```

## Test Cases
```
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Input: tasks = ["A","A","A","B","B","B"], n = 0
Output: 6
```

## Key Takeaways
- Use a frequency map to store the frequency of each task.
- Find the maximum frequency and the number of tasks with maximum frequency.
- Calculate the least number of time units required using the formula (maxFreq - 1) * (n + 1) + maxFreqCount.