import datetime

now = datetime.datetime.now
class Base:
    def __init__(self, event, **kwargs):
        self._event = event
        self.kwargs = kwargs

    def __str__(self):
        return str(bool(self))

    def __repr__(self):
        return bool(self)

    def __bool__(self):
        pass

class Present(Base):
    def __bool__(self):
        return self._event == now()

class Past(Base):
    def __bool__(self):
        return self._event < now()

class Future(Base):
    def __bool__(self):
        return self._event > now()

    
