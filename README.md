# thumbor_rewrite_loader
An HTTP loader which rewrites matches from a list with a single canonical domain. Not production ready, not tested, so please wait for a stable 1.0.0 release.

##### Concept and Purpose
We wanted a way to load origin images via a local/private cache. We happen to be using Varnish to do that. Varnish has static backend definitions so we can't (and don't care to) cache images from third party origins.

This came about partially because during high traffic spikes right as some content was being published, our front end would generate a lot of differently sized images for the same original image. In addition to just having a lot of clients requesting uncached image variants. This thundering herd scenario would sometimes max out our request rate limit to S3. By using Varnish to proxy these origin image requests they are collapsed to a single request and cached locally. Solving the rate limit issues and keeping the origin image around for what is a high probability of further variant requests in the near term.


##### Install
`pip install git+git://github.com/voxmedia/thumbor_rewrite_loader.git@0.9.1`
Where `0.9.1` is the release/tag. See releases for the latest version or optionally drop the `@` param to install from HEAD. All options are at your own risk.

##### Develop / Install locally
`git clone git@github.com:voxmedia/thumbor_rewrite_loader.git`
`cd thumbor_rewrite_loader && pip install -e .`


##### You must define the following config variables in your thumbor.conf
`REWRITE_LOADER_HOST_PATTERNS`, A list of regexs
`REWRITE_LOADER_CANONICAL_HOST`, A string


##### You must also enable the loader in your thumbor.conf
`LOADER = 'thumbor.loaders.thumbor_rewrite_loader'`


##### Example
```
LOADER = 'thumbor.loaders.thumbor_rewrite_loader'
REWRITE_CANONICAL_HOST = 'avarnish.cache.com'
REWRITE_HOST_PATTERNS = ['cachedby.avarnishcache.com', 'cachedby.avarnishcache.com']
```

In the above example, if a request is made to thumbor for: `http://youthumbor.com/unsafe/100x100/http://cachedby.avarnishcache.com/dog.jpg`
Then the loader will rewrite the request to the original image `http://cachedby.avarnishcache.com/dog.jpg` to instead load from `http://avarnish.cache.com/dog.jpg`


###### Authors
Jason Ormand [@okor](https://github.com/okor)

###### Functionality ported from private plugin created by the following authors
- Carmen Sarlo [@csarlo](https://github.com/csarlo)
- Clif Reeder [@clifff](https://github.com/clifff)
- Adri [@amplifi](https://github.com/amplifi)
- Pablo Mercado [@odacrem](https://github.com/odacrem)
