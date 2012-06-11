public: yes
tags: [Arbeitsalltag,Ubuntu,Linux]

Using Evolution with Exchange 2007
==================================

Today I tried configuring Evolution 2.28.3 with our MS Exchange 2007
server. Unfortunately, it did not work, the following error message was
displayed:

    The server is running Exchange 5.5. Exchange Connector supports
    Microsoft Exchange 2000 and 2003 only.

To be able to access Exchange 2007 anyways, install the
``evolution-mapi`` package (Ubuntu) and use the servertype "Exchange
MAPI" instead of "Microsoft Exchange".

