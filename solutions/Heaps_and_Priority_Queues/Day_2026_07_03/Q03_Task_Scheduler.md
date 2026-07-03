# Task Scheduler

## Problem Statement
Given a list of tasks and a cooling period, schedule the tasks such that the maximum time is utilized and no two same tasks are executed within the cooling period. The tasks are represented by characters and the cooling period is given by an integer. For example, if the tasks are ['A', 'A', 'A', 'B', 'B', 'B'] and the cooling period is 2, the tasks should be scheduled as "ABABAB" or any other valid scheduling to maximize the CPU utilization.

## Approach
The approach is to use a priority queue to store the tasks along with their frequencies. The task with the highest frequency is executed first and then it is pushed back into the queue after the cooling period.

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
        
        int maxFreq = 0;
        int maxFreqCount = 0;
        for (auto& pair : freq) {
            if (pair.second > maxFreq) {
                maxFreq = pair.second;
                maxFreqCount = 1;
            } else if (pair.second == maxFreq) {
                maxFreqCount++;
            }
        }
        
        int ans = (maxFreq - 1) * (n + 1) + maxFreqCount;
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
- The use of a priority queue is not necessary in this problem, a simple unordered map can be used to store the frequency of tasks.
- The maximum frequency of a task is used to calculate the minimum time required to schedule all tasks.
- The cooling period is used to calculate the idle time slots in the schedule.