for pdffile in *.pdf
do
	echo "processing $pdffile..."
	cp $pdffile $pdffile.bak   # make a backup
	pdf2ps $pdffile            # convert to ps
	ps2eps -B ${pdffile%.*}.ps # convert to eps and crop
	epspdf ${pdffile%.*}.eps   # convert back to pdf

	# clean up
	rm ${pdffile%.*}.eps
	rm ${pdffile%.*}.ps
done
