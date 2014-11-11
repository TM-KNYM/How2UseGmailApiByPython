#!/usr/bin/python
# -*- coding: utf-8 -*-

from gmailapi import GmailApi
import json
import sys
if __name__ == "__main__":
    '''
        GmailApiのサンプルコードです。
        実際の処理はgmailapi.pyで行っています。
        詳しい処理はgmailapi.pyの処理を見てください。
    '''
    
    argvs = sys.argv
    with open(argvs[1]) as f:
        auth_info = json.load(f)
        
        user = 'me'

        api = GmailApi(auth_info)#初回実行時は認証が求められます。
        query =  "is:unread"#未読メッセージでフィルタリングするクエリ
        
        #未読メールのリストを表示
        maillist = api.getMailList(user, query ) 
        print( json.dumps(maillist, indent=4))

        #Idからメールの内容を表示
        content = api.getMailContent(user, maillist["messages"][0]['id'])

        print()
        print( json.dumps(content, indent=4))




