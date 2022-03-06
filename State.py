from sre_parse import State
from termios import FIONREAD


class StateClass:
    def __init__(self, stateName):
        self.stateName = stateName

    def setLinks(self, _links):
        self.links = _links

    def setGlobStates(self, _states):
        self.states = _states
    
    routes = {}

    def addRoute(self, targetState, _route):
        self.routes[targetState] = _route