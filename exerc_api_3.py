import os
from twilio.rest import Client

recovery_code = "KHEDR89ST9P98X2J6VQQYY53"

account_sid = 'AC9c159ab6c3de1b051fbdaba533e581ce'
auth_token = 'd4f0d16e826b8a879e979cde287abf38'
client = Client(account_sid, auth_token)

remetente = '+12059526165'
destino = '+5562981895100'

message = client.messages \
                .create(
                     body="Testando API, de mensagens de celular. Favor não responder mensagem",
                     from_=remetente,
                     to=destino
                 )
print(message.sid)