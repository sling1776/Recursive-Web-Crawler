
# 0.  From Problem Analysis to Data Definitions

make a program that will access every link on a website up to a max number. If a link has 
been repeated, it will not re-access that link. After it accesses the link, it will print
the url in a tiered view to help the user see how deep it goes.


# 1.  System Analysis

probably going to use recursion and call a crawl() method over and over again. 

# 2.  Functional Examples

check for valid url.
if none supplied:
    exit.
if not valid
    exit
check for valid maxDept number 
if not valid or not supplied:
    set a default value of 3.
call crawl() on the url and give it the max depth.

crawl(url, depth, maxDepth, visited)
    if depth > maxDepth
        return
    try:
        access url
        add to visited set
        if there was an error visiting the site 
            display error to the user and return.
        print the url to the screen
        get all the links from the HTML file.
        make sure the url is and absolute url.
        if not, then make it an absolute url.
        if the url starts with HTTP
            if the url not in visited
                call crawl on the url. 
    catch:
        exception if error in accessing the URL.


# 3.  Function Template


# 4.  Implementation
Done.

# 5.  Testing

Run the program like so:

`
$ python crawler.py URL [optional-maxDepth]
`

Fill in the URL with a url that has the scheme "HTTP" or "HTTPS". The maxDepth argument
is optional and will default to 3 if the user enters a bad input or neglects to enter it. 

To test: run:

`
$ python crawler.py http://unnovative.net/level0.html
`

This will take you through 3 levels of this particular website's links:

```
$ python crawler.py http://unnovative.net/level0.html 10
Crawling from http://unnovative.net/level0.html to a maximum depth of 10 links
http://unnovative.net/level0.html
    http://unnovative.net/level1.html
        http://unnovative.net/level2.html
            http://unnovative.net/level3.html
                http://unnovative.net/level4.html
                    http://unnovative.net/level5.html
                        http://unnovative.net/level6.html
                            http://unnovative.net/level7.html
                                http://unnovative.net/level8.html
                                    http://unnovative.net/level9.html
                                        http://unnovative.net/level10.html
```

If you go up to 30 it will wrap back to 0 at 15 and so will end the program after that.

```
$ python crawler.py http://unnovative.net/level0.html 30
Crawling from http://unnovative.net/level0.html to a maximum depth of 30 links
http://unnovative.net/level0.html
    http://unnovative.net/level1.html
        http://unnovative.net/level2.html
            http://unnovative.net/level3.html
                http://unnovative.net/level4.html
                    http://unnovative.net/level5.html
                        http://unnovative.net/level6.html
                            http://unnovative.net/level7.html
                                http://unnovative.net/level8.html
                                    http://unnovative.net/level9.html
                                        http://unnovative.net/level10.html
                                            http://unnovative.net/level11.html
                                                http://unnovative.net/level12.html
                                                    http://unnovative.net/level13.html
                                                        http://unnovative.net/level14.html
                                                            http://unnovative.net/level15.html
```

A bad url does not contain the scheme "http" and/or the location. 
This program assumes that a location must contain a "." it is not smart enough beyond 
that to tell if the url is valid. it will attempt to access the url and then will throw
an exception if it cannot reach it. 

```
$ python crawler.py http://unnovative
Error: Invalid URL supplied.
Please supply an absolute URL to this program
```
```
$ python crawler.py http://unnovative.
Crawling from http://unnovative. to a maximum depth of 3 linkscrawl(): HTTPConnectionPool(host='unnovative.', port=80): Max retries exceeded with url: / (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x03C48460>: Failed to establish a new connection: [Errno 11001] getaddrinfo failed'))
```


