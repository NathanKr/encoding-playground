<h2>motivation</h2>
better understanding of encoding in particular in html using python

<h2>what is encoding</h2>
encoding in computers area is actually charcter encoding. computer work with number of 0 and 1 , so how can we represent a character e.g. '3' , 'A' , '&' in a computer ??
the solution is a mapping - encoding i.e. a unique number representing each charcter.

<h2>What is unicode</h2>
unicode is a standard for consistent encoding. unicode can be implemented by few encoding methods : utf-8 , utf-16 , utf-32. utf stands for Unicode Transformation Format . more info <a href='https://en.wikipedia.org/wiki/Unicode'>here</a>


<h2>common types of character encoding methods</h2>
<ul>
<li>ascii - this is one byte per charcater mapping . thus only 256 characters can have unique mapping which is a limitation. the limitation is solved by unicode. check mapping table i.e. encoding table <a href='http://www.asciitable.com/'>here</a></li>
<li>utf-8 - one of unicode encoding methods. this is variable width charcter mapping ,  1-4 bytes per character e.g. 'A' is represented by 1 byte but 'א' by 2 bytes (check <a href='https://he.wikipedia.org/wiki/UTF-8'>here</a>). check encoding table <a href='https://www.utf8-chartable.de/'>here</a>. according to <a href='https://www.w3schools.com/html/html_charset.asp'>this</a> utf8 is the recommended encoding (called charset) in html5 specification</li>
<li>utf-32 - one of unicode encoding methods. this is fixed width charcter mapping . each charcater is mapped to 4 bytes numeric value</li>
</ul>

<h2>encoding a string --> get its mapping to bytes</h2>
<ul>
<li>given a string e.g. 'hello string' we can encode it i.e. get its mapping to numbers meaning list of bytes . but here we must specify which encoding method to use e.g. ascii , utf8 ...
</li>
<li>encoding 'hello world' using ascii encoding method will result in the following bytes  : b"\x68\x65\x6c\x6c\x6f\x20\x77\x6f\x72\x6c\x64" . \x is hex base representation and prefix b mark the string as the encoding to bytes </li>
<li>encoding a string using ascii might not result in the same list of bytes as encoding a string to utf8. it will be the same for 'hello world' because the mapping in ascii and utf8 for these characters is the same. however, encode of 'שלום עולם' to ascii will fail</li>
<li>check the file encode_string.py and encode_decode_string.py for examples</li>
<li>encode a string using the function encode(encoding_method)</li>
</ul>

<h2>decoding a string --> get string from its encoding to bytes</h2>
<ul>
<li>decode encoded string using the function decode(encoding_method)</li>
<li>check code sample of decode in decode_to_string.py and encode_decode_string.py</li>
</ul>

<h2>read an html file with hebrew content</h2>
<ul>
    <li>read an html file with hebrew text, thus encoding must be used in read. utf8 is used on file read because that's the encoding set in the html file simple_utf_8.html</li>
    <li>notice the error when encoding is not used. check figs/encoding_error.jpg</li>
</ul>


<h2>points of interest</h2>
<ul>
<li>the encoding in html is set in the charset tag. the html 5 recommendation if utf8</li>
<li>encoded string is represented in pythob by prefix b to string e.g b"\x68\x65\x6c\x6c\x6f\x20\x77\x6f\x72\x6c\x64" is ascii encoding of 'hello world'</li>
</ul>
