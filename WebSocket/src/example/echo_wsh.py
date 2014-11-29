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

class Message(object):
    request = None

_crawler_path = "~/Desktop/WebOfWeb/MyCrawler/MyCrawler"
_spider_name = "single_url_spider"
_p = None
def callback(ch, method, properties, body):
    #_message_queue.append(body)
    print "Message received!"
    print Message.request
    if Message.request is not None:
        print "_request is not none"
        message = "%r" % (body,)
        print body
        print message
        if isinstance(message, unicode):
            print "message is unicode"
            Message.request.ws_stream.send_message(message, binary=False)
        else:
            print "message is not unicode"
            Message.request.ws_stream.send_message(message, binary=False) 

def revive_spider(url):
    command = "cd %s;scrapy crawl %s -a s_url=%s" % (_crawler_path, _spider_name, url)
    _p = subprocess.Popen(command, shell=True)
    return command


def web_socket_do_extra_handshake(request):
    # This example handler accepts any request. See origin_check_wsh.py for how
    # to reject access from untrusted scripts based on origin value.

    pass  # Always accept.


def web_socket_transfer_data(request):
    while True:
        line = request.ws_stream.receive_message()
        if line is not None:
            dic = json.loads(line)
            if dic["url"] is not None:
                print dic["url"]
                revive_spider(dic["url"])
                break;

    print "Should start transfer data!"
    Message.request = request
    _connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    _channel = _connection.channel()
    _channel.queue_declare(queue='hello')
    _channel.basic_consume(callback, queue='hello', no_ack=True)
    _channel.start_consuming()

# vi:sts=4 sw=4 et
