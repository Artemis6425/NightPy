# A python wrapper for Nightbot API
### Forked by Artemis

API documentation : https://api-docs.nightbot.tv/


### Install 

First, clone the repository
```bash
git clone https://github.com/Artemis6425/NightPy.git
```
Then, navigate to that directory and run the `setup.py` file
```bash
python setup.py install
```
### Usage
```python
from NightPy.nightpy import NightPy


np = NightPy(api_token_here)

np.skip_current_queue_item()
```
