import datetime


class Base:
    def __init__(self, event, *args):
        self._event = event
        # self.args = args

        # reference to datetime now
        self.now = datetime.datetime.now

        # allowance: less and add 100 microseconds
        self.within_second = datetime.timedelta(microseconds=100)

    def __str__(self):
        return str(bool(self))

    def __repr__(self):
        return str(bool(self))

    def __bool__(self):
        pass

class Present(Base):
    def __bool__(self):
        return ((self._event >= self.now() - self.within_second)) and \
                (self._event <= (self.now() + self.within_second))

class Past(Base):
    def __bool__(self):
        return self._event < (self.now() - self.within_second)

class Future(Base):
    def __bool__(self):
        return self._event > (self.now() + self.within_second)

    
