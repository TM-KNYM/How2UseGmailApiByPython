#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
memo:


'''
import sys
from apiclient.discovery import build
import webbrowser
from apiclient.discovery import build
from oauth2client.client import OAuth2WebServerFlow
from oauth2client.file import Storage
from oauth2client.tools import run
import httplib2

from multiprocessing import Process, Value

import base64
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

auth_url = u"https://accounts.google.com/o/oauth2/auth?"

response_setting = {
    "scope" : "https://mail.google.com/",
    "response_type":u"code",
}
class GmailApi():
        def reconnect(self):
            '''サーバーにアクセスして認証をもう一度行う
            '''
            try:
                self.service = GmailServiceFactory().createService(self.auth_info)
            except errors.HttpError, error:
                 pass

	def sendMessage(self, user, message):
		"""メールを送信します。messageの作り方はcreateMesage関数を参照

                    Keyword arguments:
                    user -- meを指定する。
                    message -- createMessageで生成したオブジェクトを渡す必要があります

                    Returns: None
                """
		try:
			message = (self.service.users().messages().send(userId=user, body=message).execute())
			return message
  		except errors.HttpError, error:
			print 'An error occurred: %s' % error

	def getMailList(self,user,qu):
            ''' メールの情報をリストで取得します
              quの内容でフィルタリングする事が出来ます

               Keyword arguments:
               user -- me又はgoogleDevloperに登録されたアドレスを指定します。
               qu -- queryを設定します
                     例えばexample@gmail.comから送られてきた未読のメールの一覧を取得するには以下のように指定すればよい
                    "from: example@gmail.com is:unread"
               Returns: メール情報の一覧　idとThreadIdをKeyとした辞書型のリストになる
                 "messages": [
                      {
                       "id": "nnnnnnnnnnnn",
                       "threadId": "zzzzzzzzzzz"
                      },
                      {
                       "id": "aaaaaa",
                       "threadId": "bbbbbb"
                      },,,,
                  }
            '''
            try:
               return self.service.users().messages().list(userId=user,q=qu).execute() 
            except errors.HttpError, error:
               reconnect()

	def getMailContent(self, user, i):
            """指定したメールのIDからメールの内容を取得します。

                    Keyword arguments:
                    user -- meを指定する。
                    i -- メールのId getMailList()等を使用して取得したIdを使用する

                    Returns: メールの内容を辞書型で取得する
                    詳細は以下
                    http://developers.google.com/apis-explorer/#p/gmail/v1/gmail.users.messages.get
            """
            try:
		return  self.service.users().messages().get(userId=user,id=i).execute() 
            except errors.HttpError, error:
                    reconnect()

	def doMailAsRead(self,user,i):
            """指定したメールのIDを既読にします
                Keyword arguments:
                user -- meを指定する。
                i -- メールのId getMailList()等を使用して取得したIdを使用する

                Returns:　なし
            """
            query ={"removeLabelIds":
                            ["UNREAD"]
                            }
            self.service.users().messages().modify(userId=user,id=i,body=query).execute()
	
	def createMessage(self, sender, to, subject, message_text):
                """sendMessageで送信するメールを生成します
                    Keyword arguments:
                    sender -- meを指定する。
                    to -- メールのId getMailList()等を使用して取得したIdを使用する
                    subject -- 件名
                    message_text --　メールの内容
                    
                    Returns:　なし  
                """
		message = MIMEText(message_text)
		message['to'] = to
		message['from'] = sender
		message['subject'] = subject
		return {'raw': base64.urlsafe_b64encode(message.as_string())}

	#以下は必要に迫られて作った関数	
        def expMailContents(self, user, i, key):
            try:
		content =  self.getMailContent(user,i)
		return (filter(lambda header:header["name"] == key, content["payload"]["headers"] ))[0]["value"]
            except errors.HttpError, error:
                    reconnect()
	def getMailFrom(self, user, i):
            try:
		return self.expMailContents(user, i, "From") 
            except errors.HttpError, error:
                    reconnect()
	def getMailSubject(self, user, i):
            try:
		return self.expMailContents(user, i, "Subject") 
            except errors.HttpError, error:
                    reconnect()    
	
        
        def __init__(self, auth_info):
            self.auth_info = auth_info
            self.service = GmailServiceFactory().createService(self.auth_info)

class GmailServiceFactory():

    def createService(self, auth_info):
		STORAGE = Storage('gmail.auth.storage')
		credent = STORAGE.get()
        
		if credent is None or credent.invalid:
                        info = auth_info['installed']
                        flow = OAuth2WebServerFlow(info["client_id"], info["client_secret"], response_setting["scope"],info["redirect_uris"][0])
			auth_url = flow.step1_get_authorize_url()
			webbrowser.open(auth_url)#ブラウザを開いて認証する
			code = raw_input("input code : ")
			credent = flow.step2_exchange(code)
			STORAGE.put(credent)
		http = httplib2.Http()
		http = credent.authorize(http)
	 
		gmail_service = build("gmail", "v1", http = http)
		return gmail_service


