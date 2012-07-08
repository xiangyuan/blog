public: yes
tags: [Linux]

Create 30-sec soundsamples with SoX
===================================

To create 30-second sound samples (e.g. for audio previews of songs) from existing tracks on
GNU/Linux, you can use `SoX <http://linux.die.net/man/1/sox>`_.

This command will create a 30-second sample starting at 30 seconds into the song, with a 2-second
fade-in and a 2-second fade-out:

.. sourcecode:: bash

    $ sox song-full.wav song-sample.wav trim 30 30 fade 0:2 0:30 0:2

It's possible that with Ubuntu sox doesn't convert mp3 files, as it has been compiled without mp3
support. In that case, either recompile sox or pipe the output into lame (or another encoder):

.. sourcecode:: bash

    $ sox song-full.wav -t wav - trim 30 30 fade 0:2 0:30 0:2 | lame - song-sample.mp3

E.g. to convert all .flac files in the current directory to mp3 samples, issue this command:

.. sourcecode:: bash

    for file in ./*.flac ; do sox $file -t wav - trim 30 30 fade 0:2 0:30 0:2 | lame - $file.sample.mp3; done
