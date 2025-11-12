# Procrastibar

A fun progress bar library for Python that displays the progress as a sequence of emojis narrating a random famous story.

## Installation

```bash
pip install procrastibar
```

## Usage

```python
from procrastibar import StoryProgressBar
import time

with StoryProgressBar(total=100) as pbar:
    for i in range(100):
        time.sleep(0.1)
        pbar.update(1)
```

The progress bar will show a sequence of emojis that tell a story, advancing as the progress increases.

## Stories Included

The library randomly selects from emoji sequences representing famous stories such as:

- Little Red Riding Hood
- Snow White
- Cinderella
- Aladdin
- The Lion King
- Star Wars
- Harry Potter
- The Wizard of Oz
- Peter Pan
- Alice in Wonderland

Each story is told through a series of emojis that represent key events in the tale.