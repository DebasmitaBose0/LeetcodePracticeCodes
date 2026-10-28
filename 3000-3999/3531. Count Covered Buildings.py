class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        # 1. Sort events: Primary sort by timestamp (int), 
        # Secondary sort to ensure OFFLINE (0) comes before MESSAGE (1)
        events.sort(key=lambda x: (int(x[1]), 0 if x[0] == "OFFLINE" else 1))
        
        mentions = [0] * numberOfUsers
        online_at = [0] * numberOfUsers # Time when user becomes online
        
        for event_type, timestamp, data in events:
            t = int(timestamp)
            
            if event_type == "OFFLINE":
                user_id = int(data)
                online_at[user_id] = t + 60
                
            elif event_type == "MESSAGE":
                if data == "ALL":
                    for i in range(numberOfUsers):
                        mentions[i] += 1
                elif data == "HERE":
                    for i in range(numberOfUsers):
                        if online_at[i] <= t:
                            mentions[i] += 1
                else:
                    # Parse string like "id1 id0 id1"
                    parts = data.split()
                    for p in parts:
                        user_id = int(p[2:]) # Remove "id" prefix
                        mentions[user_id] += 1
                        
        return mentions