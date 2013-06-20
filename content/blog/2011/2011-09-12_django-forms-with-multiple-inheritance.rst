public: yes
tags: [django]
summary: How to validate Django forms in a DRY way using multiple inheritance.

Django Forms with Multiple Inheritance
======================================

Sometimes you want to validate only parts of a Django form. A use case
for this would be a user profile. A user may have an extensive user
profile, but sometimes you only want to validate a subset of the form
fields, e.g. the city and the phone number, when providing a profile
edit form. On another page you might want to offer a username change. If
you try to validate one of those forms using POST data for the provided
fields only, the validation will fail because there are other mandatory
fields. In that case, Python's support for multiple inheritance may
suit you.

Multiple form inheritance
~~~~~~~~~~~~~~~~~~~~~~~~~

First, define a form for all the form field subsets you might need to
validate.

.. sourcecode:: python

    class FormA(forms.Form):
        username = forms.CharField(required=True, label=_(u'Username'))


    class FormB(forms.Form):
        city = forms.CharField(required=True, label=_(u'City'))
        phone = forms.IntegerField(required=True, label=_(u'Phone'))

Then create a third form that extends both the first and the second
form. You may also add additional fields.

.. sourcecode:: python

    class FormAB(FormA, FormB):
        language = forms.CharField(required=True, label=_(u'Language'))

Display the forms:

.. sourcecode:: python

        Change Username
        {{ formA.as_ul }}

        Change City/Phone
        {{ formB.as_ul }}

        Entire Userprofile
        {{ formAB.as_ul }}

The result looks correct:
~~~~~~~~~~~~~~~~~~~~~~~~~

.. sourcecode:: python

    >>> a = FormA({'username': 'danilo'})
    >>> a.is_valid()
    True
    >>> b = FormB({'city': 'Bern', 'phone': '0791112233'})
    >>> b.is_valid()
    True
    >>> c = FormAB({'username': 'danilo', 'city': 'Bern', 'phone': '0791112233'})
    >>> c.is_valid()
    False
    >>> c = FormAB({'username': 'danilo', 'city': 'Bern',
    ...             'phone': '0791112233', 'language': 'de'})
    >>> c.is_valid()
    True

.. image:: http://blog.ich-wars-nicht.ch/wp-content/uploads/2011/09/2011-09-12-185255_291x225_scrot.png
   :align: center
   :alt: Django form
