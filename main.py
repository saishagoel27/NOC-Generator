import re
from noc_generator import generate_noc
from pdf_convertor import text_to_pdf

def main():
    print("===== NOC Generator =====")
    
    # Input from user
    guest_name = input("Enter guest name: ")
    if not guest_name.strip():
        print("Guest name cannot be empty!")  
        return
    
    guest_profession = input("Enter guest profession: ")
    company_name = "Mishka Productions"  
    host_name = "Mr. Kunal Kulkarni"  
    recording_date = input("Enter recording date (e.g., 26th April 2025): ")
    recording_time = input("Enter recording time (e.g., 3:00 PM to 5:00 PM): ")
    recording_location = input("Enter recording location: ")

    # generating NOC
    print("\nGenerating NOC document...")
    noc_document = generate_noc(
        guest_name, guest_profession, company_name, host_name,
        recording_date, recording_time, recording_location
    )

    # NOC generation success check
    print("\n===== Generated NOC Document =====")
    print(noc_document)

    # Handling weird characters
    noc_document_cleaned = noc_document.replace("’", "'").replace("�", "'")

    # try to save as txt file
    filename_raw = f"NOC_{guest_name}"
    safe_filename = re.sub(r'[^a-zA-Z0-9_]', '_', filename_raw) + ".txt"
    try:
        with open(safe_filename, "w", encoding="utf-8") as file:
            file.write(noc_document_cleaned)
        print(f"\n✅ Text file saved as '{safe_filename}'")
    except Exception as e:
        print(f"\n❌ Error saving .txt file: {e}")
        return

    # Ask user if they want to review the NOC
    review_choice = input("\nDo you want to review and edit the NOC before generating the PDF? (yes/no): ").strip().lower()

    if review_choice == "yes":
        print(f"➡️ Please open '{safe_filename}' in a text editor and make any changes.")
        input("Press Enter once you're done and ready to create the PDF...")
    try:
        with open(safe_filename, "r", encoding="utf-8") as file:
            final_text = file.read()
    except Exception as e:
        print(f"❌ Failed to read file for PDF generation: {e}")
        return

    # convert the txt to PDF (using fpdf)
    pdf_filename = safe_filename.replace(".txt", ".pdf")
    success, result = text_to_pdf(final_text, pdf_filename)
    if success:
        print(f"PDF created as '{result}'")
    else:
        print(f"Error creating PDF: {result}")

if __name__ == "__main__":
    main()
