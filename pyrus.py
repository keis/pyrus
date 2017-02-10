from structlog.processors import KeyValueRenderer
from colors import color


class PyrusRenderer(KeyValueRenderer):
    colors = {
        'debug': 'white',
        'warning': 'yellow',
        'error': 'red',
    }
    default_color = 'blue'

    def __call__(self, _, __, event_dict):
        level = event_dict.pop('level')
        ts = event_dict.pop('timestamp')
        event = event_dict.pop('event')
        c = self.colors.get(level, self.default_color)
        return ' '.join(
            [
                '%s[%s]' % (color(level[:4].upper(), c), ts),
                '%-44s' % (event,),
            ]
            + [color(k, c) + '=' + repr(v)
               for k, v in self._ordered_items(event_dict)]
        )
