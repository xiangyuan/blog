public: yes
tags: [Webdesign]

Attachment Icons for Drupal
===========================

If you want to add filetype-specific icons to Drupal attachments (or
html file links in general), try this CSS:

::

    table#attachments a[href$='.pdf']
    {
      padding-left: 20px;
      background: transparent url(icon-pdf.png) no-repeat center left;
    }

    table#attachments a[href$='.zip'], table#attachments a[href$='.rar']
    {
      padding-left: 20px;
      background: transparent url(icon-zip.png) no-repeat center left;
    }

Tested in IE7, IE8, and Firefox 3.5

(Via
`redpanda.ch <http://www.redpanda.ch/blog/drupal/dateianh%C3%A4nge-attachments-mit-file-icons.html?quicktabs_1=0>`_)

