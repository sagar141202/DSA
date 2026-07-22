# Task Scheduler

## Problem Statement
Given a char array representing tasks CPU need to do. It contains capital letters A to Z. Each letter represents a different task. Tasks could be done without original order. Each task could be done one at a time. For each task, there is a cooldown interval: after completing a task, the CPU cannot do the same task again for n intervals. Return the least number of units of times that the CPU will take to finish all the given tasks. Example: tasks = ["A","A","A","B","B","B"], n = 2, output = 8, because the order is A -> B -> idle -> idle -> A -> B -> idle -> idle.

## Approach
The algorithm uses a priority queue to store the frequency of each task and a cooldown queue to handle the cooldown interval. The idea is to always execute the task with the highest frequency first and update the cooldown queue accordingly.

## Complexity
- Time: O(n log k)
- Space: O(k)

## C++ Solution
```cpp
#include <queue>
#include <unordered_map>
#include <vector>

class Solution {
public:
    int leastInterval(std::vector<char>& tasks, int n) {
        // count frequency of each task
        std::unordered_map<char, int> freq;
        for (char task : tasks) {
            freq[task]++;
        }

        // priority queue to store tasks
        std::priority_queue<int> pq;
        for (auto& pair : freq) {
            pq.push(pair.second);
        }

        int time = 0;
        std::queue<std::pair<int, int>> cooldown;

        while (!pq.empty() || !cooldown.empty()) {
            // add tasks back to pq from cooldown
            if (!cooldown.empty() && cooldown.front().second == time) {
                pq.push(cooldown.front().first);
                cooldown.pop();
            }

            // execute the task with the highest frequency
            if (!pq.empty()) {
                int freq = pq.top();
                pq.pop();
                if (freq > 1) {
                    cooldown.push({freq - 1, time + n + 1});
                }
            }

            time++;
        }

        return time;
    }
};
```

## Test Cases
```
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
```

## Key Takeaways
- Use a priority queue to store the frequency of each task.
- Use a cooldown queue to handle the cooldown interval.
- Always execute the task with the highest frequency first and update the cooldown queue accordingly.