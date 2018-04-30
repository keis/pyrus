from structlog.processors import KeyValueRenderer
from colors import color


class PyrusRenderer(KeyValueRenderer):
    colors = {
        'debug': 'white',
        'warning': 'yellow',
        'error': 'red',
        'critical': 'magenta',
    }
    default_color = 'blue'

    def __init__(self, colored=True, **kwargs):
        self._enable_colors = colored
        super().__init__(**kwargs)

    def __call__(self, _, __, event_dict):
        level = event_dict.pop('level')
        ts = event_dict.pop('timestamp')
        event = event_dict.pop('event')
        return ' '.join(
            [
                '%s[%s]' % (self._colored(level[:4].upper(), level), ts),
                '%-44s' % (event,),
            ]
            + [self._colored(k, level) + '=' + repr(v)
               for k, v in self._ordered_items(event_dict)]
        )

    def _colored(self, text, level):
        if self._enable_colors:
            c = self.colors.get(level, self.default_color)
            return color(text, c)

        return text
