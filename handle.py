# -*- coding: utf-8 -*-
# filename: handle.py

import web
import hashlib
import reply
import receive

class Handle(object):
	def POST(self):
		try:
		    webData = web.data()
		    print "Handle Post webdata is ", webData
		    recMsg = receive.parse_xml(webData)
		    if isinstance(recMsg, receive.Msg) and recMsg.MsgType == 'text':
			toUser = recMsg.FromUserName
			fromUser = recMsg.ToUserName
			content = "test"
			replyMsg = reply.TextMsg(toUser, fromUser, content)
			return replyMsg.send()
		    else:
			print "暂且不处理"
			return "success"
		except Exception, Argment:
		    return Argment
	def GET(self):
		try:
			data = web.input()
			if len(data) == 0:
				return "hello, this is handle view"
			signature = data.signature
			timestamp = data.timestamp
			nonce = data.nonce
			echostr = data.echostr
			token = "1234" 
			list = [token, timestamp, nonce]
			list.sort()
			sha1 = hashlib.sha1()
			map(sha1.update, list)
			hashcode = sha1.hexdigest()
		        print "handle/GET func: hashcode, signature: ", hashcode, signature
			if hashcode == signature:
				return echostr
			else:
				return ""
		except Exception, Argument:
			return Argument
