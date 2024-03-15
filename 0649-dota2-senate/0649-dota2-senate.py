class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        
        rads = []
        dires = []
        l = len(senate)
        
        for i in range(0, l, 1):
            # print("Radiants:{0}".format(rads))
            # print("Dires:{0}".format(dires))
            # print(i)
            if senate[i] == "R":
                # print("HERE")
                rads.append(i)
                # print(rads)
            else:
                # print("THERE")
                dires.append(i)
                # print(dires)
            # print(rads)
            # print(dires)
              
            
        while rads != [] and dires != []:
            # print("Radiants:{0}".format(rads))
            # print("Dires:{0}".format(dires))
            # print(i, j)
            if rads[0] < dires[0]:
                dires.pop(0) # Lost
                rads.append(rads.pop(0) + l) # Winner enter queue again
            else:
                rads.pop(0)
                dires.append(dires.pop(0) + l)
            
                
        if rads == []:
            return "Dire"
        
        return "Radiant"
            