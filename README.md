# html_downloader

This is to download html files from a url and perform same for newly found valid urls.

## Setup-
1. Clone the repo
2. Setup virtualenv, if you want 
3. Install dependencies- pip install requirements.txt
4. Modify settings i.e.- HTML_FILES_ROOT (dir to store downloaded files)

## Run-
1. To run:
```{r, engine='bash', Run downloader}
python main.py http://www.facebook.com/
```

2. For help:
```{r, engine='bash', Run downloader}
python main.py -h
```
## Test and debug-
1. Enable logging using settings.DEBUG variable
2.Play around with complex urls with a lot of query parameters i.e.- 
http://www.google.ps/search?hl=en&client=firefox-a&hs=42F&rls=org.mozilla%3Aen-US%3Aofficial&q=The+type+%27Microsoft.Practices.ObjectBuilder.Locator%27+is+defined+in+an+assembly+that+is+not+referenced.+You+must+add+a+reference+to+assembly+&aq=f&aqi=&aql=&oq=

## Result-
It will create a directory structure and leaf will be a html file.
For example: for url 'http://example.com/a/b/c'

Directory structure will be inside $HTML_FILES_ROOT -

```{r, engine='bash', Run dir_structure}
.
├── files
│   └── www.example.com
│       └── a
│           └── b
│               └── c.html
```
## Example- 
On run-
```{r, engine='bash', Run downloader}
python main.py http://www.facebook.com/
```

Resulted directory structure- 
```{r, engine='bash', Run downloader}
.
├── bn-in.facebook.com
│   └── root.html
├── developers.facebook.com
│   └── root.html
├── facebook.com
│   └── root.html
├── gu-in.facebook.com
│   └── root.html
├── hi-in.facebook.com
│   └── root.html
├── kn-in.facebook.com
│   └── root.html
├── messenger.com
│   └── root.html
├── ml-in.facebook.com
│   └── root.html
├── mr-in.facebook.com
│   └── root.html
├── pa-in.facebook.com
│   └── root.html
├── ta-in.facebook.com
│   └── root.html
├── te-in.facebook.com
│   └── root.html
├── ur-pk.facebook.com
│   └── root.html
└── www.facebook.com
    ├── help
    │   └── 568137493302217.html
    └── root.html

```


## Tools used (env)-
1. Pychram as IDE
2. Python shell to test run
3. Bash for execution 

## To Do-
1. Enhance dir structure
2. Suggetions??

## Problem- 
Write a program that takes a URL as an input, and saves the response of that URL in a file, and then does the same for all the pages linked inside that HTML page. 

You need to devise a method for generating unique filenames for each URL. 
It would be best if the downloaded files are organized in a way that mimics the URL structure of the site.

Make sure that all your code is commented and easy to read by someone else.

Hint: We are looking at similar output as GNU wget command of linux
