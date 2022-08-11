from pprint import pprint
from notion_client import Client # NotionAPI
import requests

notion = Client(auth='secret_AvtxQ3suJMSXsbFhYRbT6xBdQz52B17EmJ9BLJUkAtE')
db = notion.databases.query(
    **{
        'database_id' : '8a576c66284645e5aa9bfd5a562fef3a'  # NotionデータベースID
      }
)

page = notion.get_block("https://www.notion.so/3007ec07920a48e4b106e6b5538c5302")
print(page)

# for idx in range(len(db['results'])):
#     title = db['results'][idx]['properties']['Overview']['title'][0]['text']['content']
#     url = db['results'][idx]['properties']['URL']['url']
# #    print('{} : {}'.format(title, url))
# #    print(url)
#     r = requests.get(url, verify=True)
#     print(r)