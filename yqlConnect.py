#!/usr/bin/python3

import urllib.parse
import requests
import re
import json
from pprint import pprint

class yqlConnect:
  def __init__(self):
    self.base_url = 'https://query.yahooapis.com/v1/public/yql?';
    self.output_fmt = 'json'

  def urlBuilder(self, qry):
    base_url = self.base_url;
    formatedQry = {
        'q': qry,
        'format': self.output_fmt
        }
    url = base_url + urllib.parse.urlencode(formatedQry)
    return url;
    
  def grabWebContent(self,uri=''):
    src =''
    r = requests.get(uri)
    if r.status_code == 200:
      src = r.text;
    else:
      src = '{}';
      print ('Request Error ' + str(r.status_code) + ' < '+uri)
    return src;

  def request(self, yql=''):
    req_url = self.urlBuilder(qry=yql);
    response = self.grabWebContent(uri=req_url);

    if self.output_fmt == 'json':
      data = json.loads(response);
    else:
      data = response;
    return data;