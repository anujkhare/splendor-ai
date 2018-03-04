
class AI(object):

    def create_neural_net(self):
        raise NotImplementedError()

    def make_move(self, state):
        pass


    def choose_noble(self, nobles):
        raise NotImplementedError()
        return nobles[0]

class MoveInfo(object):
    def __init__(self,
                 move,
                 pre_move_values=None,
                 post_move_values=[None, None],
                 pre_move_vecs=None,
                 post_move_vecs=[],
                 pre_move_grads=None,
                 current_player_index=None):
        self.move = move

        self.pre_move_values = pre_move_values
        self.post_move_values = post_move_values

        self.pre_move_vecs = pre_move_vecs
        self.post_move_vecs = post_move_vecs

        self.pre_move_grads = pre_move_grads
