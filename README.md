# FC message remover
This repo is for a small tool developed in Python and using Selenium for the automatisation of the deletion of your messages in the infamous spanish forum www.forocoches.com
## Usage
```
$ python3 delete.py
```

## Dependencies

### Selenium
 ```sh
$ sudo pip3 install selenium
```
### Numpy
 ```sh
$ sudo pip3 install numpy
```

## Troubleshooting
### Selenium gecko driver
Selenium for Python is cool and sexy, but nothing comes for free: if this is the first time you use Selenium API for Python, you may have problems with something called "gecko driver" and it is browser dependent. For example, if you are going to use the Firefox browser with Selenium, you will need the Selenium gecko driver for Firefox, which is different from the Chrome one, etc. Don't panic, this is not a big deal. All you have to do to use the Firefox browser with Selenium, if this is your first time and you have problems with the gecko driver, is download it (the gecko driver for Firefox) and put it in your `PATH`, e. g., place it in `/usr/bin` or `/usr/local/bin`.


Other supported browsers will have their own drivers available. Links to some of the more popular browser drivers follow.

**Chrome**: https://sites.google.com/a/chromium.org/chromedriver/downloads

**Edge**: https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/

**Firefox**: https://github.com/mozilla/geckodriver/releases

**Safari**: https://webkit.org/blog/6900/webdriver-support-in-safari-10/


