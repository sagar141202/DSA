# K Closest Points to Origin

## Problem Statement
Given an array of points where points[i] = [xi, yi] represents a point on a 2D plane, find the k closest points to the origin (0, 0). The distance between two points (x1, y1) and (x2, y2) is calculated as sqrt((x2 - x1)^2 + (y2 - y1)^2). Return the k closest points. You may return the answer in any order. The answer is guaranteed to be unique (no two points have the same distance to the origin). 0 < k <= points.length <= 10^4, -10^4 < xi, yi < 10^4.

## Approach
We can use a priority queue to solve this problem, where the priority of each point is its distance to the origin. We will push all points into the priority queue and then pop the k smallest points. Alternatively, we can use a custom comparator with the nth_element function or sort function to achieve the same result more efficiently.

## Complexity
- Time: O(n log k)
- Space: O(k)

## C++ Solution
```cpp
#include <queue>
#include <vector>
#include <iostream>

using namespace std;

struct Point {
    int x, y;
};

struct Comparator {
    bool operator()(const Point& p1, const Point& p2) {
        int dist1 = p1.x * p1.x + p1.y * p1.y;
        int dist2 = p2.x * p2.x + p2.y * p2.y;
        return dist1 > dist2;
    }
};

vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
    priority_queue<Point, vector<Point>, Comparator> pq;
    for (const auto& point : points) {
        Point p;
        p.x = point[0];
        p.y = point[1];
        if (pq.size() < k) {
            pq.push(p);
        } else {
            if (point[0] * point[0] + point[1] * point[1] < pq.top().x * pq.top().x + pq.top().y * pq.top().y) {
                pq.pop();
                pq.push(p);
            }
        }
    }

    vector<vector<int>> result;
    while (!pq.empty()) {
        Point p = pq.top();
        pq.pop();
        result.push_back({p.x, p.y});
    }
    return result;
}

int main() {
    vector<vector<int>> points = {{1, 3}, {-2, 2}};
    int k = 1;
    vector<vector<int>> result = kClosest(points, k);
    for (const auto& point : result) {
        cout << "[" << point[0] << ", " << point[1] << "]" << endl;
    }
    return 0;
}
```

## Test Cases
```
Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]
```

## Key Takeaways
- The priority queue can be used to keep track of the k smallest elements.
- The Comparator struct is used to define the priority of each point in the priority queue.
- The distance between two points is calculated as the sum of the squares of the differences in their x and y coordinates.