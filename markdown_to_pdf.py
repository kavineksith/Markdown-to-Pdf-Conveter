import markdown
import pdfkit
import logging
import sys
import os

# Custom exception for Markdown to PDF conversion errors
class MarkdownToPDFConversionError(Exception):
    def __init__(self, message):
        super().__init__(message)

# Class to handle Markdown to PDF conversion
class MarkdownToPDFConverter:
    def __init__(self, markdown_file, output_pdf_path):
        """
        Initializes the MarkdownToPDFConverter with the input and output file paths.
        :param markdown_file: Path to the input Markdown file.
        :param output_pdf_path: Path to save the output PDF file.
        """
        self.markdown_file = markdown_file
        self.output_pdf_path = output_pdf_path

    def read_markdown(self):
        """
        Reads the content of the Markdown file.
        :return: The content of the markdown file as a string.
        :raises MarkdownToPDFConversionError: If file reading fails.
        """
        try:
            with open(self.markdown_file, 'r', encoding='utf-8') as file:
                logging.info(f"Successfully opened Markdown file: {self.markdown_file}")
                return file.read()
        except FileNotFoundError:
            logging.error(f"Markdown file '{self.markdown_file}' not found.")
            raise MarkdownToPDFConversionError(f"Markdown file '{self.markdown_file}' not found.")
        except Exception as e:
            logging.error(f"Error reading markdown file: {str(e)}")
            raise MarkdownToPDFConversionError(f"Error reading markdown file: {str(e)}")

    def convert_to_html(self, markdown_text):
        """
        Converts the Markdown content to HTML.
        :param markdown_text: The raw Markdown text.
        :return: HTML content as a string.
        """
        logging.info("Converting Markdown to HTML.")
        return markdown.markdown(markdown_text)

    def apply_css_styles(self, html_content):
        """
        Applies CSS styles to the HTML content for PDF layout.
        :param html_content: The HTML content to be styled.
        :return: The styled HTML content as a string.
        """
        css = """
        <style>
            @page {
                size: A4;
                margin: 20mm;
            }

            body {
                font-family: Arial, sans-serif;
                line-height: 1.6;
                padding: 15mm;
            }

            h1, h2, h3 {
                color: #333;
            }

            p {
                margin-bottom: 10px;
            }

            ul {
                padding-left: 20px;
            }

            li {
                margin-bottom: 5px;
            }

            .page-number {
                position: fixed;
                bottom: 10mm;
                right: 10mm;
                font-size: 10px;
                color: #333;
            }
        </style>
        """
        logging.info("Applying CSS styles to HTML.")
        # Add CSS styles to the HTML content
        return f"<html><head>{css}</head><body>{html_content}<div class='page-number'>Page 1</div></body></html>"

    def convert_to_pdf(self, html_content):
        """
        Converts the styled HTML content to a PDF file.
        :param html_content: The styled HTML content.
        :raises MarkdownToPDFConversionError: If PDF generation fails.
        """
        try:
            logging.info(f"Converting HTML to PDF: {self.output_pdf_path}")
            pdfkit.from_string(html_content, self.output_pdf_path, options={"page-size": "A4"})
            logging.info(f"PDF successfully created at {self.output_pdf_path}")
        except Exception as e:
            logging.error(f"Error generating PDF: {str(e)}")
            raise MarkdownToPDFConversionError(f"Error generating PDF: {str(e)}")

    def process_conversion(self):
        """
        Orchestrates the process of converting a Markdown file to a styled PDF.
        :raises MarkdownToPDFConversionError: If any error occurs during conversion.
        """
        try:
            # Read Markdown file content
            markdown_text = self.read_markdown()

            # Convert Markdown to HTML
            html_content = self.convert_to_html(markdown_text)

            # Apply CSS styles to HTML
            styled_html = self.apply_css_styles(html_content)

            # Convert the styled HTML to PDF
            self.convert_to_pdf(styled_html)
        except MarkdownToPDFConversionError as e:
            logging.error(f"Conversion failed: {e}")
            sys.exit(1)  # Exit with a failure code

# Function to configure logging
def configure_logging():
    """
    Configures logging for the script.
    Logs events to both console and a log file.
    """
    log_filename = "conversion_log.log"
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_filename),
            logging.StreamHandler()
        ]
    )
    logging.info("Logging configured. Logs will be saved in 'conversion_log.log'.")

# Main function to handle command-line arguments and trigger conversion
def main():
    # Ensure correct number of arguments
    if len(sys.argv) != 3:
        print("Usage: python markdown_to_pdf.py <input_markdown_file> <output_pdf_file>")
        sys.exit(1) # Exit with a failure code

    markdown_file = sys.argv[1]  # Input Markdown file
    output_pdf = sys.argv[2]     # Output PDF file

    # Check if the input Markdown file exists
    if not os.path.isfile(markdown_file):
        print(f"Error: The file '{markdown_file}' does not exist.")
        logging.error(f"Markdown file '{markdown_file}' not found.")
        sys.exit(1) # Exit with a failure code

    # Configure logging
    configure_logging()

    # Create an instance of the MarkdownToPDFConverter class
    converter = MarkdownToPDFConverter(markdown_file, output_pdf)

    # Start the conversion process
    converter.process_conversion()

# Run the main function if this script is executed directly
if __name__ == "__main__":
    main()
    sys.exit(0)  # Exit with success code
