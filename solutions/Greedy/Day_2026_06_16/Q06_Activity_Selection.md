# Activity Selection

## Problem Statement
Given a set of activities with their start and finish times, select the maximum number of activities that can be performed by a single person, assuming that a person can only work on a single activity at a time. The activities are given as pairs of start and finish times. The goal is to find the maximum number of activities that do not conflict with each other. For example, if we have two activities with start and finish times (1, 4) and (3, 5), they conflict with each other because they overlap. However, activities (1, 2) and (3, 4) do not conflict.

## Approach
The algorithm sorts the activities based on their finish times and then iterates through the sorted list, selecting the activities that do not conflict with the previously selected activity. This approach ensures that we always choose the activity with the earliest finish time, allowing us to select the maximum number of activities.

## Complexity
- Time: O(n log n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

struct Activity {
    int start, finish;
};

bool compareActivities(const Activity &a, const Activity &b) {
    return a.finish < b.finish;
}

int activitySelection(vector<Activity> &activities) {
    // Sort activities based on their finish times
    sort(activities.begin(), activities.end(), compareActivities);
    
    int count = 1;  // Initialize count of selected activities
    int lastFinish = activities[0].finish;  // Finish time of last selected activity
    
    // Iterate through the sorted activities
    for (int i = 1; i < activities.size(); i++) {
        // If the current activity does not conflict with the last selected activity
        if (activities[i].start >= lastFinish) {
            count++;  // Increment the count of selected activities
            lastFinish = activities[i].finish;  // Update the finish time of last selected activity
        }
    }
    
    return count;
}

int main() {
    vector<Activity> activities = {{1, 4}, {3, 5}, {0, 6}, {5, 7}, {3, 8}, {5, 9}, {6, 10}, {8, 11}, {8, 12}, {2, 13}, {12, 14}};
    cout << "Maximum number of activities: " << activitySelection(activities) << endl;
    return 0;
}
```

## Test Cases
```
Input: [(1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9), (6, 10), (8, 11), (8, 12), (2, 13), (12, 14)]
Output: 4
```

## Key Takeaways
- The problem can be solved using a greedy approach by sorting the activities based on their finish times.
- The algorithm selects the activities that do not conflict with the previously selected activity, ensuring the maximum number of activities are selected.
- The time complexity of the algorithm is O(n log n) due to the sorting operation.