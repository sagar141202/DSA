# Task Scheduler

## Problem Statement
Given a list of tasks and a cooldown period, schedule the tasks such that no two same tasks are executed within the cooldown period. The tasks are represented by characters, and the cooldown period is an integer. Return the least number of units of time that the CPU will take to finish all the given data. For example, if the tasks are ["A","A","A","B","B","B"] and the cooldown period is 2, the CPU will take 8 units of time to finish all the tasks, with the schedule being "ABABAB". The constraints are 1 <= task.length <= 10000 and 0 <= n < 100.

## Approach
We can use a priority queue to store the tasks along with their frequencies. The task with the highest frequency is executed first. We also use a queue to store the tasks that are in the cooldown period. The algorithm sorts the tasks based on their frequencies and then constructs the schedule.

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
        for (auto& it : freq) {
            maxFreq = max(maxFreq, it.second);
        }
        
        // Calculate the number of tasks with maximum frequency
        int maxFreqCount = 0;
        for (auto& it : freq) {
            if (it.second == maxFreq) {
                maxFreqCount++;
            }
        }
        
        // Calculate the least number of units of time
        return max((int)tasks.size(), (maxFreq - 1) * (n + 1) + maxFreqCount);
    }
};
```

## Test Cases
```
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
```

## Key Takeaways
- Use a frequency map to store the frequency of each task.
- Calculate the maximum frequency and the number of tasks with maximum frequency.
- Use the formula (maxFreq - 1) * (n + 1) + maxFreqCount to calculate the least number of units of time.