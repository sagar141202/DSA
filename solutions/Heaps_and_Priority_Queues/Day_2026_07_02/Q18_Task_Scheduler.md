# Task Scheduler

## Problem Statement
Given a list of tasks and a cool down period, schedule the tasks such that the same task is not executed within the cool down period. The tasks are represented by characters and the cool down period is an integer. The function should return the least number of time units required to schedule all tasks. For example, if tasks = ['A','A','A','B','B','B'] and cool_down = 2, the function should return 8 because the schedule would be A -> B -> idle -> A -> B -> idle -> A -> B.

## Approach
The approach to solve this problem is to use a priority queue to store the frequency of each task and a queue to store the tasks that are in the cool down period. We then iterate over the tasks, incrementing the frequency of each task and pushing it into the priority queue. If the size of the priority queue is greater than the cool down period, we pop the task with the highest frequency from the priority queue and push it into the cool down queue.

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
        int max_freq = 0;
        for (auto& it : freq) {
            max_freq = max(max_freq, it.second);
        }

        // Calculate the number of tasks with maximum frequency
        int max_freq_count = 0;
        for (auto& it : freq) {
            if (it.second == max_freq) {
                max_freq_count++;
            }
        }

        // Calculate the least number of time units required
        int time_units = (max_freq - 1) * (n + 1) + max_freq_count;
        return max((int)tasks.size(), time_units);
    }
};
```

## Test Cases
```
Input: tasks = ['A','A','A','B','B','B'], n = 2
Output: 8
Input: tasks = ['A','A','A','B','B','B'], n = 0
Output: 6
Input: tasks = ['A','A','A','A','A','A','B','C','D','E','F','G'], n = 2
Output: 16
```

## Key Takeaways
- Use a frequency map to store the frequency of each task.
- Calculate the maximum frequency and the number of tasks with maximum frequency.
- Calculate the least number of time units required using the formula (max_freq - 1) * (n + 1) + max_freq_count.
- Return the maximum of the total number of tasks and the calculated time units.