## Markdown to PDF Converter Documentation

### Overview:
This Python script converts a Markdown file to a styled PDF. The script:
1. Reads a Markdown file provided as input.
2. Converts the Markdown content to HTML.
3. Applies custom CSS styles for layout and formatting.
4. Converts the styled HTML to a PDF and saves it to the specified output path.
5. Logs all actions and errors to a log file.
6. Accepts command-line arguments for the input Markdown file and the output PDF file.

### Features:
- **CSS Styling**: The script applies predefined CSS for the PDF layout (e.g., margins, font styles, page size).
- **Logging**: Logs the execution process, including successes and errors, to both a log file and the console.
- **Command-Line Arguments**: Uses `sys.argv` to allow users to provide input and output file paths via the command line.

---

### Requirements:

1. **Python 3.x**: The script is written in Python 3.x.
2. **Required Python Libraries**:
   - `markdown`: To convert Markdown to HTML.
   - `pdfkit`: To convert HTML to PDF.
   - `logging`: For logging events.
   - `sys`: To handle command-line arguments.
   - `os`: To check for file existence.
   
   Install the required libraries:
   ```bash
   pip install markdown pdfkit
   ```

3. **External Dependency**:
   - `wkhtmltopdf`: `pdfkit` depends on `wkhtmltopdf` to generate PDFs from HTML. Make sure it's installed:
     - On macOS: `brew install wkhtmltopdf`
     - On Linux: `sudo apt install wkhtmltopdf`
     - On Windows: [Download wkhtmltopdf](https://wkhtmltopdf.org/downloads.html)

---

### Script Usage:

1. **Command-Line Arguments**:
   The script accepts two command-line arguments:
   - **Input Markdown File**: Path to the Markdown file to be converted.
   - **Output PDF File**: Path to save the generated PDF.

   Example:
   ```bash
   python markdown_to_pdf.py input.md output.pdf
   ```

   Where:
   - `input.md` is the Markdown file.
   - `output.pdf` is the generated PDF.

2. **Log File**:
   - The script creates a log file named `conversion_log.log` in the same directory as the script.
   - Logs include timestamps, actions (e.g., file opened, conversion started), and error messages.

---

### Script Structure:

#### 1. **MarkdownToPDFConversionError (Custom Exception)**:
   - A custom exception class used to handle errors during the conversion process.
   - Provides a meaningful error message when an error occurs (e.g., file not found, conversion failure).

#### 2. **MarkdownToPDFConverter Class**:
   This class encapsulates the process of converting a Markdown file to PDF:
   - **`__init__(self, markdown_file, output_pdf_path)`**: Initializes the converter with the input Markdown file and output PDF path.
   - **`read_markdown(self)`**: Reads the content of the Markdown file and returns it as a string. If the file doesn't exist, raises a `MarkdownToPDFConversionError`.
   - **`convert_to_html(self, markdown_text)`**: Converts the Markdown content to HTML.
   - **`apply_css_styles(self, html_content)`**: Applies predefined CSS styles to the HTML content (margins, font styles, page layout).
   - **`convert_to_pdf(self, html_content)`**: Converts the styled HTML content into a PDF and saves it to the specified output path. If the conversion fails, raises a `MarkdownToPDFConversionError`.
   - **`process_conversion(self)`**: Orchestrates the entire conversion process: reading the Markdown, converting to HTML, applying CSS, and generating the PDF.

#### 3. **Logging**:
   - The script uses Python's built-in `logging` module to log events and errors.
   - Logs both to the console and to a log file (`conversion_log.log`).
   - Log levels include `INFO` for normal actions and `ERROR` for issues encountered during the process.

#### 4. **Command-Line Arguments (sys.argv)**:
   - The script expects two arguments: the input Markdown file path and the output PDF file path.
   - It checks for the correct number of arguments and validates the input file's existence before proceeding.

#### 5. **Main Function**:
   - Configures logging.
   - Handles command-line arguments.
   - Creates an instance of the `MarkdownToPDFConverter` class and calls `process_conversion()` to perform the conversion.

---

### Logging Details:

- **Log File**: `conversion_log.log`
   - **INFO logs**: Include successful steps like file opening, HTML conversion, and PDF creation.
   - **ERROR logs**: Include issues such as file reading errors, conversion failures, or missing dependencies.

   Example log entry:
   ```
   2025-01-26 12:34:56,789 - INFO - Successfully opened Markdown file: input.md
   2025-01-26 12:34:56,790 - INFO - Converting Markdown to HTML.
   2025-01-26 12:34:56,791 - INFO - Applying CSS styles to HTML.
   2025-01-26 12:34:56,792 - INFO - Converting HTML to PDF: output.pdf
   2025-01-26 12:34:56,794 - INFO - PDF successfully created at output.pdf
   ```

---

### Error Handling:

- **File Not Found**: If the Markdown file doesn't exist or cannot be opened, a `MarkdownToPDFConversionError` is raised and logged, and the program exits with an error code.
  
- **PDF Generation Failure**: If the PDF generation fails (e.g., `wkhtmltopdf` is not properly installed), a `MarkdownToPDFConversionError` is raised and logged.

---

### Example:

1. **Create a Markdown file** (e.g., `input.md`):
   ```markdown
   # Sample Markdown Document

   This is a simple markdown to PDF conversion example.

   ## Features

   - Convert markdown to HTML
   - Convert HTML to PDF
   - Customize PDF layout with A4 size and margins

   ## Conclusion

   This demonstrates how you can adjust PDF layout using Python and CSS.
   ```

2. **Run the Script**:
   ```bash
   python markdown_to_pdf.py input.md output.pdf
   ```

3. **Check the Log File** (`conversion_log.log`):
   The log file will contain details of the conversion process, including any errors encountered.

---

### Conclusion:

This script provides a flexible and automated way to convert Markdown files to PDF while applying custom styling. It offers robust error handling, logging, and command-line interface support, making it suitable for both individual and batch processing scenarios.


## **License**

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## **Disclaimer:**

Kindly note that this project is developed solely for educational purposes, not intended for industrial use, as its sole intention lies within the realm of education. We emphatically underscore that this endeavor is not sanctioned for industrial application. It is imperative to bear in mind that any utilization of this project for commercial endeavors falls outside the intended scope and responsibility of its creators. Thus, we explicitly disclaim any liability or accountability for such usage.