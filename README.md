# Speaking GPU for monitoring your experiments


## Quick start

Clone this repository and install it.
```bash
git clone []
cd sg_bot
python setup.py develop
```

Then, make a webhook in your discord server

**Step 1**

![](asset/step_1.png)

**Step 2**

![](asset/step_2.png)

**Step 3**

![](asset/step_3.png)

**Step 4**

![](asset/step_4.png)

You can set the bot name and image. Check `asset/rtx.png`. Copy the url from this step.


Place authentication file in the root directory
```bash
cd
# You are under /home/[username]/.
mkdir auth
cd auth

# You are under /home/[username]/auth
vi url.txt
[Paste your server url]
```

Call the bot inside your training script!
```python
from speaking_gpu import bot

sg_bot = bot.SpeakingGPU()
sg_bot.send('Hello, world!')
# You can force the notification
sg_bot.send('Hello, world!', force_notification=True)
```

![](asset/step_5.png)