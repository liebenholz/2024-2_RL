from knu_rl_env.grid_survivor import GridSurvivorAgent, make_grid_survivor, evaluate


'''
Implement your agent by overriding knu_rl_env.grid_survivor.GridSurvivorAgent
'''
class GridSurvivorRLAgent(GridSurvivorAgent):
    def act(self, state):
        '''
        Return value is one of actions following:
        - GridSurvivorAgent.ACTION_LEFT
        - GridSurvivorAgent.ACTION_RIGHT
        - GridSurvivorAgent.ACTION_FORWARD
        '''
        pass

'''
Implement how to train your agent
'''
def train():
    '''
    Below is to create the grid adventure environment.
    '''
    env = make_grid_survivor(
        show_screen=True # or, False
    )
    '''
    And your training code might be followed.
    Don't forget to dump your trained agent into a file.
    '''



if __name__ == '__main__':
    agent = '''Load your trained agent from the file'''
    evaluate(agent)