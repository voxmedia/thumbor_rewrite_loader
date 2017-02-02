# thumbor_rewrite_loader
An HTTP loader which rewrites matches from a list with a single canonical domain.


### You must define the following config variables in your thumbor.conf
`REWRITE_LOADER_HOST_PATTERNS`, A list of regexs
`REWRITE_LOADER_CANONICAL_HOST`, A string

### You must also enable the loader in your thumbor.conf
`LOADER = 'thumbor.loaders.thumbor_rewrite_loader'`

### Example
```
LOADER = 'thumbor.loaders.thumbor_rewrite_loader'
REWRITE_CANONICAL_HOST = 'avarnish.cache.com'
REWRITE_HOST_PATTERNS = ['cachedby.avarnishcache.com', 'cachedby.avarnishcache.com']
```

In the above example, if a request is made to thumbor for: `http://youthumbor.com/unsafe/100x100/http://cachedby.avarnishcache.com/dog.jpg`
Then the loader will rewrite the request to the original image `http://cachedby.avarnishcache.com/dog.jpg` to instead load from `http://avarnish.cache.com/dog.jpg`


###### Authors
Jason Ormand [@okor](https://twitter.com/okor)
