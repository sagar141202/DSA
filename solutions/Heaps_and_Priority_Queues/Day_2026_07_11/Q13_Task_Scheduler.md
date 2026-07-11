# Task Scheduler

## Problem Statement
Given a list of tasks and a cool down period, schedule the tasks to minimize the total time. Each task can only be executed once every cool down period. The function should return the least number of units of time that the CPU will take to finish all the tasks. For example, if tasks = ["A","A","A","B","B","B"], n = 2, then the function should return 8 because the optimal schedule would be "ABABABAB".

## Approach
This problem can be solved using a max heap to store the frequency of each task and a queue to store the tasks that are cooling down. The max heap will ensure that the task with the highest frequency is executed first. The queue will keep track of the tasks that are cooling down and will add them back to the max heap when the cool down period is over.

## Complexity
- Time: O(N log N)
- Space: O(N)

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
- The max heap is used to store the frequency of each task, ensuring the task with the highest frequency is executed first.
- The queue is used to store the tasks that are cooling down, adding them back to the max heap when the cool down period is over.
- The time complexity is O(N log N) due to the use of the max heap, where N is the number of tasks.