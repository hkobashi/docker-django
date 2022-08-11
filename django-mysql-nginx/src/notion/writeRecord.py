import os
from pprint import pprint

from notion_client import Client

notion = Client(auth='secret_AvtxQ3suJMSXsbFhYRbT6xBdQz52B17EmJ9BLJUkAtE')
db = notion.databases.query(
    **{
        'database_id' : '8a576c66284645e5aa9bfd5a562fef3a'  # データベースID
      }
)

# 追加する野菜と個数の辞書を作成
append_dict = {'test1' : 'URL1', 'test2' : 'URL2'}

# １レコードずつデータベースにInsertする
for title,linkedUrl in append_dict.items():
    notion.pages.create(
        **{
            'parent': { 'database_id': '8a576c66284645e5aa9bfd5a562fef3a'},
            'properties': {
                'Overview': {
                    'title': [
                        {
                            'text': {
                                'content': title  # 野菜名を指定
                            }
                        }
                    ]
                },
                'URL': {
                    'url' : linkedUrl  # 個数を指定
                }
            }
        }
    )
# for idx in range(len(db['results'])):
#     title = db['results'][idx]['properties']['Overview']['title'][0]['text']['content']
#     url = db['results'][idx]['properties']['URL']['url']
#     print('{} : URL {}'.format(title, url))    