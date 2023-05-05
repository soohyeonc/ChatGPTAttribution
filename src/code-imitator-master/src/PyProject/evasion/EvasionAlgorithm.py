import sys
sys.path.insert(0, '/home/seal12/Downloads/Chatgpt/code-imitator-master/src/PyProject')


from enum import Enum

class EvasionAlgorithm(Enum):
    """
    Enum to represent the different evasion algorithms.
    """

    SimAnnealing = 0
    MCTS_Classic = 2
