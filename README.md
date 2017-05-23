# yqlConnector v0.5

*  Make YQL Requests in Python 3. 
*  Errorhandling is currently missing

## Example: Weatherforcast for Location

```
#!/usr/bin/python3
from yqlConnect import yqlConnect
from pprint import pprint  # optional

conn = yqlConnect();
qry = 'select * from weather.forecast where woeid in (select woeid from geo.places(1) where text="Berne, Switzerland")';
res = conn.request(yql=qry);
pprint(res)
```

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* I’d like to thank the Academy first of all
* Stackoverflow Community
