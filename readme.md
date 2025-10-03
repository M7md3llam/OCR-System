# OCR Text Extractor - README

## What is this?
A simple tool that can **read text from images and PDF files** and convert them into **editable text files**. Just take a picture of a document, and this app will extract all the text for you!

## What can it do?
- 📷 Read text from photos (JPG, PNG files)
- 📄 Read text from PDF documents
- 💾 Save extracted text as:
  - Text files (.txt)
  - PDF files (.pdf) 
  - Image files (.jpg, .png)
- 🌐 Web interface for easy use
- ⚡ Automatic quality checking - tells you if your image is too blurry

## Quick  Setup (5 minutes)

### Step 1: Install Tesseract (The Brain)
**Windows:**
1. Download from: https://github.com/UB-Mannheim/tesseract/wiki
2. Run the installer
3. Use default settings

**Mac:**
```bash
brew install tesseract
```

**Linux:**
```bash
sudo apt install tesseract-ocr
```

### Step 2: Install Python Packages
Open command prompt/terminal and run:
```bash
pip install opencv-python pytesseract Pillow numpy flask
```

### Step 3: Run the App!
**Option A - Simple Text Interface:**
```bash
python ocr_app.py
```

**Option B - Web Browser Interface:**
```bash
python web_ocr.py
```
Then open: http://localhost:5000

## How to Use

### Using the Text Interface:
1. Run `python ocr_app.py`
2. Press `1` to extract text
3. Enter your image file path (like `C:/Users/You/Desktop/my_document.jpg`)
4. See the extracted text!
5. Press `y` to save it to a file

### Using the Web Interface:
1. Run `python web_ocr.py`
2. Open your web browser to http://localhost:5000
3. Click "Choose File" and pick your image/PDF
4. Click "Extract Text"
5. Download your text file!

## Example
**You have:** A photo of a printed document
**The app does:** Reads the text from the photo
**You get:** A text file with all the text that you can edit in Word or any text editor

## Tips for Best Results
- ✅ Use good lighting when taking photos
- ✅ Make sure text is clear and not blurry
- ✅ Take pictures straight (not at an angle)
- ✅ High contrast (black text on white background works best)
- ❌ Avoid shadows on the document
- ❌ Avoid handwritten text (works best with printed text)
- ❌ Avoid very fancy fonts

## What if it doesn't work?

### Common Problems:

**"Tesseract not found" error:**
- Make sure you installed Tesseract correctly
- On Windows, the app should find it automatically

**"No text found":**
- Try a clearer image
- Better lighting
- Straighten the image

**File not found:**
- Check your file path
- Make sure the file exists

**PDF doesn't work:**
- Install extra package: `pip install pdf2image`

## Need More Features?

The full version can also:
- Run in the background and automatically process new files
- Process multiple files at once
- Give you a quality score for your images
- Work as a continuous service

## Files in this Project:
- `ocr_app.py` - Simple text interface (start here!)
- `web_ocr.py` - Web browser interface
- `ocr_system.py` - Full advanced system
- `ocr_daemon.py` - Background service version

## Just Want to Try It?
Start with `ocr_app.py` - it's the easiest to use!

## Support
If you have problems:
1. Make sure Tesseract is installed
2. Check your image quality
3. Try a different image file

## Perfect For:
- Digitizing printed documents
- Extracting text from screenshots
- Converting PDFs to editable text
- Archiving paper documents digitally

---

**Remember:** Start with `python ocr_app.py` for the simplest experience!🚀