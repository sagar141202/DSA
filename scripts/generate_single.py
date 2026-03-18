from groq import Groq
import os
import json
import random
import subprocess
from datetime import datetime
from pathlib import Path

# ─────────────────────────────────────────────
#  QUESTION BANK — All major DSA topics
# ─────────────────────────────────────────────
QUESTION_BANK = {
    "Arrays_and_Strings": [
        "Two Sum", "Best Time to Buy and Sell Stock", "Contains Duplicate",
        "Product of Array Except Self", "Maximum Subarray (Kadane's Algorithm)",
        "Maximum Product Subarray", "Find Minimum in Rotated Sorted Array",
        "Search in Rotated Sorted Array", "3Sum", "Container With Most Water",
        "Trapping Rain Water", "Sliding Window Maximum", "Longest Substring Without Repeating Characters",
        "Minimum Window Substring", "Group Anagrams", "Valid Anagram",
        "Rotate Array", "Move Zeroes", "Merge Intervals", "Insert Interval",
        "Spiral Matrix", "Set Matrix Zeroes", "Pascal's Triangle",
        "Next Permutation", "Jump Game", "Gas Station"
    ],
    "Trees_and_Graphs": [
        "Binary Tree Inorder Traversal", "Binary Tree Level Order Traversal",
        "Maximum Depth of Binary Tree", "Symmetric Tree", "Path Sum",
        "Construct Binary Tree from Preorder and Inorder Traversal",
        "Binary Tree Zigzag Level Order Traversal", "Lowest Common Ancestor of BST",
        "Validate Binary Search Tree", "Kth Smallest Element in BST",
        "Number of Islands", "Clone Graph", "Course Schedule (Topological Sort)",
        "Pacific Atlantic Water Flow", "Surrounded Regions",
        "Word Ladder", "Word Search", "Graph Valid Tree",
        "Redundant Connection", "Accounts Merge",
        "Serialize and Deserialize Binary Tree", "Binary Tree Maximum Path Sum",
        "Diameter of Binary Tree", "Right Side View of Binary Tree",
        "Invert Binary Tree", "Flatten Binary Tree to Linked List"
    ],
    "Dynamic_Programming": [
        "Climbing Stairs", "House Robber", "House Robber II",
        "Longest Common Subsequence", "Longest Increasing Subsequence",
        "Coin Change", "Word Break", "Combination Sum IV",
        "Partition Equal Subset Sum", "Target Sum",
        "Distinct Subsequences", "Edit Distance", "Regular Expression Matching",
        "Wildcard Matching", "Minimum Path Sum", "Unique Paths",
        "Decode Ways", "Jump Game II", "Burst Balloons",
        "Palindromic Substrings", "Longest Palindromic Subsequence",
        "Maximum Square of 1s", "Triangle Minimum Path", "Interleaving String",
        "Paint House", "Best Time to Buy and Sell Stock with Cooldown"
    ],
    "Linked_Lists": [
        "Reverse Linked List", "Linked List Cycle", "Linked List Cycle II",
        "Merge Two Sorted Lists", "Merge K Sorted Lists", "Remove Nth Node From End",
        "Reorder List", "Add Two Numbers", "Copy List with Random Pointer",
        "Flatten a Multilevel Doubly Linked List", "Rotate List",
        "Partition List", "Sort List", "Intersection of Two Linked Lists",
        "Remove Duplicates from Sorted List", "Odd Even Linked List"
    ],
    "Stacks_and_Queues": [
        "Valid Parentheses", "Min Stack", "Evaluate Reverse Polish Notation",
        "Daily Temperatures", "Car Fleet", "Largest Rectangle in Histogram",
        "Implement Queue using Stacks", "Implement Stack using Queues",
        "Decode String", "Asteroid Collision", "Basic Calculator II",
        "Next Greater Element I", "Next Greater Element II",
        "Remove K Digits", "Simplify Path"
    ],
    "Recursion_and_Backtracking": [
        "Subsets", "Subsets II", "Permutations", "Permutations II",
        "Combination Sum", "Combination Sum II", "Letter Combinations of Phone Number",
        "Palindrome Partitioning", "N-Queens", "Sudoku Solver",
        "Word Search II", "Generate Parentheses", "Beautiful Arrangement",
        "Restore IP Addresses", "Gray Code"
    ],
    "Sorting_and_Searching": [
        "Merge Sort Implementation", "Quick Sort Implementation",
        "Kth Largest Element in Array", "Find Peak Element",
        "Search a 2D Matrix", "Search a 2D Matrix II",
        "Find K Closest Elements", "Median of Two Sorted Arrays",
        "Count of Smaller Numbers After Self", "Wiggle Sort II",
        "Sort Colors (Dutch Flag)", "Largest Number", "Meeting Rooms II"
    ],
    "Heaps_and_Priority_Queues": [
        "Kth Largest Element in a Stream", "Top K Frequent Elements",
        "Find Median from Data Stream", "K Closest Points to Origin",
        "Task Scheduler", "Reorganize String", "Sliding Window Median",
        "Smallest Range Covering Elements from K Lists"
    ],
    "Tries": [
        "Implement Trie (Prefix Tree)", "Search Suggestions System",
        "Design Add and Search Words Data Structure", "Replace Words",
        "Longest Word in Dictionary"
    ],
    "Bit_Manipulation": [
        "Single Number", "Number of 1 Bits", "Counting Bits",
        "Reverse Bits", "Missing Number", "Sum of Two Integers",
        "Power of Two", "XOR of all Numbers in Range", "Bitwise AND of Numbers Range"
    ],
    "Math_and_Number_Theory": [
        "Palindrome Number", "Reverse Integer", "Pow(x,n)",
        "Sqrt(x)", "Roman to Integer", "Integer to Roman",
        "Count Primes (Sieve)", "Happy Number", "Excel Sheet Column Number",
        "Factorial Trailing Zeroes"
    ],
    "Greedy": [
        "Activity Selection", "Fractional Knapsack", "Huffman Coding",
        "Minimum Spanning Tree (Prim's)", "Dijkstra's Algorithm",
        "Assign Cookies", "Non-overlapping Intervals", "Boats to Save People",
        "Minimum Number of Arrows to Burst Balloons"
    ],
    "Advanced_Graphs": [
        "Bellman-Ford Algorithm", "Floyd-Warshall Algorithm",
        "Minimum Spanning Tree (Kruskal's)", "Tarjan's Algorithm (SCC)",
        "Bridges in Graph", "Articulation Points", "Euler Path",
        "Bipartite Graph Check", "Alien Dictionary"
    ]
}

