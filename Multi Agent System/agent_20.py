
import random

import matplotlib.pyplot as plt


class Agent:
    def __init__(self,agent_id,position):
        self.agent_id = agent_id
        self.position = position
    def move(self):
        # -1 means move left/down, 0 means stay, and 1 means move right/up
        dx= random.choice([-1,0,1])
        dy= random.choice([-1,0,1])
        self.position[0] += dx
        self.position[1] += dy


agents = []
for i in range(20):
    x = random.randint(0, 10)
    y = random.randint(0, 10)
    agent = Agent(i, [x, y])
    agents.append(agent)

for step in range(100):
    for agent in agents:
        agent.move()


x_positions = []
y_positions = []

for agent in agents:
    x_positions.append(agent.position[0])
    y_positions.append(agent.position[1])

plt.scatter(x_positions, y_positions)
plt.title("Final Positions of Agents")
plt.xlabel("X Position")
plt.ylabel("Y Position")
plt.grid(True)
plt.show()