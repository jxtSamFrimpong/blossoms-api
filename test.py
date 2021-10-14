import requests

BASE = "http://127.0.0.1:5000/"

data = [
{
                             'name':'what happens under your pillow every night will shock you',
                          'channel_id': 44,
                             'channel_name':'Vsauce',
                             'views':1324235,
                             'likes':31244,
                             'date': 31534678968
                          },
{
                             'name':'climb up this cliff and risk your future',
                          'channel_id': 44,
                             'channel_name':'Vsauce',
                             'views':57846876,
                             'likes':4487656,
                             'date': 31534678968
                          },
{
                             'name':'youll never believe this was happening to you since you were born',
                          'channel_id': 44,
                             'channel_name':'Vsauce',
                             'views':8989756,
                             'likes':879770,
                             'date': 31534678968
                          }
]



if __name__ == "__main__":

    for i in range(len(data)):
        reaponse = requests.put(BASE + "watch/" + str(i),
                                data[i]
                                )
        print(reaponse.json())

reaponse = requests.patch(BASE + 'watch/2', {'date': 100000})
print(reaponse.json())

