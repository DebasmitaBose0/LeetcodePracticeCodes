class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        res = []
        
        # Iterate through every possible hour (0-11)
        for h in range(12):
            # Iterate through every possible minute (0-59)
            for m in range(60):
                # Count the number of set bits (1s) in both h and m
                # bin(x).count('1') tells us how many LEDs are on for that number
                if (bin(h).count('1') + bin(m).count('1')) == turnedOn:
                    # Format the time: h:mm (minutes always two digits)
                    res.append(f"{h}:{m:02d}")
                    
        return res