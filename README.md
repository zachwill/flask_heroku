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
[heroku](https://www.heroku.com/) as fast as possible. For added
convenience, the templates use [Twitter's Bootstrap
project](http://twitter.github.com/bootstrap/) to help reduce the amount
of time it's takes you as a developer to go from an idea to a working
site.

All of the CSS stylesheets are written using the [Less
CSS](http://lesscss.org/) syntax (even Bootstrap's CSS). If you're using
Mac OS X for development, make sure to check out [incident57's
Less.app](http://incident57.com/less/).

Lastly, in heroku's production environment, your Flask application will
be served through the [gevent Python module](http://www.gevent.org/)
WSGI server.


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

Second, let's download `pip`, `virtualenv`, and the [`heroku` Ruby
gem](http://devcenter.heroku.com/articles/using-the-cli).

    $ sudo easy_install pip
    $ sudo pip install virtualenv
    $ gem install heroku

Next, we'll need to install `libevent` for the `gevent` production
server. If you're operating on a Linux OS, you can `apt-get install
libevent-dev`. If you're using Mac OS X, consider installing the
[homebrew](http://mxcl.github.com/homebrew/) package manager, and run
the following command:

    $ brew install libevent

Now, you can setup an isolated environment with `virtualenv`.

    $ virtualenv --no-site-packages env
    $ source env/bin/activate

Then, let's get the requirements installed in your isolated test
environment.

    $ pip install -r requirements.txt

Now, you can run the application locally.

    $ python bootstrap.py

Or, to test the production configuration, simply run:

    $ python bootstrap.py --gevent

You can also specify what port you'd prefer to use.

    $ python bootstrap.py --port 5555

If you haven't [signed up for heroku](https://api.heroku.com/signup), go
ahead and do that. You should then be able to [add your SSH key to
heroku](http://devcenter.heroku.com/articles/quickstart), and also
`heroku login` from the commandline.

Now, to upload your application, you'll first need to do the
following:

    $ heroku create --stack cedar
    $ git push heroku master

Finally, we can scale the web process and make sure the application is
up and running.

    $ heroku scale web=1
    $ heroku ps

To get the name of your application -- and view it in your web browser
(at `my-app-name.herokuapps.com`) -- run the following:

    $ heroku apps

And, to deactivate `virtualenv` (once you've finished coding), you
simply run the following command:

    $ deactivate


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
