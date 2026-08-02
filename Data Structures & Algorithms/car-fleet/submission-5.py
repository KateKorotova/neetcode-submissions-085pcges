class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sort_pos = sorted(zip(position, speed), key=lambda x: -x[0])
        stack = []
        if not position:
            return 0
        stack.append((target - sort_pos[0][0])/sort_pos[0][1])
        for pos, speed in sort_pos[1:]:
            time = (target - pos) / speed
            if time > stack[-1]:
                stack.append(time)

        return len(stack)
        