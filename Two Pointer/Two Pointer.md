# Two-Pointer Technique (General Explanation)

## Idea
- Place one pointer at the **start** (`left`) and one at the **end** (`right`) of a **sorted array**.
- At each step, examine the pair `(nums[left], nums[right])`.
- Depending on the condition (e.g., their sum vs. target), move one pointer:
  - If the condition is **too small**, move `left` forward (to increase the sum).
  - If the condition is **too large**, move `right` backward (to decrease the sum).
  - If it matches, you’ve found the answer.

The **sorted order** guarantees that moving the pointers systematically eliminates impossible pairs.

---

## Why It Works
- A naive solution would check every pair `(i, j)` → **O(n²)** time.
- Two pointers skip large groups of pairs at once:
  - If `nums[left] + nums[right] > condition`, then all pairs with that `right` and larger `left` are **even bigger** → safely skipped.
  - If `nums[left] + nums[right] < condition`, then all pairs with that `left` and smaller `right` are **even smaller** → safely skipped.
- Each pointer only moves forward or backward, never revisiting the same element → linear scan.

---

## Runtime
- Each pointer moves at most `n` times.
- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(1)`

---

## General Pseudocode

```python
def two_pointer_template(nums, condition):
    # Step 1: sort if needed
    nums.sort()

    # Step 2: initialize pointers
    left = 0
    right = len(nums) - 1

    answer = []

    # Step 3: move pointers until they meet
    while left < right:
        # Compute some value with nums[left], nums[right]
        state = nums[left] + nums[right]   # example: sum

        if state == condition:
            # Handle case: store result / return / update
            answer.append([nums[left], nums[right]])

            # Move both pointers (and skip duplicates if needed)
            left += 1
            right -= 1

        elif state < condition:
            # Adjust left pointer to increase value
            left += 1
        else:
            # Adjust right pointer to decrease value
            right -= 1

    return answer
```

---

## When to Use Two Pointers
- Input is sorted (or can be sorted).
- You are checking pairwise relationships.

## Common problems:
- Two Sum in sorted arrays.
- 3Sum (fix one element, run two-pointer on the rest).
- Checking if a string is a palindrome.
- Container With Most Water.
- Trapping Rain Water.
- Merging sorted arrays.