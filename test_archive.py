import os
from zipfile import ZipFile, ZIP_DEFLATED
from pypdf import PdfReader


def test_zip_archive():
    resources = os.path.join(os.path.dirname(os.path.abspath(__name__)), 'files')
    csv_file = 'csv_file.csv'
    pdf_file = 'pdf_file.pdf'
    xlsx_file = 'xlsx_file.xlsx'
    files = [csv_file, pdf_file, xlsx_file]

    with ZipFile(os.path.join(resources,'archive.zip'), mode='w', compression=ZIP_DEFLATED) as my_zip:
        for file in files:
            my_zip.write(os.path.join(resources, file), file)



    with ZipFile(os.path.join(resources,'archive.zip'), mode='r') as my_zip:
        for file in my_zip.namelist():
            assert file in files

