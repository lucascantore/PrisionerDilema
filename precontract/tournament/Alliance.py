
# We assume that no one is going to modify the alliance internal attributes.

class Alliance:
    def __init__(self, leader):
        # leader of the alliance
        self.leader = leader
        # members of the alliance
        self.members = [leader]
        # map that, given the alliance player number, returns the percentage that they give to the alliance
        self.members_give = {leader.number: 1}
        # map that, given the alliance player number, return the percentage that they receive from the alliance
        # leader starts with 1, because they are the only member of the alliance
        # we also use the leader receive to measure how much percentage of the alliance total
        # can still be offered to other players
        self.members_receive = {leader.number: 1}

        # when alliance is no longer valid, turns to false
        # (Example: when the leader accepts another offer and no other players were in the alliance)
        self.is_valid = True

    # adds member to alliance, and returns whether it was successful or not.
    def add_member(self, member, offer):
        if not self.can_add_new_member_for(member, offer):
            # should be verified before calling add_member
            raise ValueError("Tried to add a member to an alliance, with an invalid combination")

        self.members_give[member.number] = offer.give
        self.members_receive[member.number] = offer.receive
        self.members_receive[self.leader.number] -= offer.receive
        self.members.append(member.number)

    def can_add_new_member_for(self, member ,offer):
        if member in self.members:
            print("could not add member: member already in alliance")
            return False
        if self.remaining_receive_percentage() - offer.receive < 0:
            print("could not add member: total offered sum should not be greater than 1")
            return False
        if not self.is_valid:
            print("could not add member: alliance is not longer valid")
            return False

        return True

    def invalidate_alliance(self):
        self.is_valid = False

    def remaining_receive_percentage(self):
        return self.members_receive[self.leader.number]

    def alliance_index(self):
        return self.leader.number

    def get_received_percentage_for(self, player_number):
        return self.members_receive[player_number]

    def __str__(self):
        return f"{{Leader: {self.leader},\n members: {self.members}, \n members_give: {self.members_give}, \n members_receive: {self.members_receive}"
