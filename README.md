# Umgebung zum Signieren von Dokumenten

Mit `wkhtmltopdf` wird die .pdf-Datei aus HMTL genereiert:

<pre>
>> wkhtmltopdf --page-size A4 --margin-top 15mm --margin-bottom 15mm --margin-left 15mm --margin-right 15mm Lebenslauf.html Lebenslauf.pdf
</pre>

Mit dem Python Skript `sign.py` wird die generierte .pdf-Datei anschließend signiert:
<pre>
>> source venv/bin/activate
(venv) >> python3 sign.py
Done! Image placed on page 3 at 1.5cm, 23.6cm.
</pre>