# Activity Selection

## Problem Statement
Given a set of activities with their start and finish times, select the maximum number of activities that can be performed by a single person, assuming that a person can only work on a single activity at a time. The activities are represented as pairs of integers, where the first integer is the start time and the second integer is the finish time. The goal is to find the maximum number of non-overlapping activities.

## Approach
The algorithm sorts the activities by their finish times and then iterates through the sorted list, selecting the activities that do not overlap with the previously selected activity. This approach ensures that the maximum number of non-overlapping activities are selected. The key intuition is to always choose the activity with the earliest finish time.

## Complexity
- Time: O(n log n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

// Define a structure to represent an activity
struct Activity {
    int start;
    int finish;
};

// Comparison function to sort activities by finish time
bool compareActivities(const Activity &a, const Activity &b) {
    return a.finish < b.finish;
}

// Function to select the maximum number of non-overlapping activities
int selectActivities(vector<Activity> &activities) {
    // Sort the activities by their finish times
    sort(activities.begin(), activities.end(), compareActivities);

    // Initialize the count of selected activities
    int count = 1;

    // Initialize the finish time of the last selected activity
    int lastFinish = activities[0].finish;

    // Iterate through the sorted list of activities
    for (int i = 1; i < activities.size(); i++) {
        // Check if the current activity does not overlap with the last selected activity
        if (activities[i].start >= lastFinish) {
            // Increment the count of selected activities
            count++;

            // Update the finish time of the last selected activity
            lastFinish = activities[i].finish;
        }
    }

    // Return the maximum number of non-overlapping activities
    return count;
}

int main() {
    // Example usage
    vector<Activity> activities = {{1, 2}, {3, 4}, {0, 6}, {5, 7}, {8, 9}, {5, 9}};
    cout << "Maximum number of non-overlapping activities: " << selectActivities(activities) << endl;
    return 0;
}
```

## Test Cases
```
Input: [(1, 2), (3, 4), (0, 6), (5, 7), (8, 9), (5, 9)]
Output: 4
```

## Key Takeaways
- The greedy approach is suitable for this problem because it allows us to make the locally optimal choice (selecting the activity with the earliest finish time) that leads to a globally optimal solution.
- The time complexity of the algorithm is O(n log n) due to the sorting step, where n is the number of activities.
- The space complexity is O(1) because we only use a constant amount of space to store the count of selected activities and the finish time of the last selected activity.