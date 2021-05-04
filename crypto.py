import cryptocompare
from twilio.rest import Client 
 
def getPrice():
    cryptocompare.cryptocompare._set_api_key_parameter('2677da6f009941e0d53e5d19c995da74ea35e2c2e9f11a68bee9cff48124e282')
    x = cryptocompare.get_price('DOGE', currency='INR', full=False)
    # y = cryptocompare.get_historical_price_hour('DOGE', currency='INR', limit=5)
    # z = cryptocompare.get_avg('DOGE', currency='INR')
    return(x['DOGE']['INR'])

account_sid = 'ACd90dd42a4b19c5f9366d48418b8ca81e' 
auth_token = 'PUT_YOUR_API_HERE' 
client = Client(account_sid, auth_token) 

while(True):
    x = getPrice()
    if x < 30:
        message = client.messages.create( 
                                    from_='whatsapp:+14155238886',  
                                    body='Doge Current Price is : Rs {}'.format(x),      
                                    to='whatsapp:+919778471728' 
                                ) 
        
        print(message.sid)
        break
    
