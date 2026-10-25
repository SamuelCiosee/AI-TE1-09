import random

import matplotlib.pyplot as plt


def distance(pos1,pos2):
    dx=pos1[0]-pos2[0]
    dy=pos1[1]-pos2[1]
    return (dx**2+dy**2)**0.5

def detect_nearby_agents(current_agent,agents,detection_range):
    nearby_agents=[]
    for other_agent in agents:
        if other_agent.agent_id != current_agent.agent_id:
            d=distance(current_agent.position,other_agent.position)
            if d<=detection_range:
                nearby_agents.append(other_agent)
    return nearby_agents



class Agent:
    def __init__(self,agent_id,position):
        self.agent_id = agent_id
        self.position = position
    def move(self,agents,detection_range):

        nearby_agents=detect_nearby_agents(self,agents,detection_range)

        if nearby_agents:
            move_x = 0
            move_y = 0

            print("Agent", self.agent_id,"at", self.position, "detected", len(nearby_agents),"nearby agents","at",nearby_agents[0].position)
            for other in nearby_agents:
                if self.position[0] < other.position[0]: # If the current agent is to the left of the other agent
                    move_x -= 1 # Move left
                    print("Agent", self.agent_id,"moves left to", self.position)

                elif self.position[0] > other.position[0]: # If the current agent is to the right of the other agent
                    move_x += 1 # Move right
                    print("Agent", self.agent_id,"moves right to", self.position)

                if self.position[1] < other.position[1]: # If the current agent is below the other agent
                    move_y -= 1 # Move down
                    print("Agent", self.agent_id,"moves down to", self.position)    

                elif self.position[1] > other.position[1]: # If the current agent is above the other agent
                    move_y += 1 # Move up
                    print("Agent", self.agent_id,"moves up to", self.position)
            
            move_x = max(-1, min(1, move_x))
            move_y = max(-1, min(1, move_y))


            self.position[0] += move_x
            self.position[1] += move_y

        else:
            dx= random.choice([-1,0,1])
            dy= random.choice([-1,0,1])
            self.position[0] += dx
            self.position[1] += dy

            





        # -1 means move left/down, 0 means stay, and 1 means move right/up
        dx= random.choice([-1,0,1])
        dy= random.choice([-1,0,1])
        self.position[0] += dx
        self.position[1] += dy



agents=[]

for i in range(20):
    x = random.randint(0, 50)
    y = random.randint(0, 50)

    agent = Agent(i, [x, y])
    agents.append(agent)

for step in range(1):
    for agent in agents:
        agent.move(agents,5)




x_positions = []
y_positions = []
for agent in agents:
    x_positions.append(agent.position[0])
    y_positions.append(agent.position[1])

plt.scatter(x_positions, y_positions)
plt.title("Agent Positions")
plt.xlabel("X Position")
plt.ylabel("Y Position")
plt.show()