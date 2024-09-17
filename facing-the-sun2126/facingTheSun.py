class Solution:
    # Returns count buildings that can see sunlight
    def countBuildings(self, height):
        maximum = -1
        building = 0
        for i in height:
            if i> maximum:
                maximum = i
                building += 1
        return building