import random


class Agent:
    def __init__(self,agent_id,position):
        self.agent_id = agent_id
        self.position = position
    def move(self):
        dx= random.choice([-1,0,1])
        dy= random.choice([-1,0,1])
        self.position[0] += dx
        self.position[1] += dy

agent1=Agent(1,[0,0])

print(agent1.agent_id)
print(agent1.position)

print("Before move:",agent1.position)
agent1.move()
agent1.move()
print("After move:",agent1.position)
