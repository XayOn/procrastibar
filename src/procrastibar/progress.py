from tqdm import tqdm
from .stories import get_random_story

class StoryProgressBar(tqdm):
    def __init__(self, *args, **kwargs):
        self._story_name, self.story = get_random_story()
        # Set ncols to accommodate the story length, minimum 80
        kwargs.setdefault('ncols', max(80, len(self.story) * 2 + 20))
        super().__init__(*args, **kwargs)
        self.bar_format = '{bar}'

    @property
    def story_name(self):
        return self._story_name

    def format_meter(self, n, total, elapsed, ncols=None, prefix='', ascii=False, unit='it', unit_scale=False, rate=None, bar_format=None, postfix=None, unit_divisor=1000, initial=0, colour=None, ncols_override=None, nrows=None, **kwargs):
        if total == 0:
            return ''
        filled = int(n / total * len(self.story))
        bar = ''.join(self.story[:filled])
        return bar