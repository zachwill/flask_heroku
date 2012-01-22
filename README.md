Flask Heroku
============

<pre><code>


             ##
 #########  ###
  ##     #   ##                     :GG   DG
  ##         ##                     :EE   EE                        ;E
  ##         ##                     :EE  KK                         ;E
  ##         ##                     :EE                             ;E
  ##   #     ##     ####     ####   :EEEEEEG   KEEEE     WE  WEEE;  ;E   EE EE   EE  
  ######     ##    ##  #f   #   #   :EE   EE  GEf;tEK  EEKK EEfiEE, ;E  fE  EE   EE  
  ##   #     ##        #l   ##            EE  KE   tE  EK   E;   EE ;E  E,  EE   EE  
  ##         ##       ##a    ###          EK  EEEEEEE  EK   E    KE ;EEEE   EE   EE  
  ##         ##    ##  #s     ###         EK  EE       EK   E    KE ;E EE   EE   EE  
  ##         ##   ##   #k       ##   E    EE  EE       EK   E,   EK ;E  KE  EE   EE  
  ##         ##   ##   ##W  #   #:   E    EK  ;EK.,EK  EK   EE,:EE, ;E   ED KE.,EEE  
 #####      #####  ### W#   ####,         EK   ,KEEE   K#    DEEK.  iK   WK  KEEE.   


                    github.com/zachwill/flask_heroku

</code></pre>


What is this?
-------------

A template to get your [Flask](http://flask.pocoo.org/) app running on
[Heroku](https://www.heroku.com/) as fast as possible. For added
convenience, the templates use [Twitter's Bootstrap
project](http://twitter.github.com/bootstrap/) to help reduce the amount
of time it's takes you as a developer to go from an idea to a working
site.

All of the CSS stylesheets are written using the [Less
CSS](http://lesscss.org/) syntax (even Bootstrap's CSS). If you're using
Mac OS X for development, make sure to check out [incident57's
Less.app](http://incident57.com/less/).

Alternatively, there's a [Less binary
compiler](https://github.com/cloudhead/less.js/) that works similarly on
the commandline, or you can always use the [`less.js`
script](https://github.com/cloudhead/less.js/) in your website otherwise
-- it's incredibly fast. For instance, if you visit the [Less CSS
site](http://lesscss.org), notice that it doesn't link to any CSS files.

Lastly, in Heroku's production environment, your Flask application will
be served through [`gunicorn`](http://gunicorn.org/) and
[`gevent`](http://www.gevent.org/).


Why should I use this?
----------------------

Everything I've learned from writing and maintaining the [Flask
Engine](https://github.com/zachwill/flask-engine) template for Google
App Engine has made its way into this repo, too. The goal is to make a
simple repo that can be cloned and added to for the majority of projects
going forward, while also staying minimal in size and complexity.


Instructions
------------

First, you'll need to clone the repo.

    $ git clone git@github.com:zachwill/flask_heroku.git
    $ cd flask_heroku

Second, let's download `pip`, `virtualenv`, `foreman`, and the [`heroku`
Ruby gem](http://devcenter.heroku.com/articles/using-the-cli).

    $ sudo easy_install pip
    $ sudo pip install virtualenv
    $ sudo gem install foreman heroku

Now, you can setup an isolated environment with `virtualenv`.

    $ virtualenv --no-site-packages env
    $ source env/bin/activate


Installing Packages
--------------------

### Gevent

To use `gevent`, we'll need to install `libevent` for the
`gevent` production server. If you're operating on a Linux OS, you can
`apt-get install libevent-dev`. If you're using Mac OS X, consider
installing the [homebrew](http://mxcl.github.com/homebrew/) package
manager, and run the following command:

    $ brew install libevent

If you're using Mac OS X, you can also install `libevent` through [a DMG
available on Rudix](http://rudix.org/packages-jkl.html#libevent).


### Without Gevent

If you'd rather use `gunicorn` without `gevent`, you just need to edit
the `Procfile` and `requirements.txt`.

First, edit the `Procfile` to look the following:

    web: gunicorn -w 4 -b "0.0.0.0:$PORT" app:app

Second, remove `gevent` from the `requirements.txt` file.

### pip

Then, let's get the requirements installed in your isolated test
environment.

    $ pip install -r requirements.txt


Running Your Application
------------------------

Now, you can run the application locally.

    $ foreman start

You can also specify what port you'd prefer to use.

    $ foreman start -p 5555


Deploying
---------

If you haven't [signed up for Heroku](https://api.heroku.com/signup), go
ahead and do that. You should then be able to [add your SSH key to
Heroku](http://devcenter.heroku.com/articles/quickstart), and also
`heroku login` from the commandline.

Now, to upload your application, you'll first need to do the
following -- and obviously change `app_name` to the name of your
application:

    $ heroku create app_name -s cedar

And, then you can push your application up to Heroku.

    $ git push heroku master
    $ heroku scale web=1

Finally, we can make sure the application is up and running.

    $ heroku ps

Now, we can view the application in our web browser.

    $ heroku open

And, to deactivate `virtualenv` (once you've finished coding), you
simply run the following command:

    $ deactivate


Next Steps
----------

After you've got your application up and running, there a couple next
steps you should consider following.

1. Create a new `README.md` file.
2. Add your Google Analytics ID to the `base.html` template.
3. Adjust the `author` and `description` `<meta>` tags in the
   `base.html` template.
4. Change the `humans.txt` and `favicon.ico` files in the `static`
   directory.
5. Change the `apple-touch` icons in the `static` directory.


Reactivating the Virtual Environment
------------------------------------

If you haven't worked with `virtualenv` before, you'll need to
reactivate the environment everytime you close or reload your terminal.

    $ source env/bin/activate

If you don't reactivate the environment, then you'll probably receive a
screen full of errors when trying to run the application locally.


Adding Requirements
-------------------

In the course of creating your application, you may find yourself
installing various Python modules with `pip` -- in which case you'll
need to update the `requirements.txt` file. One way that this can be
done is with `pip freeze`.

    $ pip freeze > requirements.txt


Custom Domains
--------------

If your account is verified -- and your credit card is on file -- you
can also easily add a custom domain to your application.

    $ heroku addons:add custom_domains
    $ heroku domains:add www.mydomainname.com

You can add a [naked domain
name](http://devcenter.heroku.com/articles/custom-domains), too.

    $ heroku domains:add mydomainname.com

Lastly, add the following A records to your DNS management tool.

    75.101.163.44
    75.101.145.87
    174.129.212.2
