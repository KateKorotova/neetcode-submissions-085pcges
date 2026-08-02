class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sort_pos = sorted(zip(position, speed), key=lambda x: -x[0])
        # if not position:
        #     return 0
        curr_time = (target - sort_pos[0][0])/sort_pos[0][1]
        fleets = 1
        for pos, speed in sort_pos[1:]:
            time = (target - pos) / speed
            if time > curr_time:
                curr_time = time
                fleets += 1
        return fleets
        