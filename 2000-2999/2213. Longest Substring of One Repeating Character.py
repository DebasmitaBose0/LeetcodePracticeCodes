from ast import List
class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        n = len(s)
        s_list = list(s)

        # Segment Tree Arrays
        tree_max = [0] * (4 * n)
        tree_pref = [0] * (4 * n)
        tree_suff = [0] * (4 * n)
        tree_left_char = [''] * (4 * n)
        tree_right_char = [''] * (4 * n)

        def merge(node: int, l: int, r: int, mid: int):
            left_node = 2 * node
            right_node = 2 * node + 1

            # Inherit basic attributes
            tree_left_char[node] = tree_left_char[left_node]
            tree_right_char[node] = tree_right_char[right_node]

            tree_pref[node] = tree_pref[left_node]
            tree_suff[node] = tree_suff[right_node]

            max_len = max(tree_max[left_node], tree_max[right_node])

            # Check if boundary characters match
            if tree_right_char[left_node] == tree_left_char[right_node]:
                combined = tree_suff[left_node] + tree_pref[right_node]
                max_len = max(max_len, combined)

                # Extend prefix if left child is completely uniform
                left_len = mid - l + 1
                if tree_pref[left_node] == left_len:
                    tree_pref[node] = left_len + tree_pref[right_node]

                # Extend suffix if right child is completely uniform
                right_len = r - mid
                if tree_suff[right_node] == right_len:
                    tree_suff[node] = right_len + tree_suff[left_node]

            tree_max[node] = max_len

        def build(node: int, l: int, r: int):
            if l == r:
                tree_max[node] = 1
                tree_pref[node] = 1
                tree_suff[node] = 1
                tree_left_char[node] = s_list[l]
                tree_right_char[node] = s_list[l]
                return

            mid = (l + r) // 2
            build(2 * node, l, mid)
            build(2 * node + 1, mid + 1, r)
            merge(node, l, r, mid)

        def update(node: int, l: int, r: int, idx: int, ch: str):
            if l == r:
                s_list[idx] = ch
                tree_left_char[node] = ch
                tree_right_char[node] = ch
                return

            mid = (l + r) // 2
            if idx <= mid:
                update(2 * node, l, mid, idx, ch)
            else:
                update(2 * node + 1, mid + 1, r, idx, ch)

            merge(node, l, r, mid)

        # Build initial Segment Tree
        build(1, 0, n - 1)

        res = []
        for ch, idx in zip(queryCharacters, queryIndices):
            if s_list[idx] != ch:
                update(1, 0, n - 1, idx, ch)
            res.append(tree_max[1])

        return res