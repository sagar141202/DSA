# Activity Selection

## Problem Statement
Given a set of activities with their start and finish times, select the maximum number of activities that can be performed by a single person, assuming that a person can only work on a single activity at a time. The activities are represented as pairs of integers (start, finish), where start is the start time and finish is the finish time of the activity. The goal is to select the maximum number of non-overlapping activities.

## Approach
The approach is to sort the activities by their finish times and then select the activities greedily. The intuition is that by selecting the activity with the earliest finish time, we are leaving the maximum amount of time for the next activity.

## Complexity
- Time: O(n log n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

// Define a struct to represent an activity
struct Activity {
    int start, finish;
};

// Compare function to sort activities by finish time
bool compare Activities(Activity a, Activity b) {
    return a.finish < b.finish;
}

int activitySelection(vector<Activity>& activities) {
    // Sort activities by finish time
    sort(activities.begin(), activities.end(), compareActivities);
    
    // Initialize count of selected activities
    int count = 1;
    
    // Initialize finish time of last selected activity
    int lastFinish = activities[0].finish;
    
    // Iterate through activities
    for (int i = 1; i < activities.size(); i++) {
        // If current activity starts after last selected activity finishes, select it
        if (activities[i].start >= lastFinish) {
            count++;
            lastFinish = activities[i].finish;
        }
    }
    
    return count;
}

int main() {
    // Example usage:
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
- Sort the activities by their finish times to ensure that we are considering the activities that finish earliest first.
- Select the activities greedily based on their start times and the finish time of the last selected activity.
- This approach ensures that we are selecting the maximum number of non-overlapping activities.