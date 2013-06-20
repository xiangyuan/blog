Why some software project websites suck and others don't
========================================================

:tags: internet, open source
:summary: What distinguishes a good software project website from a bad software project website.

Today I gave some thoughts to what distinguishes a good software project website
from a bad software project website (especially for open source projects).

I came up with a few must-have criteria for a good software project website:

**On the very first page, state what the software does, and what the goal of the
project is.**

More than once, I've seen project websites about a software, that provide
downloads and how-tos and everything else, but don't even explain what the
software does. If I hear about a software and open the website, the first thing
I want to know is what the software can be used for. If I can't find that
information quickly, I lose interest.

**Provide Screenshots in the main navigation**

Whether you like it or not, what many users care for are screenshots.  Feature
lists are great, but when you see some screenshots of the program in action, you
get the general Idea how it works and how user-friendly it has been designed.
Great features are useless if the UI sucks.

**Put the download section in the main navigation**

The second most important thing on a project website is the link to the download
section. It should be visible on every page, and it should provide quick, easy
download possibilities. Also, redirected downloads suck. Direct (and therefore
`wget`-able) downloadlinks are better.

**Provide documentation**

What users want and developers hate, is documentation. Great documentation can
contribute to great success. A good example of this is the area of software
frameworks. A lot of frameworks (like `CodeIgniter
<http://codeigniter.com/user_guide/>`_, `Django
<https://docs.djangoproject.com/en/1.4/>`_ and `jQuery
<http://docs.jquery.com/Main_Page>`_) are highly successful - not least because
of the great and easy-to-understand documentation. Provide good documentation
(e.g. on `ReadTheDocs <http://readthedocs.org/>`_) and don't forget to share it
with others.

**Provide a way for feedback**

Many open source projects grew over time because of user feedback. User feedback
is important. And it needs to be quick and easy. A registration for an issue
tracker is a no-go for me. If I have to register, I don't report. Allow
anonymous bugreports and feature requests, and a lot more feedback will come in.

**For OSS projects: Provide easy possibilities to participate and share code**

Among software users, there are many great and capable programmers. Many of them
have great ideas for contributions they could make. Most of them don't have the
time and motivation to track down the owner of the source repository and to ask
for the permission to contribute. And patches that can't be shared aren't fun.
Provide an e-mail address to send in patches. Or even better, use a `distributed
source code management system
<http://en.wikipedia.org/wiki/Distributed_revision_control>`_ like `Git
<http://git-scm.com/>`_. And then host it on a platform like `Github
<https://github.com/>`_, so that users can easily contribute their changes to
the main branch, without you having to manage tedious permissions.

**Stay in touch with the users**

Communicate. And provide information on how to reach you on all available
communication channels, like e-mail, IRC, twitter, facebook, forums etc. The
more there are, the better. Inform the users about updates, but don't spam them
(use newsfeeds or social networks). And answer all not-totally-stupid questions.
If you communicate, and if your software rocks, users will turn into fans.

 

A majority of the mentioned issues should be known to most people releasing
software, but apparently aren't. The project website is the first contact with
the "outer world" and in most cases best way to promote your software. Use it,
don't waste this potential.

There are probably several other important things to remember when creating a
project website. The listed ones are just some important issues that came to my
mind, the list is by no means complete.  You are free to contribute your
experiences in the comment box.
