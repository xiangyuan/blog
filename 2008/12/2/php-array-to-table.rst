public: yes
tags: [Webdesign]

PHP Array to Table
==================

Ich habe mir eine kleine PHP-Funktion geschrieben, welche ein
eindimensionales Array in eine mehrspaltige Tabelle verwandelt.

::

    /**
     * Generates a multi-column table from an array 
     *
     * @version 0.9  
     * @param array     Array to process 
     * @param columns   Number of columns to return  
     * @optional id     ID attribute to attach to the table
     * @optional class  CSS class attribute to attach to the table 
     */
    function generate_table($array, $columns, $table_id='', $table_class='') {
        $array_size = count($array);
        $col_size = ceil($array_size / $columns);
        
        $table = "'.$array[$i+$j*$col_size].'' : ' ';
            }
            $table .= "\n";
        }
        $table .= "\n";
        
        return $table;
    }

Verbesserungsvorschläge und Flame-Attacken sind willkommen ;)

