from knu_rl_env.road_hog import RoadHogAgent, make_road_hog, evaluate


'''
Implement your agent by overriding knu_rl_env.road_hog.RoadHogAgent
'''
class RoadHogRLAgent(RoadHogAgent):
    def act(self, state):
        '''
        Return value is one of actions following:
        - RoadHogAgent.FORWARD_ACCEL_RIGHT
        - RoadHogAgent.FORWARD_ACCEL_NEUTRAL
        - RoadHogAgent.FORWARD_ACCEL_LEFT
        - RoadHogAgent.NON_ACCEL_RIGHT
        - RoadHogAgent.NON_ACCEL_NEUTRAL
        - RoadHogAgent.NON_ACCEL_LEFT
        - RoadHogAgent.BACKWARD_ACCEL_RIGHT
        - RoadHogAgent.BACKWARD_ACCEL_NEUTRAL
        - RoadHogAgent.BACKWARD_ACCEL_LEFT
        '''
        pass

'''
Implement how to train your agent
'''
def train():
    '''
    Below is to create the grid adventure environment.
    '''
    env = make_road_hog(
        show_screen=True # or, False
    )
    '''
    And your training code might be followed.
    Don't forget to dump your trained agent into a file.
    '''



if __name__ == '__main__':
    agent = '''Load your trained agent from the file'''
    evaluate(agent)