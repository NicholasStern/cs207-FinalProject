'''
This class will serve as an abstract interface for the @Scalar and @Vector
classes.
'''


class Node():
    def __init__(self):
        pass

    def eval(self):
        '''
        When implemented by subclasses, this function will both
        update the self._val attribute of the Node type and will
        modify the derivative accordingly

        Returns (self._val, self._der)
        '''
        raise NotImplementedError

    def get_partial(self, var):
        '''
        When implemented by subclasses, this function returns the derivative
        of the node with respect to @var

        Returns (self._val, self._der)
        '''
        raise NotImplementedError

    def __add__(self, other):
        raise NotImplemented

    def __radd__(self, other):
        raise NotImplemented

    def __sub__(self, other):
        raise NotImplemented

    def __rsub__(self, other):
        raise NotImplemented

    def __mul__(self, other):
        raise NotImplemented

    def __rmul__(self, other):
        raise NotImplemented

    def __truediv__(self, other):
        raise NotImplemented

    def __rtruediv__(self, other):
        raise NotImplemented

    def __neg__(self):
        raise NotImplemented
