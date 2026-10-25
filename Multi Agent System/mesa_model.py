import mesa


class MyAgent(mesa.Agent):
    def __init__(self, model):
        super().__init__(model)

    def step(self):
        possible_steps = self.model.grid.get_neighborhood(
            self.pos,
            moore=True,
            include_center=False
        )

        new_position = self.random.choice(possible_steps)
        self.model.grid.move_agent(self, new_position)


class MyModel(mesa.Model):
    def __init__(self, width, height, num_agents):
        super().__init__()

        self.grid = mesa.space.MultiGrid(width, height, torus=True)

        for i in range(num_agents):
            agent = MyAgent(self)

            x = self.random.randrange(width)
            y = self.random.randrange(height)

            self.grid.place_agent(agent, (x, y))

    def step(self):
        self.agents.shuffle_do("step")


model = MyModel(width=10, height=10, num_agents=20)

for i in range(3):
    model.step()

    print(f"\nStep {i + 1}")

    for agent in model.agents:
        print(f"Agent {agent.unique_id} is at position {agent.pos}")