# Task Scheduler

## Problem Statement
Given a list of tasks and a cool down period, schedule the tasks to minimize the total time. Each task can only be scheduled once every cool down period. The tasks are represented by characters and the cool down period is given by an integer. For example, if we have tasks = ["A","A","A","B","B","B"] and cool down period = 2, then the schedule would be "ABABAB" or any other valid schedule.

## Approach
We use a priority queue to store the tasks and their frequencies. We then use a queue to store the tasks that are cooling down. The task with the highest frequency is scheduled first.

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
        unordered_map<char, int> freq;
        for (char task : tasks) {
            freq[task]++;
        }
        
        priority_queue<int> pq;
        for (auto& it : freq) {
            pq.push(it.second);
        }
        
        int time = 0;
        queue<pair<int, int>> cool;
        while (!pq.empty() || !cool.empty()) {
            if (!pq.empty()) {
                int count = pq.top();
                pq.pop();
                count--;
                if (count > 0) {
                    cool.push({count, time + n});
                }
            }
            time++;
            while (!cool.empty() && cool.front().second == time) {
                pq.push(cool.front().first);
                cool.pop();
            }
        }
        return time;
    }
};

int main() {
    Solution solution;
    vector<char> tasks = {'A', 'A', 'A', 'B', 'B', 'B'};
    int n = 2;
    cout << solution.leastInterval(tasks, n) << endl;
    return 0;
}
```

## Test Cases
```
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Input: tasks = ["A","A","A","B","B","B"], n = 0
Output: 6
```

## Key Takeaways
- Use a priority queue to store tasks based on their frequencies.
- Use a queue to store tasks that are cooling down.
- Schedule the task with the highest frequency first.