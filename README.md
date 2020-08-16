# Multi-armed bandit
The multi-armed bandit problem is one of the classical reinforcements learning problems that describe the friction between the agent's exploration and exploitation.

## Requirements
- [Python 3.6 or 3.7](https://www.python.org/downloads/release/python-360/)
- [Pipenv](https://pypi.org/project/pipenv/)

## How to install the packages
You can install the required Python packages using the following command:
- `pipenv sync`

## Thompson sampling
Thompson sampling is an algorithm for online decision problems where actions are taken sequentially in a manner that must balance between exploiting what is known to maximize immediate performance and investing to accumulate new information that may improve future performance.

More details can be found in [this](http://proceedings.mlr.press/v23/agrawal12/agrawal12.pdf) paper.

## How to train the agent
You can train the agent using the following command:
- `pipenv run python ts_bandits.py`

## Demo video
https://www.youtube.com/watch?v=I0XmHQJPaVM

## Improvement ideas
- create a new OpenAI Gym custom environment
- improve the code quality
- remove unnecessary comments