ALL_QUESTIONS = []
for topic, questions in QUESTION_BANK.items():
    for q in questions:
        ALL_QUESTIONS.append({"topic": topic, "question": q})

DIFFICULTY_LEVELS = ["Easy", "Medium", "Hard"]
TRACKER_PATH = Path("scripts/.tracker.json")
QUEUE_PATH = Path("scripts/.daily_queue.json")


# ─────────────────────────────────────────────
#  GROQ API
# ─────────────────────────────────────────────
def generate_solution(client, topic: str, question: str, difficulty: str) -> str:
    prompt = f"""You are an expert competitive programmer. Generate a complete DSA solution.

Topic: {topic.replace('_', ' ')}
Question: {question}
Difficulty: {difficulty}
Language: C++

Respond ONLY with a markdown file in this EXACT format (no extra text):

# {question}

## Problem Statement
(Write a clear, complete problem statement with constraints and examples)

## Approach
(Explain the algorithm/intuition in 3-5 lines)

## Complexity
- Time: O(...)
- Space: O(...)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

// solution with comments
```

## Test Cases
```
Input: ...
Output: ...
```

## Key Takeaways
- point 1
- point 2
"""
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=2000,
        temperature=0.7,
    )
    return response.choices[0].message.content


def get_file_path(topic: str, question: str, day: str, index: int) -> Path:
    safe = question.replace(" ", "_").replace("/", "_").replace("(", "").replace(")", "").replace("'", "").replace(",", "")
    return Path(f"solutions/{topic}/Day_{day}/Q{index:02d}_{safe}.md")


def load_tracker() -> set:
    if TRACKER_PATH.exists():
        with open(TRACKER_PATH) as f:
            return set(json.load(f))
    return set()


def save_tracker(done: set):
    TRACKER_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(TRACKER_PATH, "w") as f:
        json.dump(list(done), f, indent=2)


def load_queue() -> list:
    if QUEUE_PATH.exists():
        with open(QUEUE_PATH) as f:
            return json.load(f)
    return []


def save_queue(queue: list):
    with open(QUEUE_PATH, "w") as f:
        json.dump(queue, f, indent=2)


# ─────────────────────────────────────────────
#  MAIN — generates ONE solution and commits it
# ─────────────────────────────────────────────
def main():
    api_key = os.environ.get("GROQ_API_KEY")
    if not api_key:
        raise ValueError("GROQ_API_KEY not set!")

    client = Groq(api_key=api_key)
    today = datetime.now().strftime("%Y_%m_%d")

    # Load or build today's queue of 20 questions
    queue = load_queue()

    # If queue is empty or stale (from a previous day), build a fresh one
    if not queue or queue[0].get("day") != today:
        done = load_tracker()
        remaining = [q for q in ALL_QUESTIONS if q["question"] not in done]

        if len(remaining) < 20:
            print("All questions done! Resetting tracker...")
            done = set()
            save_tracker(done)
            remaining = ALL_QUESTIONS.copy()

        selected = random.sample(remaining, 20)
        queue = [{"day": today, "index": i+1, "topic": item["topic"], "question": item["question"]} for i, item in enumerate(selected)]
        save_queue(queue)
        print(f"Built fresh queue of 20 questions for {today}")

    # Pop the first item from the queue
    item = queue.pop(0)
    save_queue(queue)  # save remaining queue

    topic = item["topic"]
    question = item["question"]
    index = item["index"]
    difficulty = random.choice(DIFFICULTY_LEVELS)

    print(f"Generating [{index:02d}/20]: {question} ({topic}) — {difficulty}")

    solution = generate_solution(client, topic, question, difficulty)

    file_path = get_file_path(topic, question, today, index)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(solution)

    # Mark as done in tracker
    done = load_tracker()
    done.add(question)
    save_tracker(done)

    # Git commit this single file
    safe_name = question.replace("(", "").replace(")", "").replace("'", "")
    commit_msg = f"solved {safe_name}"

    subprocess.run(["git", "add", str(file_path), str(TRACKER_PATH), str(QUEUE_PATH)], check=True)
    subprocess.run(["git", "commit", "-m", commit_msg], check=True)

    print(f"Committed: {commit_msg}")
    print(f"Questions remaining in today's queue: {len(queue)}")


if __name__ == "__main__":
    main()
