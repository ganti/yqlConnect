#!/usr/bin/python3
from yqlConnect import yqlConnect
from pprint import pprint

conn = yqlConnect();
qry = 'select * from weather.forecast where woeid in (select woeid from geo.places(1) where text="Berne, Switzerland")';
res = conn.request(yql=qry);
pprint(res)