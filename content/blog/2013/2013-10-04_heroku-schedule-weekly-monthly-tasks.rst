Schedule Weekly or Monthly Tasks on Heroku
==========================================

:tags: heroku
:language: en
:summary: You can schedule weekly or monthly job on Heroku Scheduler using a
          nice little trick.

Current Situation
-----------------

The Heroku Cron add-on was `disabled
<https://devcenter.heroku.com/changelog-items/61>`__ in June 2012 and existing
users were migrated to the `Scheduler add-on`_. According to Heroku, the new
add-on is "superior" and should be preferred over a cronjob.

I don't know what Heroku's definition of "superior" is; the new add-on might be
better integrated into the Heroku stack and more reliable, but from a user /
feature perspective the Scheduler add-on is obviously much less powerful than a
cronjob. The main reason for this is that jobs can only be scheduled at three
pre-defined intervals: *Daily*, *Hourly* or *Every 10 Minutes*.

I'm currently working on a project where I absolutely need weekly and monthly
intervals. And the Scheduler needs to be a dyno task, not a callback URL as
supported by the `Temporize Scheduler`_.

There's also a `feature request`_ for custom frequencies on getsatisfaction
since January, but unfortunately it hasn't been replied to yet.

The Workaround
--------------

Thanks to a nice `StackOverflow answer`_ I found a workaround to this problem:
Simply "protect" a daily task using a bash if-statement. Some examples:

Run a task every Monday:

.. sourcecode:: bash

    if [ "$(date +%u)" = 1 ]; then MY_COMMAND; fi

Run a task every 1st day in a month:

.. sourcecode:: bash

    if [ "$(date +%d)" = 01 ]; then MY_COMMAND; fi

You could also run a job every year on December 24th:

.. sourcecode:: bash

    if [ "$(date +%m)" = 12 ] && [ "$(date +%d)" = 24 ]; then MY_COMMAND; fi

I think that's currently the best solution to work around this issue, much
better than hardcoding weekdays in the scheduled script.

.. _scheduler add-on: https://addons.heroku.com/scheduler
.. _temporize scheduler: https://addons.heroku.com/temporize
.. _feature request: https://getsatisfaction.com/heroku/topics/heroku_scheduler_custom_frequency_e_g_run_weekly_monthly
.. _stackoverflow answer: http://stackoverflow.com/a/18565294/284318
