from discord_webhook import DiscordWebhook, DiscordEmbed
webhookurl = "https://discord.com/api/webhooks/1019113357653065788/MUebVsWHRRfq-XYS2pDDAVyir5FuahBcMxGxS0ArNUsgj40UMcdS_1NWc2Cw9oCwF_gh"
embed = DiscordEmbed(title="BOT RUNNING", description="NULL", color="ED4245")
c = 0
while True:
    for i in range(0, 30000):
        if i == 500:
            webhook = DiscordWebhook(url=webhookurl,
                                     content=str(c) + " " + "TIMES")
            webhook.add_embed(embed)
            webhook.execute()
            c = c + 1
