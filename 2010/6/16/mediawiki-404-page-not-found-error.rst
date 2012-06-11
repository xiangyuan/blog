public: yes
tags: [php,Serveradministration]

Mediawiki 404 Page Not Found Error
==================================

I recently installed a MediaWiki installation on my IIS. Most of it
worked, but every time i wanted to create a new page or click on a red
link, instead of the "edit this article" page, a "404 page not found"
error was shown.

This is a problem with IIS misconfiguration, see `Bug
18270 <https://bugzilla.wikimedia.org/show_bug.cgi?id=18270>`_ in the
wikimedia bugzilla. `Comment
19 <https://bugzilla.wikimedia.org/show_bug.cgi?id=18270#c19>`_ solves
this issue:

    Got to IIS Manager. Open Web Sites. Right click on the website and
    select Properties. Go to the Custom Errors tab. Scroll down to the
    404 error, select it and click the "Set to Default" button.

Hope this will help someone :) Cheers!

