import numpy as np


class STN():
    """Create a state-task network object.

    """

    def __init__(self, H=10):
        self.H = H
        self._states = set()
        self._tasks = set()
        self._units = set()

    def __setattr__(self, name, value):
        if type(value) == State:
            self._states.add(name)
        elif type(value) == Task:
            self._tasks.add(name)
        elif type(value) == Unit:
            self._units.add(name)
        self.__dict__[name] = value

    def __repr__(self):
        s = "States:\n"
        for name in sorted(self._states):
            state = getattr(self, name)
            s += "    {0:20s}".format(str(state))
            s += "    {0:6.1f}".format(state.price)
            s += "    {0:6.1f}".format(state.initialize)
            s += "    {0:6.1f}\n".format(state.capacity)

        s += "\nTasks:\n"
        for name in sorted(self._tasks):
            task = getattr(self, name)
            s += "    {0:12s}\n".format(str(task))
            print(task.feeds)
            for f in task.feeds:
                s += "           Feed: {0:12s}".format(str(f))
                print(s)
                print(getattr(f, 'name'))
                s += "  {0:4.2f}".format(getattr(self, f)['rho'])
                s += "\n"
            s += "\n"
            # for f in task.feeds:
            #    s += "\n           Feed: {0:12s}".format(str(f))
            #    s += "  {0:4.2f}".format(self.feeds[f]['rho'])
            #    s += "  {0:4.2f}".format(self.feeds[f]['dur'])

        s += "\nUnits:\n"
        for name in sorted(self._units):
            unit = getattr(self, name)
            s += "    {0:12s}\n".format(str(unit))
        return s


class State():
    def __init__(self, name, initialize=0, price=0, capacity=np.Inf):
        self.name = name
        self.initialize = initialize
        self.price = price
        self.capacity = capacity

    def __repr__(self):
        return "<State>" + self.name


class Task():
    def __init__(self, name):
        self.name = name
        self.feeds = dict()
        self.products = dict()
        self.units = dict()

    def __repr__(self):
        print(self.feeds)
        print(self.products)
        print(self.units)
        return "<Task>" + self.name

    # def __str__(self):
    # s = "    {0:12s}".format(self.name)
    # for f in self.feeds:
    #    s += "\n           Feed: {0:12s}".format(str(f))
    #    s += "  {0:4.2f}".format(self.feeds[f]['rho'])
    #    s += "  {0:4.2f}".format(self.feeds[f]['dur'])
    # for p in self.products:
    #    s += "\n        Product: {0:12s}".format(str(p))
    #    s += "  {0:4.2f}".format(self.products[p]['rho'])
    #    s += "  {0:4.2f}".format(self.products[p]['dur'])
    # for u in self.units:
    #    s += "\n           Unit: {0:12s}".format(str(u))
    #    s += "  {0:4.2f}".format(self.units[u]['Bmin'])
    #    s += "  {0:4.2f}".format(self.units[u]['Bmax'])
    #    s += "  {0:4.2f}".format(self.units[u]['tclean'])
    #    s += "  {0:4.2f}".format(self.units[u]['cost'])
    #    s += "  {0:4.2f}".format(self.units[u]['vcost'])
    # return s + "\n"

    def feed(self, name, rho=1, dur=0):
        self.feeds[name] = {'rho': rho, 'dur': dur}

    def product(self, name, rho=1, dur=0):
        self.products[name] = {'rho': rho, 'dur': dur}

    def unit(self, name, Bmin=0, Bmax=np.Inf, tclean=0, cost=0, vcost=0):
        self.units[name] = {
            'Bmin': Bmin,
            'Bmax': Bmax,
            'tclean': tclean,
            'cost': cost,
            'vcost': vcost}
        name.tasks[self] = {
            'Bmin': Bmin,
            'Bmax': Bmax,
            'tclean': tclean,
            'cost': cost,
            'vcost': vcost}


# class Feed():
#    def __init__(state, task, rho=1, dur=0):


class Unit():
    def __init__(self, name):
        self.name = name
        self.tasks = dict()

    def __repr__(self):
        return "<Unit>" + self.name

    def task(self, name, Bmin=0, Bmax=np.Inf, tclean=0, cost=0, vcost=0):
        self.tasks[name] = {
            'Bmin': Bmin,
            'Bmax': Bmax,
            'tclean': tclean,
            'cost': cost,
            'vcost': vcost}
        name.units[self] = {
            'Bmin': Bmin,
            'Bmax': Bmax,
            'tclean': tclean,
            'cost': cost,
            'vcost': vcost}
