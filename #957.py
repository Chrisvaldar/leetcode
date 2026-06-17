# 957. Prison Cells After N Days
class Solution(object):
    def prisonAfterNDays(self, cells, n):
        check = {}
        order = []
        cycle_length = 0

        while True:
            curr = cells[:]
            for i in range(1, len(cells) - 1):
                if cells[i - 1] == cells[i + 1]:
                    curr[i] = 1
                else:
                    curr[i] = 0
            cells = curr
            cells[0], cells[-1] = 0, 0

            if tuple(cells) not in check:
                check[tuple(cells)] = cycle_length
                order.append(cells)
                cycle_length += 1
            else:
                break

        return order[(n - 1) % cycle_length]


sol = Solution()
print(sol.prisonAfterNDays([0, 1, 0, 1, 1, 0, 0, 1], 7))
