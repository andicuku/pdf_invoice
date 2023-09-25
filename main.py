import os

from pdfplumber.pdf import PDF

from utils import extract_spv, extract_address, extract_description, extract_total, \
    extract_date, dump_dict_to_excel


def prepare_dictionary_with_data(text: str) -> dict:
    return {
        "Reference Date": extract_date(text),
        "SPV": extract_spv(text),
        "Address": extract_address(text),
        "Description": extract_description(text),
        "Price": extract_total(text, 1),
        "Quantity": extract_total(text, -1),
        "VAT": extract_total(text, 2),
        "Total": extract_total(text, 0),
    }


def main():
    pdfs = ['test.pdf', 'test_1.pdf']
    list_of_data = []
    for pdf in pdfs:
        with PDF.open(f"pdf_directory/{pdf}") as pdf:
            list_of_data.append(prepare_dictionary_with_data(pdf.pages[0].extract_text()))

    if not os.path.isdir("reports"):
        os.mkdir("reports")

    dump_dict_to_excel(list_of_data, "reports/pdf_to_excel.xlsx")


if __name__ == '__main__':
    main()
