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
    with PDF.open("pdf_directory/test.pdf") as pdf:
        dump_dict_to_excel(prepare_dictionary_with_data(pdf.pages[0].extract_text()), f'reports/{pdf.path.name}.xlsx')

    with PDF.open("pdf_directory/test_1.pdf") as pdf:
        dump_dict_to_excel(prepare_dictionary_with_data(pdf.pages[0].extract_text()), f'reports/{pdf.path.name}.xlsx')


if __name__ == '__main__':
    main()
