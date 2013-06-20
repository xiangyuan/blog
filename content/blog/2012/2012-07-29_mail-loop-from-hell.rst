public: yes
tags: [internet, stories, irc]
summary: One of those awesome 90ies computer stories...

Mail Loop From Hell
===================

Found in `#django` on freenode, Jul 12, 2012. All names are edited.

::

    11:16 < abrt> since it's quiet in here I'll tell you a story.
    11:16 < abrt> back in 1992, I had just graduated university and was interning at a government facility in
                  newport news
    11:16 < abrt> along with some friends from college. We made $7.25/hr and were living large.
    11:16 < qns> hahahaha
    11:17 < qns> You sound like Kevin Mitinick.
    11:17 < abrt> we used to play practical jokes on each other all the time.
    11:17 < abrt> mitnick was a pussy compared to us
    11:17 < qns> :O
    11:17 < abrt> anyway, I managed to break into my friend's university UNIX account. guessed his password. easy.
    11:17 < abrt> how well do you know UNIX?
    11:18 < qns> not well yet
    11:18 < abrt> well, back in the day, they didn't have postfix or qmail any of these fancy mailservers
    11:18 < abrt> they ran sendmail
    11:18 < abrt> and they allowed individual .forward files
    11:19 < abrt> the purpose of the .forward file was to forward your email that came to your account to the
                  address in the .forward file.
    11:19 < abrt> anyway, after I broke into my friend Matt's account, I set up his .forward file to be
                  "everyone@***.edu" which I knew was an alias for the entire college.
    11:19 < abrt> I had just learned how to forge sendmail headers and was going to send him a very embarrassing
                  email "from his girlfriend"
    11:20 < abrt> fortunately for me, I decided to do a test run at 1730 on a Friday. Assuming the test run went
                  well, the embarrassing forged email would go out the following Monday.
    11:20 < abrt> so I sent a "this is a test" to Matt.
    11:21 < abrt> and went home, drank some beers with Matt and Steve, and had a great weekend
    11:21 < abrt> Monday morning I get into the lab and everyone's quiet, sort of whispering, and looking at me
    11:21 < abrt> fuck me, right?
    11:21 < abrt> I log into the gov UNIX system - and I have 13000 emails
    11:22 < abrt> what I had forgotten was that "everyone@***.edu" included Matt.
    11:22 < abrt> so the email would get sent to everyone, including him, then he would add 10 lines of header,
                  forward it to everyone, including him, ....
    11:22 < abrt> mail loop from hell.
    11:22 < qns> Did you get in trouble?
    11:22 < abrt> well, here's the thing
    11:22 < abrt> this was summer '92
    11:22 < abrt> nobody at school, right?
    11:23 < abrt> everyone had their email forwarded elsewhere
    11:23 < abrt> and the professors got jobs at places like Camp Peary, and FBI, and other research
                  organizations, ....
    11:23 < qns> So you help them?
    11:23 < abrt> and those systems couldn't handle the volume of mail, and they never thought to put the mail
                  spool on its on separate partition
    11:23 < abrt> so their systems crashed.
    11:24 < qns> haha
    11:24 < qns> So you triggered chaos all over.
    11:24 < abrt> I managed to bring down 13 CIA offices, all FBI offices east of the Mississippi, and the entire
                  Southeastern university Research Network.
    11:24 < etgr> You can claim to have hacked the FBI
    11:24 < qns> using e-mail.
    11:24 < abrt> along with various other systems, but those were the biggies
    11:24 < qns> I'd have shat myself
    11:24 < abrt> I pretty much did.
    11:25 < abrt> But back then, like possession of a fake ID, nobody really knew what to do to you for this sort
                  of thing
    11:25 < abrt> so I got a slap on the wrist, almost fired, and had to write a letter of apology to the head of
                  the computer lab at university
    11:25 < abrt> and I lost my university email account. :(
    11:26 < qns> hahahahaha
    11:26 < abrt> today I'd probably be sent to Guantanamo
    11:26 < qns> Or you'd mysteriously disappear.  :P
    11:26 < abrt> anyway, that's my story for the evening.
    11:26 < qns>  I need a story like that on my resume.
    11:26 < abrt> nah
    11:26 < abrt> here's the thing
    11:26 < abrt> that story doesn't go on a resume
    11:27 < abrt> but - fast forward 10 years later.
    11:27 < qns> Ahh
    11:27 < abrt> I'm getting my clearance
    11:27 < abrt> being interviewed by the suits from OPM
    11:27 < abrt> and they leave the room, come back with a folder, and say, "Tell us about SURANet and the CIA
                  in 1992"
    11:27 < abrt> THAT's when I shat myself.
    11:28 < abrt> BUT - good news - I got my clearance despite my history :)
    11:28 < qns> Were they impressed?
    11:28 < abrt> nah, they were laughing

After reading this story, I started a new list on kippt: `Stories from the Internet
<https://kippt.com/dbrgn/stories-from-the-internet>`__. Feel free to follow it, and also send me new candidates
if you know of any :)
