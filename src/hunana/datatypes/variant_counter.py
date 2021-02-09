class VariantCounter(object):
    def __init__(self):
        self.counters = {}

    def observe(self, s):
        try:
            self.counters[s] += 1
        except KeyError:
            self.counters[s] = 1

    def results(self, matric):
        if matric == 'values':
            return self.counters.values()
        elif matric == 'keys':
            return self.counters.keys()
        else:
            return self.counters
