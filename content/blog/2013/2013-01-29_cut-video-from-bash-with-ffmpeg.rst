public: yes
tags: [bash, linux, movie editing]
language: en
summary: |
    How to cut a video in your terminal.

Cut Videos from Bash with ffmpeg
================================

Sometimes I want an easy way to cut off some parts of a video. I don't want to
use a full-fledged movie editing software for a simple thing like that and I
don't like having to configure any output encoding settings. `ffmpeg
<http://ffmpeg.org/>`_ offers a nice solution::

    $ ffmpeg -ss 00:03:33.0 -t 00:12:04.0 -i input.mp4 -acodec copy -vcodec copy -async 1 output.mp4

Time format is `hh:mm:ss.x`. The output video will start at `3min33s` and end
after `12min4s` at `15min37s`.

The `-acodec copy` and `-vcodec copy` parameters ensure that the audio and video
codec settings used are copied from the input video.

If you only want to cut off a part in the beginning, just leave away the `-t`
option.

Source: http://superuser.com/questions/138331/using-ffmpeg-to-cut-up-video
