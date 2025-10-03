import cv2
import pytesseract
import numpy as np
from PIL import Image
import os
from pathlib import Path
import sys

# Set Tesseract path (Windows users - adjust path if needed)
if os.name == 'nt':  # Windows
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

class SimpleOCR:
    def __init__(self):
        self.supported_formats = {'.jpg', '.jpeg', '.png', '.pdf'}
    
    def preprocess_image(self, image_path):
        """Basic image preprocessing for better OCR"""
        try:
            # Read image
            image = cv2.imread(image_path)
            if image is None:
                return None, "Could not read image"
            
            # Convert to grayscale
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            
            # Apply threshold
            _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
            
            return thresh, "Success"
        except Exception as e:
            return None, f"Error processing image: {str(e)}"
    
    def extract_text(self, image_path):
        """Extract text from image"""
        try:
            # Check file format
            file_ext = Path(image_path).suffix.lower()
            if file_ext not in self.supported_formats:
                return False, f"Unsupported format: {file_ext}. Use JPG, PNG, or PDF."
            
            if file_ext == '.pdf':
                return self.extract_from_pdf(image_path)
            else:
                return self.extract_from_image(image_path)
                
        except Exception as e:
            return False, f"Error: {str(e)}"
    
    def extract_from_image(self, image_path):
        """Extract text from single image"""
        processed_image, message = self.preprocess_image(image_path)
        if processed_image is None:
            return False, message
        
        # Extract text using Tesseract
        try:
            text = pytesseract.image_to_string(processed_image, lang='eng')
            text = self.clean_text(text)
            
            if not text.strip():
                return False, "No text found in image. Try a clearer image."
            
            return True, text
        except Exception as e:
            return False, f"OCR Error: {str(e)}"
    
    def extract_from_pdf(self, pdf_path):
        """Extract text from PDF (simplified - requires pdf2image)"""
        try:
            from pdf2image import convert_from_path
            
            images = convert_from_path(pdf_path, dpi=300)
            all_text = ""
            
            for i, image in enumerate(images):
                # Save temporary image
                temp_path = f"temp_page_{i}.png"
                image.save(temp_path, 'PNG')
                
                # Extract text from page
                success, text = self.extract_from_image(temp_path)
                if success:
                    all_text += f"--- Page {i+1} ---\n{text}\n\n"
                
                # Clean up temp file
                if os.path.exists(temp_path):
                    os.remove(temp_path)
            
            if not all_text.strip():
                return False, "No text found in PDF"
            
            return True, all_text
            
        except ImportError:
            return False, "PDF support requires: pip install pdf2image"
        except Exception as e:
            return False, f"PDF Error: {str(e)}"
    
    def clean_text(self, text):
        """Clean extracted text"""
        lines = [line.strip() for line in text.split('\n') if line.strip()]
        return '\n'.join(lines)
    
    def save_text(self, text, output_path):
        """Save text to file"""
        try:
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(text)
            return True, f"Text saved to: {output_path}"
        except Exception as e:
            return False, f"Error saving file: {str(e)}"

def main():
    """Simple command-line interface"""
    ocr = SimpleOCR()
    
    print("=" * 50)
    print("       SIMPLE OCR TEXT EXTRACTOR")
    print("=" * 50)
    
    while True:
        print("\nOptions:")
        print("1. Extract text from image/PDF")
        print("2. Exit")
        
        choice = input("\nEnter your choice (1-2): ").strip()
        
        if choice == '1':
            file_path = input("Enter image/PDF file path: ").strip().strip('"')
            
            if not os.path.exists(file_path):
                print("❌ File not found!")
                continue
            
            print("⏳ Processing...")
            success, result = ocr.extract_text(file_path)
            
            if success:
                print("✅ Text extracted successfully!")
                print("\n" + "="*30)
                print("EXTRACTED TEXT:")
                print("="*30)
                print(result[:500] + "..." if len(result) > 500 else result)
                print("="*30)
                
                # Ask to save
                save = input("\nSave to file? (y/n): ").lower().strip()
                if save == 'y':
                    output_path = input("Output file path (default: extracted_text.txt): ").strip()
                    if not output_path:
                        output_path = "extracted_text.txt"
                    
                    save_success, message = ocr.save_text(result, output_path)
                    if save_success:
                        print(f"✅ {message}")
                    else:
                        print(f"❌ {message}")
            else:
                print(f"❌ {result}")
        
        elif choice == '2':
            print("Goodbye!")
            break
        
        else:
            print("❌ Invalid choice!")

if __name__ == "__main__":
    main()