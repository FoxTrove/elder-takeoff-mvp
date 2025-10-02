#!/usr/bin/env python3
"""
PDF to Image Converter for AI Takeoff MVP

Converts PDF blueprints to PNG images and saves them to a holding area
for review before processing.

Usage:
    python scripts/convert_pdf.py input.pdf
    python scripts/convert_pdf.py input.pdf --pages 1-5
    python scripts/convert_pdf.py --batch pdfs/
"""

import argparse
import sys
from pathlib import Path

try:
    from pdf2image import convert_from_path
    from PIL import Image
except ImportError:
    print("❌ Missing required packages!")
    print("\nPlease install with:")
    print("  pip install pdf2image pillow")
    print("\nOn Mac, you may also need poppler:")
    print("  brew install poppler")
    sys.exit(1)


def convert_pdf_to_images(
    pdf_path: str,
    output_dir: str = "data_holding",
    pages: str = None,
    dpi: int = 300,
    format: str = "PNG"
):
    """
    Convert PDF pages to images.
    
    Args:
        pdf_path: Path to PDF file
        output_dir: Directory to save images (holding area)
        pages: Page range (e.g., "1-5" or "1,3,5")
        dpi: Image resolution (300 is good for blueprints)
        format: Output format (PNG or JPEG)
    """
    pdf_path = Path(pdf_path)
    
    if not pdf_path.exists():
        print(f"❌ PDF not found: {pdf_path}")
        return False
    
    # Create output directory
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    print("="*70)
    print("PDF TO IMAGE CONVERTER")
    print("="*70)
    print(f"\n📄 Input PDF: {pdf_path.name}")
    print(f"📁 Output directory: {output_path}")
    print(f"🎨 Resolution: {dpi} DPI")
    print(f"📐 Format: {format}")
    
    # Parse page range
    first_page = None
    last_page = None
    
    if pages:
        print(f"📋 Pages: {pages}")
        try:
            if '-' in pages:
                first_page, last_page = map(int, pages.split('-'))
            else:
                first_page = last_page = int(pages)
        except ValueError:
            print(f"⚠️  Invalid page range: {pages}")
            print("   Use format like: 1-5 or 3")
            return False
    else:
        print(f"📋 Pages: All")
    
    print("\n🔄 Converting PDF to images...")
    
    try:
        # Convert PDF to images
        images = convert_from_path(
            str(pdf_path),
            dpi=dpi,
            first_page=first_page,
            last_page=last_page,
            fmt=format.lower()
        )
        
        print(f"✅ Extracted {len(images)} page(s)")
        
        # Save images
        saved_files = []
        base_name = pdf_path.stem
        
        for i, image in enumerate(images, start=first_page or 1):
            output_file = output_path / f"{base_name}_page_{i:03d}.png"
            image.save(output_file, format)
            saved_files.append(output_file)
            print(f"   💾 Saved: {output_file.name}")
        
        # Summary
        print("\n" + "="*70)
        print("✅ CONVERSION COMPLETE")
        print("="*70)
        print(f"\n📊 Summary:")
        print(f"   • Pages converted: {len(images)}")
        print(f"   • Files saved: {len(saved_files)}")
        print(f"   • Location: {output_path.absolute()}")
        
        print(f"\n📋 Next Steps:")
        print(f"   1. Review images in: {output_path}/")
        print(f"   2. Select pages you want to process")
        print(f"   3. Move selected images to: data_raw/")
        print(f"   4. Start labeling with: labelImg")
        
        print("\n💡 Quick move command:")
        print(f"   cp {output_path}/{base_name}_page_*.png data_raw/")
        
        return True
        
    except Exception as e:
        print(f"\n❌ Error converting PDF: {e}")
        print("\nTroubleshooting:")
        print("  • Make sure pdf2image is installed: pip install pdf2image")
        print("  • On Mac, install poppler: brew install poppler")
        print("  • On Linux: sudo apt-get install poppler-utils")
        return False


def batch_convert(directory: str, output_dir: str = "data_holding", **kwargs):
    """Convert all PDFs in a directory"""
    dir_path = Path(directory)
    
    if not dir_path.exists():
        print(f"❌ Directory not found: {dir_path}")
        return
    
    pdf_files = list(dir_path.glob("*.pdf"))
    
    if not pdf_files:
        print(f"❌ No PDF files found in: {dir_path}")
        return
    
    print(f"\n📁 Found {len(pdf_files)} PDF file(s)")
    print("="*70)
    
    success_count = 0
    
    for pdf_file in pdf_files:
        print(f"\n🔄 Processing: {pdf_file.name}")
        if convert_pdf_to_images(str(pdf_file), output_dir, **kwargs):
            success_count += 1
    
    print("\n" + "="*70)
    print("BATCH CONVERSION COMPLETE")
    print("="*70)
    print(f"✅ Successfully converted: {success_count}/{len(pdf_files)}")


def main():
    parser = argparse.ArgumentParser(
        description='Convert PDF blueprints to images for AI processing',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Convert entire PDF to holding area
  python scripts/convert_pdf.py blueprint.pdf
  
  # Convert specific pages
  python scripts/convert_pdf.py blueprint.pdf --pages 3-7
  
  # Convert single page
  python scripts/convert_pdf.py blueprint.pdf --pages 5
  
  # Batch convert all PDFs in a folder
  python scripts/convert_pdf.py --batch pdfs/
  
  # High resolution output
  python scripts/convert_pdf.py blueprint.pdf --dpi 600
  
  # Output to custom directory
  python scripts/convert_pdf.py blueprint.pdf --output my_holding_area/
        """
    )
    
    parser.add_argument(
        'pdf_path',
        nargs='?',
        help='Path to PDF file'
    )
    
    parser.add_argument(
        '--batch',
        type=str,
        help='Convert all PDFs in directory'
    )
    
    parser.add_argument(
        '--pages',
        type=str,
        help='Page range to convert (e.g., "1-5" or "3")'
    )
    
    parser.add_argument(
        '--output',
        type=str,
        default='data_holding',
        help='Output directory (default: data_holding)'
    )
    
    parser.add_argument(
        '--dpi',
        type=int,
        default=300,
        help='Image resolution in DPI (default: 300)'
    )
    
    parser.add_argument(
        '--format',
        type=str,
        default='PNG',
        choices=['PNG', 'JPEG'],
        help='Output image format (default: PNG)'
    )
    
    args = parser.parse_args()
    
    # Check if batch mode
    if args.batch:
        batch_convert(
            args.batch,
            output_dir=args.output,
            dpi=args.dpi,
            format=args.format
        )
    elif args.pdf_path:
        convert_pdf_to_images(
            args.pdf_path,
            output_dir=args.output,
            pages=args.pages,
            dpi=args.dpi,
            format=args.format
        )
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == '__main__':
    main()
