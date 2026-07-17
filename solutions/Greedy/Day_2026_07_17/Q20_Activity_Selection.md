# Activity Selection

## Problem Statement
Given a set of activities with their start and finish times, select the maximum number of activities that can be performed by a single person, assuming that a person can only work on a single activity at a time. The activities are represented as pairs of integers, where the first integer is the start time and the second integer is the finish time. The goal is to maximize the number of activities that can be performed without any conflicts.

## Approach
The algorithm sorts the activities based on their finish times and then iterates through the sorted list, selecting the activities that do not conflict with the previously selected activities. This approach ensures that the maximum number of activities can be performed.

## Complexity
- Time: O(n log n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

bool compare(vector<int>& a, vector<int>& b) {
    return a[1] < b[1];
}

int activitySelection(vector<vector<int>>& activities) {
    // Sort the activities based on their finish times
    sort(activities.begin(), activities.end(), compare);

    int count = 1;
    int finish = activities[0][1];

    // Iterate through the sorted list of activities
    for (int i = 1; i < activities.size(); i++) {
        // If the current activity does not conflict with the previously selected activity, select it
        if (activities[i][0] >= finish) {
            count++;
            finish = activities[i][1];
        }
    }

    return count;
}

int main() {
    vector<vector<int>> activities = {{1, 4}, {3, 5}, {0, 6}, {5, 7}, {3, 8}, {5, 9}, {6, 10}, {8, 11}, {8, 12}, {2, 13}, {12, 14}};
    cout << "Maximum number of activities: " << activitySelection(activities);
    return 0;
}
```

## Test Cases
```
Input: [[1, 4], [3, 5], [0, 6], [5, 7], [3, 8], [5, 9], [6, 10], [8, 11], [8, 12], [2, 13], [12, 14]]
Output: 4
```

## Key Takeaways
- The greedy algorithm is used to solve the activity selection problem.
- The activities are sorted based on their finish times to ensure that the maximum number of activities can be performed.
- The algorithm iterates through the sorted list of activities and selects the activities that do not conflict with the previously selected activities.