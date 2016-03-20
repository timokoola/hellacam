#!/usr/bin/python
# coding=utf-8
from twython import TwythonStreamer
from twython import Twython


class TwythonHelper:

    def __init__(self, keyfile):
        f = open(keyfile)
        lines = f.readlines()
        f.close()
        self.consumerkey = lines[0].split("#")[0]
        self.consumersecret = lines[1].split("#")[0]
        self.accesstoken = lines[2].split("#")[0]
        self.accesssec = lines[3].split("#")[0]
        self.api = Twython(self.consumerkey, self.consumersecret, self.accesstoken, self.accesssec)


if __name__ == '__main__':
    helper = (TwythonHelper("hellacam.keys"))
    api = helper.api
    photo = open("../image.jpg", "rb")
    response = api.upload_media(media=photo)
    api.update_status(status='Hella näyttää tältä', media_ids=[response['media_id']])
    photo.close()

