from discord_webhook import DiscordWebhook,DiscordEmbed
webhookurl="https://discord.com/api/webhooks/1019113357653065788/MUebVsWHRRfq-XYS2pDDAVyir5FuahBcMxGxS0ArNUsgj40UMcdS_1NWc2Cw9oCwF_gh"
c=1
webhook=DiscordWebhook(url=webhookurl,content=str(c)+" "+"TIMES")
embed=DiscordEmbed(title="BOT RUNNING",description="times",color="ED4245")
webhook.add_embed(embed)
while True:
 for i in range(0,3000):
  if i==500:
   webhook.execute()
   c=c+1
           
