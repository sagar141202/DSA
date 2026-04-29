# Task Scheduler

## Problem Statement
Given a char array representing tasks CPU need to do. It contains capital letters A to Z. Each letter represents a different task. Tasks could be done without original order. Each task could be done one at a time and only once every n iterations. For example, given tasks CPU task = ["A","A","A","B","B","B"], n = 2, then the output is 8, because CPU will complete these tasks in 8 units of time. The same tasks will be executed every 2 units, i.e., "A" will be executed at t = 0, 2, 4, 6 and "B" will be executed at t = 1, 3, 5, 7.

## Approach
To solve this problem, we can use a max heap to keep track of the tasks with the highest frequency. We will also use a queue to store the tasks that are waiting to be executed. The algorithm will iterate over the tasks, push them into the max heap, and then pop the tasks from the heap and execute them.

## Complexity
- Time: O(n log k)
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
- Use a max heap to keep track of the tasks with the highest frequency.
- Use a queue to store the tasks that are waiting to be executed.
- The algorithm will iterate over the tasks, push them into the max heap, and then pop the tasks from the heap and execute them.