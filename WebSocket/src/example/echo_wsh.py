# Copyright 2011, Google Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
#
#     * Redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above
# copyright notice, this list of conditions and the following disclaimer
# in the documentation and/or other materials provided with the
# distribution.
#     * Neither the name of Google Inc. nor the names of its
# contributors may be used to endorse or promote products derived from
# this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import pika
import subprocess
import json
import uuid

class Message(object):
    request = None

_crawler_path = "~/Desktop/WebOfWeb/MyCrawler/MyCrawler"
_spider_name = "single_url_spider"
_uuid = uuid.uuid4()
_p = None

def revive_spider(url):
    command = "cd %s;scrapy crawl %s -a s_url=%s -a uuid=%s" % (_crawler_path, _spider_name, url, _uuid)
    _p = subprocess.Popen(command, shell=True)
    return command


def web_socket_do_extra_handshake(request):
    # This example handler accepts any request. See origin_check_wsh.py for how
    # to reject access from untrusted scripts based on origin value.

    pass  # Always accept.


def web_socket_transfer_data(request):
    s_url = ""
    print "Websocket: client connected"
    while True:
        print "Websocket: wating for start command"
        line = request.ws_stream.receive_message()
        print "Websocket: message received %s" % line
        if line is not None:
            dic = json.loads(line)
            print "Websocket: ", dic, dic["command"]
            if dic["url"] is not None and dic["command"] == "start":
                print "Websocket: receive requested command: %s url: %s" % (dic["command"], dic["url"],)
                s_url = dic["url"]                
                break;
    print "Websocket: Should start transfer data!"
    print "Websocket: uuid is : %s" % _uuid
    revive_spider(s_url)
    _connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    _channel = _connection.channel()
    queue_name = "%s" % _uuid
    _channel.queue_declare(queue_name)
    print "Websocket: here!!!!!!!!!"
    while True:
        '''line = request.ws_stream.receive_message()
        print "Websocket: message received %s" % line
        if line is not None:
            dic = json.loads(line)
            if dic["command"] == "stop":
                print "Websocket: receive requested command: %s url: %s" % (dic["command"], dic["url"],)
                return    '''
        method_frame, header_frame, body = _channel.basic_get(queue_name)
        if method_frame:
            print "Websocket: %s" % body
            request.ws_stream.send_message(body, binary=False)


        

    

# vi:sts=4 sw=4 et
