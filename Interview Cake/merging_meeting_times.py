class Solution():
    def merge_meetings(self, meetings):
        sorted_meetings = sorted(meetings)
        merged_meetings = [sorted_meetings[0]]

        for current_meeting in sorted_meetings[1:]:
            last_merged_meeting = merged_meetings[-1]
            if self.check_merge(last_merged_meeting, current_meeting):
                merged_list[-1] = self.merge_tuples(
                    last_merged_meeting, current_meeting)
            else:
                merged_meetings.append(current_meeting)

        return merged_meetings

    def check_merge(self, last_meeting, current_meeting):
        return current_meeting[0] <= last_meeting[1]

    def merge_tuples(self, tuple1, tuple2):
        return (tuple1[0], max(tuple1[1], tuple2[1]))


#test_meetings = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
#test_meetings = [(1, 2), (2, 3)]
#test_meetings = [(0, 3), (3, 6), (4, 5), (10, 12), (9, 10)]
test_meetings = [(1, 10), (2, 6), (3, 5), (11, 12)]

solution = Solution()
result = solution.merge_meetings(test_meetings)
print(result)
