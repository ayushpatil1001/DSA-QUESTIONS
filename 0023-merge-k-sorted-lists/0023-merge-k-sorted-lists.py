
import heapq

class Solution:
    def mergeKLists(self, lists):
        heap = []
        counter = 0

        # Add the first node of every non-empty list
        for node in lists:
            if node:
                heapq.heappush(heap, (node.val, counter, node))
                counter += 1

        dummy = ListNode(0)
        current = dummy

        while heap:
            value, _, node = heapq.heappop(heap)

            # Attach the smallest node to the result
            current.next = node
            current = current.next

            # Add the next node from the same list
            if node.next:
                heapq.heappush(
                    heap, (node.next.val, counter, node.next)
                )
                counter += 1

        current.next = None
        return dummy.next
