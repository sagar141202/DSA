# Task Scheduler

## Problem Statement
Given a list of tasks and a cool down period, schedule the tasks such that the same task is not executed within the cool down period. The tasks are represented by characters and the cool down period is an integer. The function should return the least number of units of time that the CPU will take to finish all the given tasks. For example, if the tasks are ["A","A","A","B","B","B"] and the cool down period is 2, then the function should return 8 because the optimal schedule is "A -> B -> idle -> A -> B -> idle -> A -> B".

## Approach
The algorithm uses a priority queue to store the tasks and their frequencies. It iterates over the tasks, updates their frequencies, and pushes them into the priority queue. The task with the highest frequency is popped from the queue and executed. If the queue is empty, it adds idle time.

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
        // Create a frequency map
        unordered_map<char, int> freq;
        for (char task : tasks) {
            freq[task]++;
        }
        
        // Find the maximum frequency
        int maxFreq = 0;
        for (auto& it : freq) {
            maxFreq = max(maxFreq, it.second);
        }
        
        // Calculate the number of tasks with the maximum frequency
        int maxFreqCount = 0;
        for (auto& it : freq) {
            if (it.second == maxFreq) {
                maxFreqCount++;
            }
        }
        
        // Calculate the least number of units of time
        int ans = (maxFreq - 1) * (n + 1) + maxFreqCount;
        return max((int)tasks.size(), ans);
    }
};
```

## Test Cases
```
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Input: tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
Output: 16
```

## Key Takeaways
- The problem can be solved using a priority queue to store the tasks and their frequencies.
- The time complexity is O(n log n) due to the use of the priority queue.
- The space complexity is O(n) for storing the frequency map and the priority queue.