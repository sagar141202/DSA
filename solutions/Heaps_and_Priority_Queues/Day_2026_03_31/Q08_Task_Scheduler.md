# Task Scheduler

## Problem Statement
Given a list of tasks and a cool-down period, schedule the tasks such that no two same tasks are executed within the cool-down period. The tasks are represented by uppercase letters (A-Z) and the cool-down period is an integer. The goal is to find the least number of time units required to schedule all tasks. For example, if tasks = ["A","A","A","B","B","B"], n = 2, the output should be 8 because the optimal schedule would be "ABABABCA" where "C" represents an idle unit.

## Approach
The approach involves using a priority queue to store the tasks that need to be scheduled, along with their cool-down periods. We also use a map to keep track of the last time each task was executed. The algorithm iterates over the tasks, checks if the task can be executed, and updates the last execution time and the priority queue accordingly.

## Complexity
- Time: O(n log n)
- Space: O(n)

## C++ Solution
```cpp
#include <queue>
#include <unordered_map>
#include <vector>
using namespace std;

class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
        // Create a frequency map of tasks
        unordered_map<char, int> freq;
        for (char task : tasks) {
            freq[task]++;
        }

        // Create a priority queue to store tasks
        priority_queue<int> pq;
        for (auto& it : freq) {
            pq.push(it.second);
        }

        int time = 0;
        while (!pq.empty()) {
            // Store the tasks that are going to be executed in the current cycle
            vector<int> temp;
            for (int i = 0; i <= n; i++) {
                if (!pq.empty()) {
                    temp.push_back(pq.top());
                    pq.pop();
                }
            }

            // Update time
            time += (temp.size() == n + 1) ? n + 1 : temp.size();

            // Add tasks back to the priority queue if they have remaining frequency
            for (int i = 0; i < temp.size(); i++) {
                if (temp[i] - 1 > 0) {
                    pq.push(temp[i] - 1);
                }
            }
        }

        return time;
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
- Use a priority queue to store tasks that need to be scheduled, along with their frequencies.
- Use a map to keep track of the last time each task was executed.
- The algorithm iterates over the tasks and updates the last execution time and the priority queue accordingly.