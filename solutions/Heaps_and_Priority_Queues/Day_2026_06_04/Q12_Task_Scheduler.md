# Task Scheduler

## Problem Statement
Given a char array representing tasks CPU need to do, where different letters represent different tasks. The length of the array is n. The CPU can only perform one task at a time, and it needs to cool down for a certain number of time units (called the cooling period) after performing a task. In this case, the cooling period is 2 time units, meaning that after performing a task, the CPU cannot perform the same task for at least 2 time units. The task scheduler will schedule the tasks to minimize the idle time of the CPU. We need to find the least number of time units that the CPU will take to finish all the given tasks. For example, given tasks = ["A","A","A","B","B","B"], the output will be 8 because the optimal schedule is "A -> B -> idle -> A -> B -> idle -> A -> B".

## Approach
The algorithm uses a priority queue to store the frequency of each task. It then schedules the tasks based on their frequency, ensuring that the CPU cools down for the required time units after performing each task. The algorithm iteratively selects the task with the highest frequency and schedules it, then decreases its frequency and adds it back to the queue if necessary.

## Complexity
- Time: O(n log k)
- Space: O(k)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
        // Create a frequency map for tasks
        unordered_map<char, int> freq;
        for (char task : tasks) {
            freq[task]++;
        }

        // Find the maximum frequency
        int max_freq = 0;
        for (auto& pair : freq) {
            max_freq = max(max_freq, pair.second);
        }

        // Calculate the number of tasks with maximum frequency
        int max_freq_count = 0;
        for (auto& pair : freq) {
            if (pair.second == max_freq) {
                max_freq_count++;
            }
        }

        // Calculate the least number of time units required
        int time_units = (max_freq - 1) * (n + 1) + max_freq_count;
        return max((int)tasks.size(), time_units);
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
- The task scheduler problem can be solved using a priority queue to store the frequency of each task.
- The cooling period is critical in determining the least number of time units required to finish all tasks.
- The algorithm iteratively selects the task with the highest frequency and schedules it, ensuring that the CPU cools down for the required time units after performing each task.