import sys
sys.path.insert(0, '/home/seal12/Downloads/Chatgpt/code-imitator-master/src/PyProject')



import typing
import evasion.BlackBox.AMCTS.State
from evasion.Transformers.TransformerBase import TransformerBase
from evasion.BBAttackInstance import BBAttackInstance


class StateWithAttackInstance(evasion.BlackBox.AMCTS.State.State):

    def __init__(self,
                 attackinstance: typing.Optional[BBAttackInstance] = None,
                 transformer: typing.Optional[TransformerBase] = None):


        super(StateWithAttackInstance, self).__init__(transformer)
        self.attackinstance = attackinstance
