from os import path
import typing

import discord


class SpeakingGPU(object):

    def __init__(
            self,
            prefix: typing.Optional[str]=None,
            url: typing.Optional[str]=None) -> None:

        super().__init__()
        self.prefix = prefix
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
        self.buffer = []
        return

    def _preprocess(self, msg: str) -> str:
        if self.prefix is not None and self.prefix != '':
            msg = f'{self.prefix} {msg}'

        return msg

    def send(self, msg: str, force_notification: bool=False) -> None:
        if force_notification:
            msg = '@everyone ' + msg

        msg = self._preprocess(msg)
        try:
            self.webhook.send(msg)
        except Exception as e:
            print(f'Error: {e}')
        finally:
            pass

        return

    def accumulate(self, msg: str) -> None:
        self.buffer.append(msg)
        return
