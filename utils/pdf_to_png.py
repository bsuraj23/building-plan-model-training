#!/usr/bin/env python3
"""
PDF to PNG Converter for Building Plan Processing
Converts PDF files to PNG images for model training
"""

import os
import argparse
from pdf2image import convert_from_path
from pathlib import Path
from tqdm import tqdm


def pdf_to_png(pdf_path, output_folder, dpi=300):
    """
    Convert a single PDF file to PNG images.
    
    Args:
        pdf_path (str): Path to input PDF file
        output_folder (str): Directory to save output PNG files
        dpi (int): Resolution for conversion (default: 300)
    """
    try:
        # Create output folder if it doesn't exist
        os.makedirs(output_folder, exist_ok=True)
        
        # Convert PDF to images
        pages = convert_from_path(pdf_path, dpi)
        
        # Get base filename without extension
        base_name = os.path.splitext(os.path.basename(pdf_path))[0]
        
        # Save each page as PNG
        for i, page in enumerate(pages, start=1):
            output_path = os.path.join(output_folder, f"{base_name}_page_{i}.png")
            page.save(output_path, 'PNG')
            print(f"Saved: {output_path}")
            
        return len(pages)
    
    except Exception as e:
        print(f"Error converting {pdf_path}: {str(e)}")
        return 0


def batch_convert_pdfs(input_folder, output_folder, dpi=300):
    """
    Convert all PDF files in a folder to PNG images.
    
    Args:
        input_folder (str): Directory containing PDF files
        output_folder (str): Directory to save output PNG files
        dpi (int): Resolution for conversion (default: 300)
    """
    # Find all PDF files
    pdf_files = list(Path(input_folder).glob('*.pdf'))
    
    if not pdf_files:
        print(f"No PDF files found in {input_folder}")
        return
    
    print(f"Found {len(pdf_files)} PDF files")
    
    total_pages = 0
    for pdf_file in tqdm(pdf_files, desc="Converting PDFs"):
        pages_converted = pdf_to_png(str(pdf_file), output_folder, dpi)
        total_pages += pages_converted
    
    print(f"\nConversion complete! Total pages converted: {total_pages}")


def main():
    parser = argparse.ArgumentParser(
        description='Convert PDF building plans to PNG images'
    )
    parser.add_argument(
        'input',
        help='Input PDF file or folder containing PDF files'
    )
    parser.add_argument(
        'output',
        help='Output folder for PNG images'
    )
    parser.add_argument(
        '--dpi',
        type=int,
        default=300,
        help='DPI for image conversion (default: 300)'
    )
    
    args = parser.parse_args()
    
    # Check if input is file or folder
    if os.path.isfile(args.input):
        # Convert single file
        pages = pdf_to_png(args.input, args.output, args.dpi)
        print(f"Converted {pages} page(s)")
    elif os.path.isdir(args.input):
        # Convert all PDFs in folder
        batch_convert_pdfs(args.input, args.output, args.dpi)
    else:
        print(f"Error: {args.input} is not a valid file or directory")


if __name__ == '__main__':
    main()
