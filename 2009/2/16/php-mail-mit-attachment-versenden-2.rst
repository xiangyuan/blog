public: yes
tags: [Webdesign]

PHP Mail mit Attachment versenden
=================================

Hmpf, letzte Woche hab ich etwa drei Stunden erfolglos mit dem Versuch
verbracht, ein Mail mit Anhang per PHP zu versenden. Heute hab ich
gemerkt dass ich den Mailheader zwar in eine Variable gespeichert hab,
diese aber nie übergeben habe... \*head->wall\*

So funktionierts:

::

     0)
    {
        // Mailangaben werden zusammengestellt
        $sender = trim($_POST['email']);
        $receiver = "receiver@example.com";
        $subject = (isset($_POST['betreff']) ? trim($_POST['betreff']) : 'Supportanfrage');
        $attachment = chunk_split(base64_encode(file_get_contents($file['tmp_name'])));
        
        // Mailheader zusammenstellen
        $random_hash = md5(date('r', time()));
        $mailheader = "MIME-Version: 1.0\r\n";
        $mailheader .= "From:".$name." <".$sender.">\r\n";
        $mailheader .= "Content-Type: multipart/mixed; boundary=\"".$random_hash."\"\r\n";
        
        // Mailbody
        $mailbody = "--".$random_hash;  
        $mailbody .= "\nContent-Type: multipart/alternative; boundary=\"".$random_hash."\""; 
        
        $mailbody .= "\n\n--".$random_hash; 
        $mailbody .= "\nContent-Type: text/plain; charset=\"iso-8859-1\""; 
        $mailbody .= "\nContent-Transfer-Encoding: 7bit"; 
        
        $mailbody .= "\n\n".$message;
        
        $mailbody .= "\n\n--".$random_hash; 
        $mailbody .= "\nContent-Type: application/zip; name=\"attachment.zip\""; 
        $mailbody .= "\nContent-Transfer-Encoding: base64";
        $mailbody .= "\nContent-Disposition: attachment";
        
        $mailbody .= "\n\n".$attachment;
        $mailbody .= "\n--".$random_hash."--";
        
        // E-Mail versenden
        mail($receiver,$subject,$mailbody,$mailheader);
    }
    else
    {
        echo 'Fehler: Datei ist kein ZIP-Archiv.';
    }
    ?>


