#!/usr/bin/python
# -*- coding: utf-8 -*-

from gmailapi import GmailApi
import json
import sys
if __name__ == "__main__":
    '''
        GmailApi�̃T���v���R�[�h�ł��B
        ���ۂ̏�����gmailapi.py�ōs���Ă��܂��B
        �ڂ���������gmailapi.py�̏��������Ă��������B
    '''
    
    argvs = sys.argv
    with open(argvs[1]) as f:
        auth_info = json.load(f)
        
        user = 'me'

        api = GmailApi(auth_info)#������s���͔F�؂����߂��܂��B
        query =  "is:unread"#���ǃ��b�Z�[�W�Ńt�B���^�����O����N�G��
        
        #���ǃ��[���̃��X�g��\��
        maillist = api.getMailList(user, query ) 
        print( json.dumps(maillist, indent=4))

        #Id���烁�[���̓��e��\��
        content = api.getMailContent(user, maillist["messages"][0]['id'])

        print()
        print( json.dumps(content, indent=4))




