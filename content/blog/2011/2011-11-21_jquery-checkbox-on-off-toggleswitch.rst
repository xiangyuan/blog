jQuery On-Off Toggle/Switch
===========================

:tags: webdev, javascript
:summary: On-Off switches with HTML, CSS and jQuery.

Today I was looking for a nice graphical on/off switch to replace
checkboxes on a webpage I'm working on. I found `a beautiful
solution <http://devgrow.com/iphone-style-switches/>`_, but the button
was too large. Instead of changing the button size, I made my own switch
using jQuery JavaScript and CSS.

This is what it looks like:

.. image:: /static/img/2011/11/21/screenshot_toggles.png
   :alt: Screenshot of Toggles

1. HTML
-------

.. sourcecode:: html

    <div class="switch">
        <label for="mycheckbox" class="switch-toggle" data-on="On" data-off="Off"></label>
        <input type="checkbox" id="mycheckbox" />
    </div>
      
The element containing the checkbox and the label should have the class
``switch`` assigned. The label element needs the class ``switch-toggle``
as well as the ``data-on`` and ``data-on`` attributes to define the
label texts for the two statuses.

It is important that the ``.switch`` element contains only one checkbox
and that the checkbox and the label are direct children of the
``.switch`` element.

2. CSS
------

.. sourcecode:: css

    label.switch-toggle {
        background: url('switch.png') repeat-y;
        display: block !important;
        height: 12px;
        padding-left: 26px;
        cursor: pointer;
        display: none;
    }
    label.switch-toggle.on {
        background-position: 0px 12px;
    }
    label.switch-toggle.off {
        background-position: 0px 0px;
    }
    label.switch-toggle.hidden {
        display: none;
    }

Don't forget to download the `switch.png file </static/img/2011/11/21/switch.png>`_.

3. jQuery
---------

.. sourcecode:: javascript

    $(document).ready( function(){ 
        $('.switch').each(function() {
            var checkbox = $(this).children('input[type=checkbox]');
            var toggle = $(this).children('label.switch-toggle');

            if (checkbox.length) {
                checkbox.addClass('hidden');
                toggle.removeClass('hidden');
                if (checkbox[0].checked) {
                    toggle.addClass('on');
                    toggle.removeClass('off');
                    toggle.text(toggle.attr('data-on'));
                } else {
                    toggle.addClass('off');
                    toggle.removeClass('on');
                    toggle.text(toggle.attr('data-off'));
                };  
            }   
        }); 

        $('.switch-toggle').click(function(){
            var checkbox = $(this).siblings('input[type=checkbox]')[0];
            var toggle = $(this);

            // We need to inverse the logic here, because at the time of processing,
            // the checked status has not been enabled yet.
            if (checkbox.checked) {
                toggle.addClass('off');
                toggle.removeClass('on');
                toggle.text(toggle.attr('data-off'));
            } else {
                toggle.addClass('on');
                toggle.removeClass('off');
                toggle.text(toggle.attr('data-on'));
            };  
        }); 
    });

Yes, I violated the DRY principle, but the logic works, so that's good enough
for now ;)

(Credits: The image used was taken from the `Heise's socialshareprivacy
plugin <http://www.heise.de/extras/socialshareprivacy/>`__.)
