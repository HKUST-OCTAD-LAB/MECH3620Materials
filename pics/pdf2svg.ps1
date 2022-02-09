Get-ChildItem -Filter *.pdf | Foreach-Object{
    pdf2svg $_.FullName "$($_.BaseName).svg"
}