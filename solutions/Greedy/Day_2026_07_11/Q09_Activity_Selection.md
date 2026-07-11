# Activity Selection

## Problem Statement
Given a set of activities with their start and finish times, select the maximum number of activities that can be performed by a single person, assuming that a person can only work on a single activity at a time. The activities are given as pairs of integers (start, finish), where start is the start time of the activity and finish is the finish time of the activity. The goal is to find the maximum number of activities that can be selected such that no two activities overlap. For example, if we have the following activities: (1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9), (6, 10), the maximum number of activities that can be selected is 4, which are (1, 4), (5, 7), (6, 10).

## Approach
The algorithm uses a greedy approach to select the activities. It first sorts the activities based on their finish times and then iterates through the sorted activities, selecting the activities that do not overlap with the previously selected activities. The key idea is to always select the activity with the earliest finish time.

## Complexity
- Time: O(n log n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

// Define a structure to represent an activity
struct Activity {
    int start, finish;
};

// Compare function to sort activities based on finish time
bool compare(Activity a, Activity b) {
    return a.finish < b.finish;
}

// Function to select the maximum number of activities
int activitySelection(vector<Activity> activities) {
    // Sort the activities based on finish time
    sort(activities.begin(), activities.end(), compare);
    
    // Initialize the count of selected activities
    int count = 0;
    
    // Initialize the finish time of the last selected activity
    int lastFinish = -1;
    
    // Iterate through the sorted activities
    for (Activity activity : activities) {
        // Check if the current activity does not overlap with the last selected activity
        if (activity.start >= lastFinish) {
            // Select the current activity
            count++;
            // Update the finish time of the last selected activity
            lastFinish = activity.finish;
        }
    }
    
    // Return the count of selected activities
    return count;
}

int main() {
    // Example usage
    vector<Activity> activities = {{1, 4}, {3, 5}, {0, 6}, {5, 7}, {3, 8}, {5, 9}, {6, 10}};
    int count = activitySelection(activities);
    cout << "Maximum number of activities: " << count << endl;
    return 0;
}
```

## Test Cases
```
Input: [(1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9), (6, 10)]
Output: 4
```

## Key Takeaways
- The greedy approach is used to select the activities based on their finish times.
- The activities are sorted based on their finish times to ensure that the activity with the earliest finish time is always selected first.
- The algorithm has a time complexity of O(n log n) due to the sorting step.