
class Solution:
    def combinationSum(self, candidates, target):
        result = []
        candidates.sort()

        def backtrack(start, current, total):
            if total == target:
                result.append(current[:])
                return

            if total > target:
                return

            for i in range(start, len(candidates)):
                current.append(candidates[i])

                # Reuse the same number if needed
                backtrack(i, current, total + candidates[i])

                # Remove the number and try another choice
                current.pop()

        backtrack(0, [], 0)
        return result
