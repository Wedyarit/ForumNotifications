from discord_webhook import DiscordWebhook, DiscordEmbed

from utils import config_parser

class Topic(object):
    def __init__(self, author, title, date, date_last, url):
        self.author = author
        self.title = title
        self.date = date
        self.date_last = date_last
        self.url = url
        self.author_img = f'https://excalibur-craft.ru/engine/ajax/lk/skin3d.php?mode=head&login={self.author}'

    def question_to_webhook(self):
        webhook = DiscordWebhook(url=config_parser.get_section_params('webhooks')['questions'])
        embed = DiscordEmbed(title='**Задан новый вопрос**', color='FFD500')
        embed.add_embed_field(name='**Название:**', value=f'{self.title}', inline=False)
        embed.add_embed_field(name='**Время публикации:**', value=f'{self.date}', inline=False)
        embed.add_embed_field(name='**Ссылка:**', value=f'[Нажми на меня]({self.url})', inline=False)
        embed.set_thumbnail(url='https://i.imgur.com/v94XnPf.png')
        embed.set_author(name=f'{self.author}', icon_url=f'{self.author_img}')
        embed.set_timestamp()

        webhook.add_embed(embed)
        webhook.execute()

    def support_to_webhook(self):
        webhook = DiscordWebhook(url=config_parser.get_section_params('webhooks')['support'])
        embed = DiscordEmbed(title='**Подана новая заявка о проблеме с лаунчером и/или клиентом**', color='FFD500')
        embed.add_embed_field(name='**Название:**', value=f'{self.title}', inline=False)
        embed.add_embed_field(name='**Время публикации:**', value=f'{self.date}', inline=False)
        embed.add_embed_field(name='**Ссылка:**', value=f'[Нажми на меня]({self.url})', inline=False)
        embed.set_thumbnail(url='https://i.imgur.com/v94XnPf.png')
        embed.set_author(name=f'{self.author}', icon_url=f'{self.author_img}')
        embed.set_timestamp()

        webhook.add_embed(embed)
        webhook.execute()

def is_new(topic: Topic):
    return topic.date_last[-3:] == 'мин' and int(topic.date_last[:-3]) <= 5
