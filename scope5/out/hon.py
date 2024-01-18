import PyPDF2

# Open the PDF file in read binary mode
with open('C:/Users/maria/OneDrive/Desktop/Dev/Uni/HKBU/comp3115/final_project/scope5/out/Thomas Wright_Europe Lost Decade in Survival Global Politics and Strategy.pdf', 'rb') as pdf_file:
    
    # Create a PDF reader object
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)
    
    # Get the number of pages in the PDF file
    num_pages = pdf_reader.getNumPages()
    
    # Loop through each page and extract the text
    for page_num in range(num_pages):
        
        # Get the page object
        page_obj = pdf_reader.getPage(page_num)
        
        # Extract the text from the page object
        page_text = page_obj.extractText()
        
        # Print the text
        print(page_text)

