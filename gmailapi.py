#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
memo:

setup

インストール　（Linux）

easy installを使う場合
	sudo easy_install --upgrade google-api-python-client

pipを使う場合
	sudo pip install --upgrade google-api-python-client


GAEを使う場合もあるが今回は使わないので割愛

具体的な使い方はここが分かりやすそう。
https://developers.google.com/api-client-library/python/guide/aaa_oauth?hl=ja#oauth

http://everyday-01.blogspot.jp/2013/01/google-drive-sdkpython.html
gmail scope
https://developers.google.com/gmail/api/auth/scopes?hl=ja


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

auth_info = {
	"client_id"  :"",
	"client_secret" : "",
	"redirect_uri" : "urn:ietf:wg:oauth:2.0:oob",
	"scope" : "https://mail.google.com/",
	"response_type":u"code",
}
class GmailApi():
        def reconnect(self):
            try:
                self.service = GmailServiceFactory().createService()
            except errors.HttpError, error:
                 pass

	def sendMessage(self, user, message):
		"""Send an email message.
		"""
		try:
			message = (self.service.users().messages().send(userId=user, body=message).execute())
			return message
  		except errors.HttpError, error:
			print 'An error occurred: %s' % error

	def getMailList(self,user,qu):
            try:
		return self.service.users().messages().list(userId=user,q=qu).execute() 
            except errors.HttpError, error:
                reconnect()
	def getMailContent(self, user, i):
            try:
		return  self.service.users().messages().get(userId=user,id=i).execute() 
            except errors.HttpError, error:
                    reconnect()
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
	def doMailAsRead(self,user,messageId):
            """ Making mail as read

            """
            try:
                query ={"removeLabelIds":
                                ["UNREAD"]
                                }
                self.service.users().messages().modify(userId=user,id=messageId,body=query).execute()
            except errors.HttpError, error:
                reconnect()
	
	def createMessage(self, sender, to, subject, message_text):
		"""Create a message for an email.
		"""
		message = MIMEText(message_text)
		message['to'] = to
		message['from'] = sender
		message['subject'] = subject
		return {'raw': base64.urlsafe_b64encode(message.as_string())}
	 
	def __init__(self):
            try:
		self.service = GmailServiceFactory().createService()
            except errors.HttpError, error:
                 pass

class GmailServiceFactory():

    def createService(self):
		STORAGE = Storage('gmail.auth.storage')
		credent = STORAGE.get()
        
		if credent is None or credent.invalid:
			flow = OAuth2WebServerFlow(auth_info["client_id"], auth_info["client_secret"], auth_info["scope"],auth_info["redirect_uri"])
			auth_url = flow.step1_get_authorize_url()
			webbrowser.open(auth_url)
			code = raw_input("input code : ")
			credent = flow.step2_exchange(code)
			STORAGE.put(credent)
		http = httplib2.Http()
		http = credent.authorize(http)
	 
		gmail_service = build("gmail", "v1", http = http)
		return gmail_service


