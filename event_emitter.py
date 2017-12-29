class EventEmitter(object):
    _event_callbacks = None

    def __init__(self):
        self._event_callbacks = {}

    def on(self, event_name, callback):
        self._event_callbacks.setdefault(event_name, [])
        self._event_callbacks[event_name].append(callback)

    def dispatch(self, event_name):
        for callback in self._event_callbacks[event_name]:
            callback()
