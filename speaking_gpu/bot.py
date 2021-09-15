from os import path
import typing

import discord


class SpeakingGPU(object):

    def __init__(self, url: typing.Optional[str]=None) -> None:
        super().__init__()
        if url is None:
            url = path.join('~', 'auth', 'url.txt')

        if url.startswith('~'):
            url = path.expanduser(url)

        try:
            with open(url, 'r') as f:
                url = f.read().splitlines()[0]
        except FileNotFoundError:
            print(f'{url} is not found!')
            exit()

        self.webhook = discord.Webhook.from_url(
            url,
            adapter=discord.RequestsWebhookAdapter(),
        )
        return

    def send(self, msg: str, force_notification: bool=False) -> None:
        if force_notification:
            msg = '@everyone ' + msg

        self.webhook.send(msg)
        return