class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        
        rads = []
        dires = []
        l = len(senate)
        
        for i in range(0, l, 1):
            if senate[i] == "R":
                rads.append(i)
            else:
                dires.append(i)
              
            
        while rads != [] and dires != []:
            if rads[0] < dires[0]:
                dires.pop(0) # Lost
                rads.append(rads.pop(0) + l) # Winner enter queue again
            else:
                rads.pop(0)
                dires.append(dires.pop(0) + l)
            
                
        if rads == []:
            return "Dire"
        
        return "Radiant"
            