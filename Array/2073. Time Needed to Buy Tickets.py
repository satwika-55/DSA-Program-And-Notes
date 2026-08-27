# Logic; On left of 'k' , maximum we can add time = tickets[k] for each ticket.
# On left,maximum we can add time = tickets[k] - 1 for each ticket. 
# Time : O(N) 

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        total_time = 0
        target_tickets = tickets[k]
        
        for i, ticket_count in enumerate(tickets):
            if i <= k:
                # People before or at index k buy up to target_tickets
                total_time += min(ticket_count, target_tickets)
            else:
                # People after index k buy up to target_tickets - 1
                total_time += min(ticket_count, target_tickets - 1)
                
        return total_time
