from State import StateClass
stateMan = {}
stateNames = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six"
]

for n, stateName in enumerate(stateNames):
    _state = StateClass(stateName)
    _state.setLinks(stateNames[(n+1)%len(stateNames)])
    _state.setGlobStates(stateNames)
    stateMan[stateName] = _state

route = []
def getRotue(_stateName, _stateMan):
    statesToCheck = _stateMan
    for link in statesToCheck[stateName].links:
        route.append(link)
        if(link == stateName):
            statesToCheck.remove(stateName)
            stateMan[_stateName].addRoute(stateName, route)
            break
        

getRotue("one", stateMan)
stateMan["one"].addRoute("two", ["three", "three", "three","three"])
print(stateMan["one"].routes)  
