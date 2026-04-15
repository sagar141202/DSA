# Task Scheduler

## Problem Statement
Given a char array representing tasks CPU need to do. It contains capital letters A to Z. Each letter represents a different task. Tasks could be done without original order. Each task could be done one time at least. The platform can finish all tasks but the order doesn't matter. For each task, there is a cooldown interval: the gap between two same tasks. Find the least number of units of times that the CPU will take to finish all the given tasks with the given constraints. For example, tasks = ["A","A","A","B","B","B"], n = 2, the output will be 8 because one possible answer is A -> B -> idle -> A -> B -> idle -> A -> B.

## Approach
The algorithm uses a priority queue to store the frequency of each task and a cooldown queue to store the tasks that are cooling down. The time complexity is reduced by utilizing the max heap to always select the task with the highest frequency. This ensures that the CPU is always busy with the task that has the highest priority.

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
        unordered_map<char, int> count;
        for (char task : tasks) {
            count[task]++;
        }
        
        int maxCount = 0;
        int maxCountTasks = 0;
        for (auto& pair : count) {
            if (pair.second > maxCount) {
                maxCount = pair.second;
                maxCountTasks = 1;
            } else if (pair.second == maxCount) {
                maxCountTasks++;
            }
        }
        
        int ans = (maxCount - 1) * (n + 1) + maxCountTasks;
        return max((int)tasks.size(), ans);
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
- The key to solving this problem is to use a max heap to store the frequency of each task.
- We need to consider the cooldown interval when scheduling the tasks.
- The answer is the maximum of the total number of tasks and the calculated answer.