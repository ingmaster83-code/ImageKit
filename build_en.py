"""
ImageKit 영어 버전 자동 생성 스크립트
실행: python build_en.py
결과: en/ 폴더에 영어 버전 HTML 파일 생성
"""

import os, re, sys, io, json as _json
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

BASE = os.path.dirname(os.path.abspath(__file__))
EN_DIR = os.path.join(BASE, 'en')
os.makedirs(EN_DIR, exist_ok=True)

# ── 1. 페이지별 메타 번역 ─────────────────────────────────────────────────────
PAGE_META = {
    'compress-image.html': {
        'title': 'Compress Image Free Online – Reduce JPG PNG File Size | WooaImage',
        'desc':  'Compress JPG and PNG images for free. Adjust quality with a slider, compare original vs compressed size. 100% browser-based, never uploaded.',
        'kw':    'compress image, reduce image size, JPG compressor, PNG compressor, image file size reducer, compress image free online',
        'og_title': 'Compress Image Free – Reduce File Size Online | WooaImage',
        'og_desc':  'Reduce JPG/PNG image file size with a quality slider. Free, no signup. Files never leave your browser.',
        'app_name': 'Image Compressor',
        'faq': [
            ('Will compressing reduce image quality?',
             'You can adjust the compression level. At moderate settings, the difference is barely visible to the naked eye.'),
            ('What formats are supported?',
             'JPG, PNG, and WebP are all supported.'),
            ('Are compressed images stored on a server?',
             'No. All processing happens locally in your browser and nothing is ever sent externally.'),
        ],
        'h1': 'Compress Image – Free Online',
        'tool_desc': 'Upload a JPG or PNG to reduce file size. Adjust quality with the slider and compare before/after size. Everything runs in your browser.',
        'breadcrumb': 'Compress Image',
        'cross_banner_text': 'Want to compress a PDF file too?',
        'cross_banner_link_text': '📄 WooaPDF – Compress PDF →',
        'cross_banner_href': 'https://pdfkit.wooahouse.com/compress-pdf.html',
    },
    'resize-image.html': {
        'title': 'Resize Image Free Online – Change Image Size by Pixel or Percent | WooaImage',
        'desc':  'Resize images by pixel or percentage for free. Lock aspect ratio, upscale or downscale. Browser-based — files never uploaded to a server.',
        'kw':    'resize image, change image size, image resizer online free, resize photo pixels, scale image online',
        'og_title': 'Resize Image Free – Pixel or Percent | WooaImage',
        'og_desc':  'Resize images by entering width/height in pixels or percentage. Lock aspect ratio. Free, no upload.',
        'app_name': 'Image Resizer',
        'faq': [
            ('Can I resize while keeping the original aspect ratio?',
             'Yes. Enable the lock ratio option and entering width or height will automatically calculate the other dimension.'),
            ('Can I upscale images?',
             'Yes, but upscaling beyond the original resolution may reduce image quality.'),
            ('Are both pixels and percentage units supported?',
             'Yes. You can specify size in pixels (px) or percentage (%).'),
        ],
        'h1': 'Resize Image – Free Online',
        'tool_desc': 'Upload an image and resize it by entering width/height in pixels or a percentage. Lock aspect ratio for proportional scaling. All done in your browser.',
        'breadcrumb': 'Resize Image',
        'cross_banner_text': 'Need to crop a specific area of your image?',
        'cross_banner_link_text': '✂️ Crop Image →',
        'cross_banner_href': '../crop-image.html',
    },
    'rotate-image.html': {
        'title': 'Rotate & Flip Image Free Online – 90° 180° 270° Rotation | WooaImage',
        'desc':  'Rotate images 90°, 180°, 270° or flip horizontally/vertically for free. Browser-based image rotation — no upload required.',
        'kw':    'rotate image, flip image, rotate photo online free, horizontal flip, vertical flip, image rotation tool',
        'og_title': 'Rotate & Flip Image Free Online | WooaImage',
        'og_desc':  'Rotate images 90°/180°/270°, flip left-right or top-bottom. Free, no signup, no server upload.',
        'app_name': 'Image Rotate & Flip Tool',
        'faq': [
            ('What rotation angles are available?',
             '90°, 180°, and 270° rotations are supported, as well as horizontal and vertical flipping.'),
            ('Can I flip an image without rotating it?',
             'Yes. Use the horizontal flip (mirror) or vertical flip buttons independently.'),
            ('Are files sent to a server?',
             'No. All processing is done locally in your browser. Your files never leave your device.'),
        ],
        'h1': 'Rotate & Flip Image – Free Online',
        'tool_desc': 'Upload an image and rotate it 90°, 180°, or 270°, or flip it horizontally/vertically. All processing happens in your browser.',
        'breadcrumb': 'Rotate / Flip',
        'cross_banner_text': 'Need to resize your image after rotating?',
        'cross_banner_link_text': '📐 Resize Image →',
        'cross_banner_href': '../resize-image.html',
    },
    'crop-image.html': {
        'title': 'Crop Image Free Online – Image Cropper with Pixel Precision | WooaImage',
        'desc':  'Crop images to any area for free. Enter X/Y coordinates and width/height for precise cropping or drag to select. 100% browser-based.',
        'kw':    'crop image, image cropper online free, crop photo pixels, crop image online, image cut tool',
        'og_title': 'Crop Image Free – Precise Online Cropper | WooaImage',
        'og_desc':  'Crop images by entering coordinates or dragging to select an area. Precise pixel cropping. Free, no server upload.',
        'app_name': 'Image Cropper',
        'faq': [
            ('Can I crop with exact pixel precision?',
             'Yes. Enter X/Y coordinates and width/height directly, or drag to select the crop area.'),
            ('Can I crop to a specific aspect ratio (16:9, 1:1)?',
             'Yes. Enable the lock ratio option to crop at a fixed aspect ratio.'),
            ('What format will the cropped image be?',
             'The original format is preserved and downloaded as JPG or PNG.'),
        ],
        'h1': 'Crop Image – Free Online',
        'tool_desc': 'Upload an image and crop it by specifying coordinates or dragging to select an area. Supports fixed aspect ratios. All done in your browser.',
        'breadcrumb': 'Crop Image',
        'cross_banner_text': 'Need to resize the image after cropping?',
        'cross_banner_link_text': '📐 Resize Image →',
        'cross_banner_href': '../resize-image.html',
    },
    'jpg-to-png.html': {
        'title': 'JPG to PNG Converter Free Online – Convert JPEG to PNG | WooaImage',
        'desc':  'Convert JPG/JPEG images to transparent-background PNG for free. No signup. All conversion happens in your browser — no server upload.',
        'kw':    'JPG to PNG, JPEG to PNG, convert JPG to PNG free, jpg png converter online, transparent PNG',
        'og_title': 'JPG to PNG Converter Free Online | WooaImage',
        'og_desc':  'Convert JPG to PNG with transparent background support. Free, no signup, no upload.',
        'app_name': 'JPG to PNG Converter',
        'faq': [
            ('Will the converted PNG support transparency?',
             'Yes. PNG format supports transparent backgrounds, which is preserved during conversion.'),
            ('Is there any quality loss when converting JPG to PNG?',
             'PNG is a lossless format, so there is no additional quality loss during conversion.'),
            ('Are my files sent to a server?',
             'No. All processing runs entirely in your browser.'),
        ],
        'h1': 'JPG to PNG Converter – Free Online',
        'tool_desc': 'Upload a JPG or JPEG image and convert it to PNG format. Transparent background is supported. All processing happens in your browser.',
        'breadcrumb': 'JPG → PNG',
        'cross_banner_text': 'Need to convert PNG back to JPG?',
        'cross_banner_link_text': '🔄 PNG to JPG →',
        'cross_banner_href': '../png-to-jpg.html',
    },
    'png-to-jpg.html': {
        'title': 'PNG to JPG Converter Free Online – Convert PNG to JPEG | WooaImage',
        'desc':  'Convert PNG images to JPG/JPEG format for free. Reduce file size while maintaining quality. Browser-based — files never leave your device.',
        'kw':    'PNG to JPG, PNG to JPEG, convert PNG to JPG free, png jpg converter online, image format converter',
        'og_title': 'PNG to JPG Converter Free Online | WooaImage',
        'og_desc':  'Convert PNG to JPG/JPEG instantly. Reduce file size. Free, no signup, no server upload.',
        'app_name': 'PNG to JPG Converter',
        'faq': [
            ('Will transparent areas become white when converting PNG to JPG?',
             'Yes. Since JPG does not support transparency, transparent areas will be filled with white.'),
            ('Can I adjust the quality when converting to JPG?',
             'Yes. You can set the JPEG quality level to control output file size.'),
            ('Are files sent to a server?',
             'No. All processing is done locally in your browser.'),
        ],
        'h1': 'PNG to JPG Converter – Free Online',
        'tool_desc': 'Upload a PNG image and convert it to JPG/JPEG format. Smaller file size for easy sharing. All processing happens in your browser.',
        'breadcrumb': 'PNG → JPG',
        'cross_banner_text': 'Need to convert JPG back to PNG?',
        'cross_banner_link_text': '🔄 JPG to PNG →',
        'cross_banner_href': '../jpg-to-png.html',
    },
    'image-to-webp.html': {
        'title': 'Image to WebP Converter Free Online – JPG PNG to WebP | WooaImage',
        'desc':  'Convert JPG and PNG images to WebP format for free. Reduce file size by 30%+ while maintaining quality. Browser-based, no server upload.',
        'kw':    'image to WebP, JPG to WebP, PNG to WebP, convert image to WebP free, WebP converter online, web image optimization',
        'og_title': 'Image to WebP Converter Free Online | WooaImage',
        'og_desc':  'Convert JPG/PNG to WebP and reduce file size by 30%+. Free, no signup, no server upload.',
        'app_name': 'Image to WebP Converter',
        'faq': [
            ('What are the advantages of WebP format?',
             'WebP is 30%+ smaller than JPG/PNG while maintaining quality, making it ideal for web optimization.'),
            ('Is WebP supported in all browsers?',
             'Yes. All modern browsers (Chrome, Firefox, Safari, Edge) support WebP.'),
            ('Is transparency (alpha channel) preserved?',
             'Yes. PNG transparency is preserved when converting to WebP.'),
        ],
        'h1': 'Image to WebP Converter – Free Online',
        'tool_desc': 'Upload a JPG or PNG image and convert it to WebP format. Significantly smaller file size for web use. Quality slider included. All browser-based.',
        'breadcrumb': 'Image → WebP',
        'cross_banner_text': 'Need to convert WebP back to JPG?',
        'cross_banner_link_text': '🔄 WebP to JPG →',
        'cross_banner_href': '../webp-to-jpg.html',
    },
    'webp-to-jpg.html': {
        'title': 'WebP to JPG Converter Free Online – Convert WebP to JPEG | WooaImage',
        'desc':  'Convert WebP images to JPG/PNG format for free. Easy compatibility fix for apps that do not support WebP. 100% browser-based.',
        'kw':    'WebP to JPG, WebP to JPEG, WebP to PNG, convert WebP free, WebP image converter online',
        'og_title': 'WebP to JPG Converter Free Online | WooaImage',
        'og_desc':  'Convert WebP images to JPG or PNG instantly. Free, no signup, no server upload.',
        'app_name': 'WebP to JPG Converter',
        'faq': [
            ('Why do I need to convert WebP to JPG?',
             'Some older apps and platforms do not support WebP. Converting to JPG ensures wider compatibility.'),
            ('Can I choose between JPG and PNG output?',
             'Yes. You can select the output format as JPG or PNG.'),
            ('Are files uploaded to a server?',
             'No. All processing is done locally in your browser.'),
        ],
        'h1': 'WebP to JPG Converter – Free Online',
        'tool_desc': 'Upload a WebP image and convert it to JPG or PNG format. Useful for apps that do not support WebP. All processing happens in your browser.',
        'breadcrumb': 'WebP → JPG',
        'cross_banner_text': 'Need to convert JPG or PNG to WebP?',
        'cross_banner_link_text': '🔄 Image to WebP →',
        'cross_banner_href': '../image-to-webp.html',
    },
    'watermark-image.html': {
        'title': 'Add Watermark to Image Free Online – Text Watermark | WooaImage',
        'desc':  'Add a custom text watermark to images for free. Adjust font, size, color, opacity, and position. Browser-based — files never uploaded.',
        'kw':    'watermark image, add watermark to photo, image watermark online free, text watermark tool, stamp image',
        'og_title': 'Add Watermark to Image Free Online | WooaImage',
        'og_desc':  'Add custom text watermarks to images. Set font, color, opacity, and position. Free, no server upload.',
        'app_name': 'Image Watermark Tool',
        'faq': [
            ('Can I customize the watermark appearance?',
             'Yes. You can set the text, font size, color, opacity, angle, and position of the watermark.'),
            ('Can I apply the watermark to a specific position?',
             'Yes. You can choose from corner positions, center, or diagonal placement.'),
            ('Are my images stored on a server?',
             'No. All processing happens locally in your browser. Nothing is ever uploaded.'),
        ],
        'h1': 'Add Watermark to Image – Free Online',
        'tool_desc': 'Upload an image and add a custom text watermark. Set font, size, color, opacity, and position. Everything runs in your browser.',
        'breadcrumb': 'Watermark Image',
        'cross_banner_text': 'Need to add a watermark to a PDF?',
        'cross_banner_link_text': '📄 WooaPDF – Watermark PDF →',
        'cross_banner_href': 'https://pdfkit.wooahouse.com/watermark-pdf.html',
    },
    'image-to-base64.html': {
        'title': 'Image to Base64 Converter Free Online – Encode Image as Base64 | WooaImage',
        'desc':  'Convert images to Base64 encoded strings for free. Copy Base64 data or download as text file. Browser-based — files never uploaded to a server.',
        'kw':    'image to base64, base64 encode image, image base64 converter online, convert image base64 free, JPG base64 PNG base64',
        'og_title': 'Image to Base64 Converter Free Online | WooaImage',
        'og_desc':  'Encode any image as a Base64 string. Copy or download the result. Free, no server upload.',
        'app_name': 'Image to Base64 Converter',
        'faq': [
            ('What is Base64 encoding used for?',
             'Base64 encodes binary image data as text, useful for embedding images directly in HTML, CSS, or JSON.'),
            ('Which image formats are supported?',
             'JPG, PNG, WebP, GIF, and BMP are all supported.'),
            ('Are files sent to a server?',
             'No. The entire encoding process runs in your browser.'),
        ],
        'h1': 'Image to Base64 Converter – Free Online',
        'tool_desc': 'Upload an image to convert it to a Base64 encoded string. Copy to clipboard or download as a text file. All processing done in your browser.',
        'breadcrumb': 'Image → Base64',
        'cross_banner_text': 'Need to compress your images before encoding?',
        'cross_banner_link_text': '🗜️ Compress Image →',
        'cross_banner_href': '../compress-image.html',
    },
    'image-info.html': {
        'title': 'Image Info Viewer Free Online – Check Image Size Resolution Format | WooaImage',
        'desc':  'Check image resolution, file size, format, color depth, and more for free. No upload required — all analysis done in your browser.',
        'kw':    'image info, check image resolution, image file size checker, image metadata viewer, photo info online free',
        'og_title': 'Image Info Viewer – Check Image Details Free | WooaImage',
        'og_desc':  'View image resolution, file size, format, and color depth instantly. Free, no server upload.',
        'app_name': 'Image Info Viewer',
        'faq': [
            ('What information can I see about my image?',
             'You can see file name, format, resolution (width × height), file size, color depth, and more.'),
            ('Can I view EXIF metadata?',
             'Basic EXIF data such as camera model, shooting date, and GPS info is displayed if available.'),
            ('Is my image uploaded to a server?',
             'No. All analysis happens locally in your browser.'),
        ],
        'h1': 'Image Info Viewer – Free Online',
        'tool_desc': 'Upload an image to instantly check its resolution, file size, format, and metadata. No server upload — all analysis runs in your browser.',
        'breadcrumb': 'Image Info',
        'cross_banner_text': 'Need to compress or resize your image?',
        'cross_banner_link_text': '🗜️ Compress Image →',
        'cross_banner_href': '../compress-image.html',
    },
    'bg-remove.html': {
        'title': 'Remove Image Background Free Online – AI Background Remover | WooaImage',
        'desc':  'Remove image backgrounds for free using AI. Accurately detects people and objects and saves as transparent PNG. Browser-based, no signup.',
        'kw':    'remove background, background remover, remove image background free, transparent PNG, AI background remove online',
        'og_title': 'Remove Image Background Free – AI Online Tool | WooaImage',
        'og_desc':  'AI-powered background removal. Saves as transparent PNG. Free, no signup, no server upload.',
        'app_name': 'AI Background Remover',
        'faq': [
            ('What types of images work best for background removal?',
             'Images with clear subjects (people, products) against simple backgrounds give the best results.'),
            ('What format is the output after background removal?',
             'The result is saved as a transparent PNG file.'),
            ('Why is it slow on the first use?',
             'The first use downloads the AI model (~50MB). Subsequent uses are much faster as the model is cached.'),
        ],
        'h1': 'Remove Image Background – Free Online AI Tool',
        'tool_desc': 'Upload an image and the AI will automatically remove the background. Save as transparent PNG. The AI model runs in your browser — no server upload.',
        'breadcrumb': 'Background Remover',
        'cross_banner_text': 'Need to add a watermark after removing the background?',
        'cross_banner_link_text': '💧 Add Watermark →',
        'cross_banner_href': '../watermark-image.html',
    },
    'heic-to-jpg.html': {
        'title': 'HEIC to JPG Converter Free Online – Convert iPhone Photos | WooaImage',
        'desc':  'Convert HEIC/HEIF images from iPhone to JPG for free. Batch conversion supported, download all as ZIP. Browser-based, no server upload.',
        'kw':    'HEIC to JPG, HEIF to JPG, convert HEIC free, iPhone photo converter, HEIC converter online',
        'og_title': 'HEIC to JPG Converter Free Online | WooaImage',
        'og_desc':  'Convert iPhone HEIC photos to JPG instantly. Batch convert and download as ZIP. Free, no server upload.',
        'app_name': 'HEIC to JPG Converter',
        'faq': [
            ('What is HEIC format?',
             'HEIC (High Efficiency Image Container) is the default photo format on iPhones. It is smaller than JPG but not widely supported.'),
            ('Can I convert multiple HEIC files at once?',
             'Yes. Multiple HEIC files can be selected and downloaded together as a ZIP archive.'),
            ('Are files sent to a server?',
             'No. All conversion runs locally in your browser.'),
        ],
        'h1': 'HEIC to JPG Converter – Free Online',
        'tool_desc': 'Upload iPhone HEIC photos and convert them to JPG format. Batch conversion supported — download all as ZIP. Everything runs in your browser.',
        'breadcrumb': 'HEIC → JPG',
        'cross_banner_text': 'Need to compress the converted JPG files?',
        'cross_banner_link_text': '🗜️ Compress Image →',
        'cross_banner_href': '../compress-image.html',
    },
    'make-gif.html': {
        'title': 'Make GIF Free Online – Create Animated GIF from Images | WooaImage',
        'desc':  'Create animated GIFs from multiple images for free. Set frame rate and loop count. Browser-based GIF maker — no signup, no server upload.',
        'kw':    'make GIF, create animated GIF, GIF maker online free, images to GIF, animated GIF creator',
        'og_title': 'Make Animated GIF Free Online | WooaImage',
        'og_desc':  'Create animated GIFs from multiple images. Set frame rate and loops. Free, no signup, no server.',
        'app_name': 'GIF Maker',
        'faq': [
            ('What image formats can I use to make a GIF?',
             'JPG, PNG, and WebP images are all supported for creating GIFs.'),
            ('Can I control the animation speed?',
             'Yes. You can set the frame interval (delay between frames) to control the speed.'),
            ('Is there a limit on the number of frames?',
             'No strict limit, but too many frames may result in a large GIF file size.'),
        ],
        'h1': 'GIF Maker – Create Animated GIF Free Online',
        'tool_desc': 'Upload multiple images and combine them into an animated GIF. Set frame rate and loop count. All processing happens in your browser.',
        'breadcrumb': 'Make GIF',
        'cross_banner_text': 'Need to resize images before making a GIF?',
        'cross_banner_link_text': '📐 Resize Image →',
        'cross_banner_href': '../resize-image.html',
    },
    'upscale-image.html': {
        'title': 'Upscale Image Free Online – Increase Image Resolution | WooaImage',
        'desc':  'Upscale and enlarge images for free. Improve resolution using interpolation. Browser-based image upscaler — no server upload required.',
        'kw':    'upscale image, increase image resolution, image upscaler online free, enlarge image, super resolution online',
        'og_title': 'Upscale Image Free – Increase Resolution Online | WooaImage',
        'og_desc':  'Enlarge and upscale images with improved quality. Free, no signup, browser-based.',
        'app_name': 'Image Upscaler',
        'faq': [
            ('How much can I upscale an image?',
             'You can upscale to 2x or 4x the original size. Higher upscaling may show some quality reduction.'),
            ('What interpolation method is used?',
             'The tool uses bicubic interpolation for smooth, high-quality upscaling results.'),
            ('Are files sent to a server?',
             'No. All upscaling runs locally in your browser using the Canvas API.'),
        ],
        'h1': 'Upscale Image – Free Online',
        'tool_desc': 'Upload an image and enlarge it to 2x or 4x resolution. Uses bicubic interpolation for smooth results. All processing done in your browser.',
        'breadcrumb': 'Upscale Image',
        'cross_banner_text': 'Need to resize your image to a specific size?',
        'cross_banner_link_text': '📐 Resize Image →',
        'cross_banner_href': '../resize-image.html',
    },
    'ocr-image.html': {
        'title': 'Image OCR Free Online – Extract Text from Image | WooaImage',
        'desc':  'Extract text from images for free using OCR. Supports Korean and English. Copy or download extracted text. 100% browser-based with Tesseract.js.',
        'kw':    'image OCR, extract text from image, image to text free, OCR online, Tesseract OCR, photo text extractor',
        'og_title': 'Image OCR Free – Extract Text from Image Online | WooaImage',
        'og_desc':  'Extract text from images using OCR. Supports Korean & English. Free, no signup, no server upload.',
        'app_name': 'Image OCR Tool',
        'faq': [
            ('What languages are supported for OCR?',
             'Korean and English are both supported. The tool uses Tesseract.js for text recognition.'),
            ('Does OCR work on handwritten text?',
             'OCR works best on clear printed text. Handwritten or stylized fonts may have lower accuracy.'),
            ('Are images sent to a server for OCR processing?',
             'No. All OCR processing runs locally in your browser using Tesseract.js.'),
        ],
        'h1': 'Image OCR – Extract Text Free Online',
        'tool_desc': 'Upload an image to extract text using OCR. Supports Korean and English. Copy or download the result. Powered by Tesseract.js — fully browser-based.',
        'breadcrumb': 'Image OCR',
        'cross_banner_text': 'Need to extract text from a scanned PDF?',
        'cross_banner_link_text': '📄 PDF OCR →',
        'cross_banner_href': '../ocr-pdf.html',
    },
    'ocr-pdf.html': {
        'title': 'PDF OCR Free Online – Extract Text from Scanned PDF | WooaImage',
        'desc':  'Extract text from scanned PDF files using OCR for free. Supports Korean and English. Browser-based with PDF.js and Tesseract.js — no server upload.',
        'kw':    'PDF OCR, extract text from scanned PDF, PDF text extractor OCR, scanned PDF to text, OCR PDF online free',
        'og_title': 'PDF OCR Free – Extract Text from Scanned PDF | WooaImage',
        'og_desc':  'OCR scanned PDFs to extract text. Supports Korean & English. Free, no signup, no server upload.',
        'app_name': 'PDF OCR Tool',
        'faq': [
            ('What types of PDFs does this work on?',
             'This tool is designed for scanned image PDFs where text cannot be copied. For text-based PDFs, use a regular text extractor.'),
            ('What languages are supported?',
             'Korean and English OCR are both supported.'),
            ('Are PDF files uploaded to a server?',
             'No. PDFs are rendered in the browser with PDF.js and OCR runs locally via Tesseract.js.'),
        ],
        'h1': 'PDF OCR – Extract Text from Scanned PDF Free',
        'tool_desc': 'Upload a scanned PDF to extract text using OCR. Supports Korean and English. Powered by PDF.js + Tesseract.js — entirely browser-based.',
        'breadcrumb': 'PDF OCR',
        'cross_banner_text': 'Need to extract text from an image instead?',
        'cross_banner_link_text': '🖼️ Image OCR →',
        'cross_banner_href': '../ocr-image.html',
    },
    'add-text-image.html': {
        'title': 'Add Text to Image Free Online – Write on Photo | WooaImage',
        'desc':  'Add custom text to images for free. Choose font, size, color, and position. Browser-based image text overlay — no server upload needed.',
        'kw':    'add text to image, write on photo, image text overlay free, add caption to photo, text on image online',
        'og_title': 'Add Text to Image Free Online | WooaImage',
        'og_desc':  'Write custom text on any image. Set font, size, color, and position. Free, no signup, no server.',
        'app_name': 'Image Text Tool',
        'faq': [
            ('Can I change the font and color of the text?',
             'Yes. You can customize font style, size, color, and opacity.'),
            ('Can I position the text anywhere on the image?',
             'Yes. You can freely position text anywhere on the image by dragging or entering coordinates.'),
            ('Are images uploaded to a server?',
             'No. All processing happens entirely in your browser.'),
        ],
        'h1': 'Add Text to Image – Free Online',
        'tool_desc': 'Upload an image and overlay custom text. Adjust font, size, color, and position. All processing runs in your browser — no server upload.',
        'breadcrumb': 'Add Text to Image',
        'cross_banner_text': 'Need to add a watermark instead?',
        'cross_banner_link_text': '💧 Add Watermark →',
        'cross_banner_href': '../watermark-image.html',
    },
    'image-filter.html': {
        'title': 'Image Filter Free Online – Apply Photo Filters & Effects | WooaImage',
        'desc':  'Apply filters and effects to images for free. Grayscale, sepia, brightness, contrast, blur and more. 100% browser-based — no server upload.',
        'kw':    'image filter online, photo filter free, apply image effects, grayscale image, sepia filter, brightness contrast tool',
        'og_title': 'Image Filter Free – Apply Photo Effects Online | WooaImage',
        'og_desc':  'Apply grayscale, sepia, brightness, contrast, and blur filters to images. Free, no signup.',
        'app_name': 'Image Filter Tool',
        'faq': [
            ('What filters are available?',
             'Grayscale, sepia, invert, brightness, contrast, saturation, blur, and more are available.'),
            ('Can I adjust the intensity of the filters?',
             'Yes. Most filters have a slider to control the strength of the effect.'),
            ('Are files sent to a server?',
             'No. All filter processing runs locally in your browser.'),
        ],
        'h1': 'Image Filter – Apply Photo Effects Free Online',
        'tool_desc': 'Upload an image and apply filters like grayscale, sepia, brightness, contrast, and blur. Adjust intensity with sliders. Everything runs in your browser.',
        'breadcrumb': 'Image Filter',
        'cross_banner_text': 'Need to compress the image after applying filters?',
        'cross_banner_link_text': '🗜️ Compress Image →',
        'cross_banner_href': '../compress-image.html',
    },
    'mosaic-image.html': {
        'title': 'Mosaic Image Free Online – Pixelate & Blur Part of Photo | WooaImage',
        'desc':  'Apply mosaic or pixelation effect to part of an image for free. Great for hiding faces or sensitive info. Browser-based — no server upload.',
        'kw':    'mosaic image, pixelate image, blur part of photo, image mosaic online free, censor image, hide face in photo',
        'og_title': 'Mosaic & Pixelate Image Free Online | WooaImage',
        'og_desc':  'Apply mosaic effect to hide faces or sensitive areas in images. Free, no signup, no server.',
        'app_name': 'Image Mosaic Tool',
        'faq': [
            ('Can I apply mosaic to only a specific area?',
             'Yes. Draw a selection box over the area you want to mosaic and apply the effect.'),
            ('Can I adjust the mosaic block size?',
             'Yes. You can control the pixel block size to make the mosaic more or less obvious.'),
            ('Are images uploaded to a server?',
             'No. All processing happens locally in your browser.'),
        ],
        'h1': 'Mosaic & Pixelate Image – Free Online',
        'tool_desc': 'Upload an image and apply a mosaic/pixelation effect to any area. Select the region and adjust block size. All done in your browser.',
        'breadcrumb': 'Mosaic Image',
        'cross_banner_text': 'Need to blur the entire image instead?',
        'cross_banner_link_text': '🎨 Image Filter →',
        'cross_banner_href': '../image-filter.html',
    },
    'merge-image.html': {
        'title': 'Merge Images Free Online – Combine Multiple Images | WooaImage',
        'desc':  'Merge multiple images into one for free. Stack vertically, horizontally, or create a grid layout. Browser-based — no server upload.',
        'kw':    'merge images, combine images online free, stitch images together, image merger, join photos side by side',
        'og_title': 'Merge Images Free – Combine Multiple Photos Online | WooaImage',
        'og_desc':  'Combine multiple images vertically, horizontally, or in a grid. Free, no signup, no server.',
        'app_name': 'Image Merger',
        'faq': [
            ('What layout options are available for merging?',
             'You can merge images vertically (top to bottom), horizontally (side by side), or in a grid layout.'),
            ('How many images can I merge at once?',
             'There is no strict limit on the number of images you can merge.'),
            ('Are files uploaded to a server?',
             'No. All processing runs locally in your browser.'),
        ],
        'h1': 'Merge Images – Combine Photos Free Online',
        'tool_desc': 'Upload multiple images and merge them into one. Choose vertical, horizontal, or grid layout. All processing happens in your browser.',
        'breadcrumb': 'Merge Images',
        'cross_banner_text': 'Need to resize images before merging?',
        'cross_banner_link_text': '📐 Resize Image →',
        'cross_banner_href': '../resize-image.html',
    },
    'round-corner.html': {
        'title': 'Round Image Corners Free Online – Add Rounded Corners to Photo | WooaImage',
        'desc':  'Add rounded corners to images for free. Customize border radius and save as PNG with transparent corners. 100% browser-based.',
        'kw':    'round image corners, rounded corners image, circle image online free, border radius image, rounded photo edges',
        'og_title': 'Round Image Corners Free Online | WooaImage',
        'og_desc':  'Add customizable rounded corners to images. Save as transparent PNG. Free, no server upload.',
        'app_name': 'Image Round Corner Tool',
        'faq': [
            ('Can I control how rounded the corners are?',
             'Yes. You can set the border radius value to control how rounded the corners appear.'),
            ('Will the rounded corners be transparent?',
             'Yes. The corners are saved as transparent PNG so they blend naturally with any background.'),
            ('Are my images sent to a server?',
             'No. All processing happens locally in your browser.'),
        ],
        'h1': 'Round Image Corners – Free Online',
        'tool_desc': 'Upload an image and add rounded corners with customizable radius. Transparent corners are saved as PNG. All done in your browser.',
        'breadcrumb': 'Round Corners',
        'cross_banner_text': 'Need to add a border to your image?',
        'cross_banner_link_text': '🖼️ Add Border →',
        'cross_banner_href': '../image-border.html',
    },
    'split-image.html': {
        'title': 'Split Image Free Online – Cut Image into Equal Parts | WooaImage',
        'desc':  'Split an image into equal pieces or custom grid for free. Download all parts as ZIP. Browser-based — no server upload required.',
        'kw':    'split image, cut image into pieces, image splitter online free, divide image grid, slice image',
        'og_title': 'Split Image Free – Cut Photo into Parts Online | WooaImage',
        'og_desc':  'Split images into equal parts or custom grid. Download as ZIP. Free, no signup, no server upload.',
        'app_name': 'Image Splitter',
        'faq': [
            ('Can I split an image into a custom grid?',
             'Yes. You can specify the number of rows and columns to create a custom grid split.'),
            ('How are the split parts downloaded?',
             'All split image parts are packaged and downloaded as a single ZIP file.'),
            ('Are files uploaded to a server?',
             'No. All processing runs locally in your browser.'),
        ],
        'h1': 'Split Image – Cut into Parts Free Online',
        'tool_desc': 'Upload an image and split it into equal parts by specifying rows and columns. Download all pieces as a ZIP file. All done in your browser.',
        'breadcrumb': 'Split Image',
        'cross_banner_text': 'Need to merge images instead?',
        'cross_banner_link_text': '🔗 Merge Images →',
        'cross_banner_href': '../merge-image.html',
    },
    'png-to-ico.html': {
        'title': 'PNG to ICO Converter Free Online – Create Favicon from PNG | WooaImage',
        'desc':  'Convert PNG images to ICO format for free. Create favicons and app icons in multiple sizes (16x16 to 256x256). Browser-based, no upload.',
        'kw':    'PNG to ICO, create favicon, favicon generator, PNG to icon, ICO converter online free',
        'og_title': 'PNG to ICO Converter Free – Create Favicon Online | WooaImage',
        'og_desc':  'Convert PNG to ICO favicon. Multiple icon sizes supported. Free, no signup, no server upload.',
        'app_name': 'PNG to ICO Converter',
        'faq': [
            ('What ICO sizes are generated?',
             'Common sizes like 16x16, 32x32, 48x48, and 256x256 are generated for maximum compatibility.'),
            ('Can I use the resulting ICO as a website favicon?',
             'Yes. The generated ICO file can be used directly as a website favicon.'),
            ('Are files uploaded to a server?',
             'No. All conversion runs locally in your browser.'),
        ],
        'h1': 'PNG to ICO Converter – Create Favicon Free Online',
        'tool_desc': 'Upload a PNG image and convert it to ICO format for use as a favicon or app icon. Multiple sizes included. All processing done in your browser.',
        'breadcrumb': 'PNG → ICO',
        'cross_banner_text': 'Need to convert ICO back to PNG?',
        'cross_banner_link_text': '🖼️ Back to PNG →',
        'cross_banner_href': '../jpg-to-png.html',
    },
    'exif-remove.html': {
        'title': 'Remove EXIF Data Free Online – Strip Image Metadata | WooaImage',
        'desc':  'Remove EXIF metadata from images for free. Strip GPS location, camera info, and other sensitive data. Browser-based — no server upload.',
        'kw':    'remove EXIF data, strip image metadata, EXIF remover online free, remove GPS from photo, image privacy tool',
        'og_title': 'Remove EXIF Data Free – Strip Image Metadata | WooaImage',
        'og_desc':  'Remove GPS, camera info, and other EXIF data from images. Free, no signup, no server upload.',
        'app_name': 'EXIF Data Remover',
        'faq': [
            ('What metadata does this tool remove?',
             'GPS coordinates, camera model, shooting date, settings, and all other EXIF data are removed.'),
            ('Why would I want to remove EXIF data?',
             'EXIF data can contain your location (GPS) and other private information. Removing it protects your privacy when sharing images.'),
            ('Are files uploaded to a server?',
             'No. All EXIF stripping runs locally in your browser.'),
        ],
        'h1': 'Remove EXIF Data – Strip Image Metadata Free Online',
        'tool_desc': 'Upload an image to remove all EXIF metadata including GPS location and camera info. Protect your privacy before sharing. All done in your browser.',
        'breadcrumb': 'Remove EXIF',
        'cross_banner_text': 'Want to view the EXIF data first before removing?',
        'cross_banner_link_text': '📊 Image Info →',
        'cross_banner_href': '../image-info.html',
    },
    'collage-image.html': {
        'title': 'Photo Collage Maker Free Online – Create Image Collage | WooaImage',
        'desc':  'Create a photo collage from multiple images for free. Choose from various layouts and download as one image. 100% browser-based.',
        'kw':    'photo collage maker, image collage online free, create photo collage, collage maker, picture collage tool',
        'og_title': 'Photo Collage Maker Free Online | WooaImage',
        'og_desc':  'Create a photo collage from multiple images. Choose layout and download. Free, no signup, no server.',
        'app_name': 'Photo Collage Maker',
        'faq': [
            ('What collage layouts are available?',
             'Various grid and mosaic layouts are available. Choose the layout that best fits your images.'),
            ('How many images can I use in a collage?',
             'You can typically use 2 to 9 images depending on the layout.'),
            ('Are images uploaded to a server?',
             'No. All collage creation happens locally in your browser.'),
        ],
        'h1': 'Photo Collage Maker – Free Online',
        'tool_desc': 'Upload multiple images and arrange them into a collage. Choose from various layouts and download as a single image. All done in your browser.',
        'breadcrumb': 'Photo Collage',
        'cross_banner_text': 'Need to merge images in a simpler way?',
        'cross_banner_link_text': '🔗 Merge Images →',
        'cross_banner_href': '../merge-image.html',
    },
    'image-border.html': {
        'title': 'Add Border to Image Free Online – Photo Frame Effect | WooaImage',
        'desc':  'Add a custom border or frame to images for free. Choose color, size, and style. Browser-based image border tool — no server upload.',
        'kw':    'add border to image, image border online free, photo frame effect, picture border tool, image frame maker',
        'og_title': 'Add Border to Image Free Online | WooaImage',
        'og_desc':  'Add custom color borders to images. Set size and style. Free, no signup, no server upload.',
        'app_name': 'Image Border Tool',
        'faq': [
            ('Will the image size change after adding a border?',
             'Yes. The border is added around the image, so the total dimensions will increase by the border width.'),
            ('Can I add a border to a PNG with transparent background?',
             'Yes. Transparent PNG images are supported and the border is applied correctly.'),
            ('Are files sent to a server?',
             'No. All processing happens locally in your browser.'),
        ],
        'h1': 'Add Border to Image – Free Online',
        'tool_desc': 'Upload an image and add a custom border. Choose color, width, and style. The image is processed entirely in your browser — no server upload.',
        'breadcrumb': 'Image Border',
        'cross_banner_text': 'Need to add rounded corners instead?',
        'cross_banner_link_text': '⭕ Round Corners →',
        'cross_banner_href': '../round-corner.html',
    },
    'svg-to-png.html': {
        'title': 'SVG to PNG Converter Free Online – Convert SVG to PNG | WooaImage',
        'desc':  'Convert SVG vector images to PNG format for free. Set output size and get a pixel-perfect result. Browser-based — no server upload required.',
        'kw':    'SVG to PNG, convert SVG to PNG free, SVG converter online, vector to PNG, SVG PNG export',
        'og_title': 'SVG to PNG Converter Free Online | WooaImage',
        'og_desc':  'Convert SVG files to PNG. Set output size. Free, no signup, no server upload.',
        'app_name': 'SVG to PNG Converter',
        'faq': [
            ('What size PNG will be generated?',
             'You can specify the output width and height. The SVG is rendered at that resolution.'),
            ('Will the SVG quality be preserved?',
             'Yes. SVG is a vector format and scales without quality loss to any size.'),
            ('Are files uploaded to a server?',
             'No. All conversion runs locally in your browser.'),
        ],
        'h1': 'SVG to PNG Converter – Free Online',
        'tool_desc': 'Upload an SVG file and convert it to PNG. Set the output dimensions and download the result. All processing happens in your browser.',
        'breadcrumb': 'SVG → PNG',
        'cross_banner_text': 'Need to compress the PNG after converting?',
        'cross_banner_link_text': '🗜️ Compress Image →',
        'cross_banner_href': '../compress-image.html',
    },
    'index.html': {
        'title': 'Free Online Image Tools – Compress Resize Convert Edit | WooaImage',
        'desc':  'Free online image tools: compress, resize, convert, crop, rotate, filter, background remove, OCR and more. No signup. Files never leave your browser.',
        'kw':    'free image tools, image compressor, image resizer, image converter, JPG PNG WebP converter, background remover, image OCR, WooaImage',
        'og_title': 'Free Online Image Tools – WooaImage',
        'og_desc':  'Compress, resize, convert, crop, rotate, remove backgrounds, and more. 25+ free image tools — no signup, files never uploaded.',
        'app_name': 'WooaImage',
        'faq': [],
        'h1': 'Free Online Image Tools',
        'tool_desc': 'All image tools in one place — compress, resize, convert, crop, rotate, filter, remove backgrounds, OCR, and more. Free, no signup, browser-based.',
        'breadcrumb': 'Home',
        'cross_banner_text': '',
        'cross_banner_link_text': '',
        'cross_banner_href': '',
    },
}

# ── 2. 공통 문자열 치환 ──────────────────────────────────────────────────────
COMMON = [
    # lang
    ('<html lang="ko">', '<html lang="en">'),
    # locale
    ('ko_KR', 'en_US'),
    # inLanguage
    ('"inLanguage": "ko"', '"inLanguage": "en"'),
    # priceCurrency
    ('"priceCurrency": "KRW"', '"priceCurrency": "USD"'),
    # paths: CSS, JS, manifest
    ('href="css/style.css"', 'href="../css/style.css"'),
    ('href="/manifest.json"', 'href="../manifest.json"'),
    ('src="js/', 'src="../js/'),
    ('href="js/', 'href="../js/'),
    # header nav links
    ('>JPG→PNG<', '>JPG→PNG<'),
    ('>이미지 압축<', '>Compress<'),
    ('>리사이즈<', '>Resize<'),
    ('>회전/뒤집기<', '>Rotate/Flip<'),
    ('>자르기<', '>Crop<'),
    ('>전체 도구 ›<', '>All Tools ›<'),
    # header-right
    ('>소개<', '>About<'),
    # breadcrumb home
    ('>🏠 홈<', '>🏠 Home<'),
    # drop zone
    ('이미지 파일을 여기에 끌어다 놓으세요', 'Drop your image file here'),
    ('이미지 파일들을 여기에 끌어다 놓으세요', 'Drop your image files here'),
    ('파일을 여기에 끌어다 놓으세요', 'Drop your file here'),
    ('또는 버튼을 클릭해서 파일을 선택하세요', 'or click the button to select a file'),
    ('이미지 파일 선택', 'Select Image File'),
    ('이미지 파일들 선택', 'Select Image Files'),
    ('파일 선택', 'Select File'),
    # file panel
    ('>선택된 파일<', '>Selected File<'),
    ('선택된 파일', 'Selected File'),
    # options titles
    ('<div class="options-title">압축 설정</div>', '<div class="options-title">Compression Settings</div>'),
    ('<div class="options-title">변환 설정</div>', '<div class="options-title">Conversion Settings</div>'),
    ('<div class="options-title">리사이즈 설정</div>', '<div class="options-title">Resize Settings</div>'),
    ('<div class="options-title">회전 설정</div>', '<div class="options-title">Rotation Settings</div>'),
    ('<div class="options-title">자르기 설정</div>', '<div class="options-title">Crop Settings</div>'),
    ('<div class="options-title">워터마크 설정</div>', '<div class="options-title">Watermark Settings</div>'),
    ('<div class="options-title">필터 설정</div>', '<div class="options-title">Filter Settings</div>'),
    ('<div class="options-title">GIF 설정</div>', '<div class="options-title">GIF Settings</div>'),
    ('<div class="options-title">업스케일 설정</div>', '<div class="options-title">Upscale Settings</div>'),
    # option labels
    ('<span class="option-label">압축 품질</span>', '<span class="option-label">Compression Quality</span>'),
    ('<span class="option-label">출력 형식</span>', '<span class="option-label">Output Format</span>'),
    ('<span class="option-label">품질</span>', '<span class="option-label">Quality</span>'),
    ('<span class="option-label">너비</span>', '<span class="option-label">Width</span>'),
    ('<span class="option-label">높이</span>', '<span class="option-label">Height</span>'),
    ('<span class="option-label">비율 고정</span>', '<span class="option-label">Lock Ratio</span>'),
    ('<span class="option-label">단위</span>', '<span class="option-label">Unit</span>'),
    ('<span class="option-label">회전 각도</span>', '<span class="option-label">Rotation Angle</span>'),
    ('<span class="option-label">워터마크 텍스트</span>', '<span class="option-label">Watermark Text</span>'),
    ('<span class="option-label">글자 크기</span>', '<span class="option-label">Font Size</span>'),
    ('<span class="option-label">색상</span>', '<span class="option-label">Color</span>'),
    ('<span class="option-label">투명도</span>', '<span class="option-label">Opacity</span>'),
    ('<span class="option-label">위치</span>', '<span class="option-label">Position</span>'),
    ('<span class="option-label">테두리 두께</span>', '<span class="option-label">Border Width</span>'),
    ('<span class="option-label">테두리 색상</span>', '<span class="option-label">Border Color</span>'),
    ('<span class="option-label">모서리 반경</span>', '<span class="option-label">Corner Radius</span>'),
    ('<span class="option-label">프레임 간격</span>', '<span class="option-label">Frame Delay</span>'),
    ('<span class="option-label">반복 횟수</span>', '<span class="option-label">Loop Count</span>'),
    ('<span class="option-label">배율</span>', '<span class="option-label">Scale</span>'),
    ('<span class="option-label">분할 방식</span>', '<span class="option-label">Split Method</span>'),
    ('<span class="option-label">가로 분할</span>', '<span class="option-label">Columns</span>'),
    ('<span class="option-label">세로 분할</span>', '<span class="option-label">Rows</span>'),
    ('<span class="option-label">블록 크기</span>', '<span class="option-label">Block Size</span>'),
    ('<span class="option-label">언어</span>', '<span class="option-label">Language</span>'),
    # buttons
    ('>🗜️ 압축 시작<', '>🗜️ Compress<'),
    ('>🔄 변환 시작<', '>🔄 Convert<'),
    ('>🔄 변환<', '>🔄 Convert<'),
    ('>📐 리사이즈 시작<', '>📐 Resize<'),
    ('>✂️ 자르기 시작<', '>✂️ Crop<'),
    ('>🔄 회전 적용<', '>🔄 Apply Rotation<'),
    ('>💧 워터마크 추가<', '>💧 Add Watermark<'),
    ('>🎨 필터 적용<', '>🎨 Apply Filter<'),
    ('>🎞️ GIF 만들기<', '>🎞️ Make GIF<'),
    ('>🔍 업스케일 시작<', '>🔍 Upscale<'),
    ('>📤 OCR 시작<', '>📤 Run OCR<'),
    ('>🔍 텍스트 추출 시작<', '>🔍 Extract Text<'),
    ('>✂️ 분할 시작<', '>✂️ Split<'),
    ('>🔗 합치기 시작<', '>🔗 Merge<'),
    ('>🖼️ 콜라주 만들기<', '>🖼️ Make Collage<'),
    ('>➕ 이미지 추가<', '>➕ Add Image<'),
    ('>+ 이미지 추가<', '>+ Add Image<'),
    ('>지우기<', '>Clear<'),
    ('>전체 선택<', '>Select All<'),
    ('>선택 해제<', '>Deselect<'),
    # progress
    ('>변환 중...<', '>Processing...<'),
    ('>처리 중...<', '>Processing...<'),
    ('>압축 중...<', '>Compressing...<'),
    # result titles
    ('<div class="result-title">압축 완료!</div>', '<div class="result-title">Compressed!</div>'),
    ('<div class="result-title">변환 완료!</div>', '<div class="result-title">Done!</div>'),
    ('<div class="result-title">완료!</div>', '<div class="result-title">Done!</div>'),
    ('<div class="result-title">처리 완료!</div>', '<div class="result-title">Done!</div>'),
    # size labels
    ('<div class="size-label">원본</div>', '<div class="size-label">Original</div>'),
    ('<div class="size-label">압축 후</div>', '<div class="size-label">Compressed</div>'),
    ('<div class="size-label">감소율</div>', '<div class="size-label">Reduction</div>'),
    # download
    ('>⬇️ 압축된 이미지 다운로드<', '>⬇️ Download Compressed Image<'),
    ('>⬇️ 변환된 이미지 다운로드<', '>⬇️ Download Converted Image<'),
    ('>⬇️ 이미지 다운로드<', '>⬇️ Download Image<'),
    ('>⬇️ 다운로드<', '>⬇️ Download<'),
    ('⬇️ 전체 다운로드 (ZIP)', '⬇️ Download All (ZIP)'),
    ('>⬇️ ZIP으로 다운로드<', '>⬇️ Download ZIP<'),
    ('>⬇️ GIF 다운로드<', '>⬇️ Download GIF<'),
    ('>⬇️ Base64 다운로드<', '>⬇️ Download Base64<'),
    ('>📋 복사<', '>📋 Copy<'),
    ('>📋 Base64 복사<', '>📋 Copy Base64<'),
    ('>📤 공유하기<', '>📤 Share<'),
    # features section
    ('개인정보 보호', 'Privacy Protected'),
    ('파일이 서버로 전송되지 않습니다', 'Files never sent to server'),
    ('>빠른 처리<', '>Fast Processing<'),
    ('로컬 처리로 속도 빠름', 'Fast local processing'),
    ('>완전 무료<', '>Completely Free<'),
    ('회원가입 없이 무제한 사용', 'Unlimited, no signup'),
    # footer
    ('모든 권리 보유.', 'All rights reserved.'),
    ('>개인정보처리방침<', '>Privacy Policy<'),
    ('href="privacy.html"', 'href="../privacy.html"'),
    ('href="about.html"', 'href="../about.html"'),
    ('href="index.html"', 'href="../index.html"'),
    # FAQ section heading
    ('>자주 묻는 질문<', '>Frequently Asked Questions<'),
    # our-sites-bar active link: imagekit 영어 버전
    ('href="https://imagekit.wooahouse.com/" target="_blank" rel="noopener" class="active"',
     'href="https://imagekit.wooahouse.com/en/" target="_blank" rel="noopener" class="active"'),
    # PWA button
    ('>📌 홈 화면에 추가<', '>📌 Add to Home Screen<'),
    # JPG/PNG support text
    ('JPG, PNG 파일을 업로드하세요', 'Upload JPG or PNG files'),
    ('JPG, PNG, WebP 파일을 업로드하세요', 'Upload JPG, PNG, or WebP files'),
    ('지원 형식:', 'Supported formats:'),
    # quality slider labels
    ('<span>낮음 (소용량)</span>', '<span>Low (small size)</span>'),
    ('<span>높음 (고화질)</span>', '<span>High (best quality)</span>'),
    # mode tabs
    ('픽셀', 'Pixels'),
    ('비율 (%)', 'Percent (%)'),
    # file info
    ('파일 정보', 'File Info'),
    # rotation buttons
    ('>↩️ 90° 왼쪽<', '>↩️ 90° Left<'),
    ('>↪️ 90° 오른쪽<', '>↪️ 90° Right<'),
    ('>↕️ 상하 반전<', '>↕️ Flip Vertical<'),
    ('>↔️ 좌우 반전<', '>↔️ Flip Horizontal<'),
    # JS button states
    ("btn.textContent = '⏳ 변환 중...';", "btn.textContent = '⏳ Converting...';"),
    ("btn.textContent = '⏳ 압축 중...';", "btn.textContent = '⏳ Compressing...';"),
    ("btn.textContent = '⏳ 처리 중...';", "btn.textContent = '⏳ Processing...';"),
    ("btn.textContent = '🗜️ 압축 시작';", "btn.textContent = '🗜️ Compress';"),
    ("btn.textContent = '🔄 변환 시작';", "btn.textContent = '🔄 Convert';"),
    # JS error messages
    ("showError('이미지 파일을 선택해주세요.');", "showError('Please select an image file.');"),
    ("showError('파일을 선택해주세요.');", "showError('Please select a file.');"),
    ("showError('지원하지 않는 파일 형식입니다.');", "showError('Unsupported file format.');"),
    ("showError('처리 중 오류가 발생했습니다.');", "showError('An error occurred during processing.');"),
    ("showError('처리 중 오류가 발생했습니다: ' + err.message);", "showError('Processing failed: ' + err.message);"),
    # progress
    ("'처리 중...'", "'Processing...'"),
    ("'변환 중...'", "'Converting...'"),
    ("'압축 중...'", "'Compressing...'"),
    # JS template literals
    ("`${Math.round(ratio * 100)}% 감소`", "`${Math.round(ratio * 100)}% smaller`"),
    # about/info links
    ('"WooaImage이란?"', '"What is WooaImage?"'),
    ('"서비스 특징"', '"Features"'),
    # OCR language options
    ('<option value="kor+eng">한국어 + English</option>', '<option value="kor+eng">Korean + English</option>'),
    ('<option value="kor">한국어만</option>', '<option value="kor">Korean only</option>'),
    ('<option value="eng">English only</option>', '<option value="eng">English only</option>'),
    # cross-link banner spans
    ('<span>이미지 압축</span>', '<span>Compress Image</span>'),
    ('<span>이미지 리사이즈</span>', '<span>Resize Image</span>'),
    ('<span>이미지 회전</span>', '<span>Rotate Image</span>'),
    ('<span>이미지 자르기</span>', '<span>Crop Image</span>'),
    ('<span>JPG → PNG</span>', '<span>JPG → PNG</span>'),
    ('<span>PNG → JPG</span>', '<span>PNG → JPG</span>'),
    # image info labels
    ('파일명', 'File Name'),
    ('파일 크기', 'File Size'),
    ('해상도', 'Resolution'),
    ('파일 형식', 'Format'),
    # GIF labels
    ('프레임 수', 'Frames'),
    ('반복', 'Loop'),
    ('무한 반복', 'Infinite loop'),
    # upscale labels
    ('2배 업스케일', '2x Upscale'),
    ('4배 업스케일', '4x Upscale'),
    # bg-remove
    ('배경 제거 중...', 'Removing background...'),
    ('AI 모델 로딩 중...', 'Loading AI model...'),
    # split image
    ('가로 분할 수', 'Columns'),
    ('세로 분할 수', 'Rows'),
    # mosaic
    ('모자이크 적용', 'Apply Mosaic'),
    ('모자이크 블록 크기', 'Mosaic Block Size'),
    # collage layout
    ('레이아웃 선택', 'Select Layout'),
    ('2분할 (좌우)', '2 Split (side by side)'),
    ('2분할 (상하)', '2 Split (top/bottom)'),
    ('3분할', '3 Split'),
    ('4분할 격자', '2×2 Grid'),
    # border style
    ('실선', 'Solid'),
    ('점선', 'Dashed'),
    ('이중선', 'Double'),
    # footer bottom
    ('© 2026 WooaImage. 모든 권리 보유.', '© 2026 WooaImage. All rights reserved.'),
    ('© 2026 WooaImage by WooaHouse. 모든 권리 보유.', '© 2026 WooaImage by WooaHouse. All rights reserved.'),
]

# ── 3. 언어 선택기 CSS ────────────────────────────────────────────────────────
LANG_SWITCHER_CSS = """    .lang-switcher { display:flex; align-items:center; gap:4px; }
    .lang-switcher a { color:rgba(255,255,255,0.7); text-decoration:none; font-size:0.8rem; font-weight:600; padding:3px 8px; border-radius:12px; transition:background 0.15s; }
    .lang-switcher a.active { color:white; background:rgba(255,255,255,0.25); }
    .lang-switcher a:hover { color:white; background:rgba(255,255,255,0.18); }
    .lang-switcher span { color:rgba(255,255,255,0.3); font-size:0.75rem; }
"""

def build_page(filename, meta):
    ko_path = os.path.join(BASE, filename)
    en_path = os.path.join(EN_DIR, filename)

    with open(ko_path, encoding='utf-8') as f:
        html = f.read()

    # ── 메타 태그 교체 ──
    html = re.sub(r'<title>[^<]+</title>', f'<title>{meta["title"]}</title>', html)
    html = re.sub(r'<meta name="description" content="[^"]*"', f'<meta name="description" content="{meta["desc"]}"', html)
    html = re.sub(r'<meta name="keywords" content="[^"]*"', f'<meta name="keywords" content="{meta["kw"]}"', html)
    html = re.sub(r'<meta property="og:title" content="[^"]*"', f'<meta property="og:title" content="{meta["og_title"]}"', html)
    html = re.sub(r'<meta property="og:description" content="[^"]*"', f'<meta property="og:description" content="{meta["og_desc"]}"', html)
    html = re.sub(r'<meta property="og:url" content="[^"]*"', f'<meta property="og:url" content="https://imagekit.wooahouse.com/en/{filename}"', html)
    html = re.sub(r'<link rel="canonical" href="[^"]*"', f'<link rel="canonical" href="https://imagekit.wooahouse.com/en/{filename}"', html)

    # ── hreflang 추가 (canonical 바로 뒤) ──
    hreflang = (f'\n  <link rel="alternate" hreflang="ko" href="https://imagekit.wooahouse.com/{filename}">'
                f'\n  <link rel="alternate" hreflang="en" href="https://imagekit.wooahouse.com/en/{filename}">'
                f'\n  <link rel="alternate" hreflang="x-default" href="https://imagekit.wooahouse.com/en/{filename}">')
    html = re.sub(r'(<link rel="canonical"[^>]*>)', r'\1' + hreflang, html)

    # ── ld+json 업데이트 ──
    html = re.sub(r'"name": "([^"]*[가-힣][^"]*)"', f'"name": "{meta["app_name"]}"', html)
    html = re.sub(r'"description": "([^"]*[가-힣][^"]*)"', f'"description": "{meta["desc"]}"', html)
    html = re.sub(r'"url": "https://imagekit\.wooahouse\.com/' + re.escape(filename) + '"',
                  f'"url": "https://imagekit.wooahouse.com/en/{filename}"', html)

    # ── FAQ 교체 ──
    if meta.get('faq'):
        faq_items = meta['faq']
        faq_html_parts = []
        for i, (q, a) in enumerate(faq_items):
            is_last = (i == len(faq_items) - 1)
            mb = '' if is_last else 'margin-bottom:1.2rem;'
            faq_html_parts.append(
                f'      <div class="faq-item" style="{mb}padding:1rem;background:#f8f9fa;border-radius:8px;">\n'
                f'        <h3 style="font-size:1rem;font-weight:600;margin-bottom:0.5rem;">Q. {q}</h3>\n'
                f'        <p style="color:#555;margin:0;">{a}</p>\n'
                f'      </div>'
            )
        faq_inner = '\n'.join(faq_html_parts)
        html = re.sub(
            r'<div class="faq-list">.*?</div>\s*</section>',
            f'<div class="faq-list">\n{faq_inner}\n    </div>\n  </section>',
            html, flags=re.DOTALL
        )
        html = re.sub(r'<h2[^>]*>자주 묻는 질문</h2>', '<h2 style="font-size:1.4rem;margin-bottom:1.5rem;">Frequently Asked Questions</h2>', html)
        # FAQPage ld+json 교체
        faq_entities = []
        for q, a in faq_items:
            faq_entities.append({
                "@type": "Question",
                "name": q,
                "acceptedAnswer": {"@type": "Answer", "text": a}
            })
        new_faq_json = _json.dumps({
            "@context": "https://schema.org",
            "@type": "FAQPage",
            "mainEntity": faq_entities
        }, ensure_ascii=False, indent=2)
        html = re.sub(
            r'<script type="application/ld\+json">\s*\{[^<]*"FAQPage"[^<]*\}[^<]*</script>',
            f'<script type="application/ld+json">\n{new_faq_json}\n</script>',
            html, flags=re.DOTALL
        )

    # ── cross-link banner 교체 ──
    if meta.get('cross_banner_text'):
        # cross-link-banner div 전체를 찾아 교체 (span + a 구조 통째로)
        new_banner = (
            f'  <div class="cross-link-banner">\n'
            f'    <span>{meta["cross_banner_text"]}</span>\n'
            f'    <a href="{meta["cross_banner_href"]}">{meta["cross_banner_link_text"]}</a>\n'
            f'  </div>'
        )
        html = re.sub(
            r'<div class="cross-link-banner">.*?</div>',
            new_banner,
            html, flags=re.DOTALL
        )

    # ── Tool header (h1, desc, breadcrumb) ──
    if meta.get('h1'):
        replaced = re.sub(r'<h1 id="toolTitle">[^<]*</h1>', f'<h1 id="toolTitle">{meta["h1"]}</h1>', html)
        if replaced == html:
            replaced = re.sub(r'<h1>([^<]*)</h1>', f'<h1>{meta["h1"]}</h1>', html, count=1)
        html = replaced
    if meta.get('tool_desc'):
        replaced = re.sub(r'<p id="toolDesc">[^<]*</p>', f'<p id="toolDesc">{meta["tool_desc"]}</p>', html)
        html = replaced
    if meta.get('breadcrumb'):
        html = re.sub(r'<span id="breadcrumbTitle">[^<]*</span>', f'<span id="breadcrumbTitle">{meta["breadcrumb"]}</span>', html)

    # ── 공통 문자열 치환 ──
    for ko, en in COMMON:
        html = html.replace(ko, en)

    # ── 언어 선택기 CSS 삽입 ──
    if 'lang-switcher' not in html:
        html = html.replace('  </style>', LANG_SWITCHER_CSS + '  </style>', 1)
        if '  </style>' not in html:
            # </head> 바로 앞에 스타일 블록 삽입
            html = html.replace('</head>', f'  <style>\n{LANG_SWITCHER_CSS}  </style>\n</head>', 1)

    # ── 헤더에 언어 선택기 삽입 ──
    html = re.sub(
        r'(\s*</div>\s*</header>)',
        f'\n    <div class="header-right">\n'
        f'      <div class="lang-switcher">\n'
        f'        <a href="../{filename}">KO</a>\n'
        f'        <span>|</span>\n'
        f'        <a href="{filename}" class="active">EN</a>\n'
        f'      </div>\n'
        f'      <a href="../about.html" style="color:rgba(255,255,255,0.85); font-size:0.85rem; text-decoration:none; margin-left:8px;">About</a>\n'
        f'    </div>\n'
        f'  </div>\n'
        f'</header>',
        html, count=1
    )

    # ── 쿠팡 완전 제거 → 애드센스로 교체 ──
    ADSENSE_BLOCK = (
        '<div style="text-align:center;margin:32px auto 0;max-width:728px;padding:0 8px">\n'
        '<ins class="adsbygoogle"\n'
        '     style="display:block"\n'
        '     data-ad-client="ca-pub-6464921081676309"\n'
        '     data-ad-slot="7080296704"\n'
        '     data-ad-format="auto"\n'
        '     data-full-width-responsive="true"></ins>\n'
        '<script>(adsbygoogle = window.adsbygoogle || []).push({});</script>\n'
        '</div>'
    )
    html = re.sub(r'\s*<script src="https://ads-partners\.coupang\.com/g\.js"></script>\n?', '', html)
    html = re.sub(
        r'<!-- Coupang Partners -->\s*<div[^>]*>.*?</div>',
        ADSENSE_BLOCK,
        html, flags=re.DOTALL
    )
    html = re.sub(r'<script>\s*new PartnersCoupang\.G\([^)]*\);?\s*</script>', '', html)
    html = re.sub(r'<p class="coupang-notice">[^<]*</p>', '', html)

    # ── og:locale 교체 ──
    html = html.replace('content="ko_KR"', 'content="en_US"')

    with open(en_path, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f'  OK en/{filename}')


# ── 4. 실행 ──────────────────────────────────────────────────────────────────
if __name__ == '__main__':
    print('Building English pages for WooaImage...')
    for filename, meta in PAGE_META.items():
        ko_path = os.path.join(BASE, filename)
        if os.path.exists(ko_path):
            build_page(filename, meta)
        else:
            print(f'  SKIP {filename} (not found)')

    # about, privacy 처리
    ABOUT_EXTRA = [
        ('<title>서비스 소개 | WooaImage - 무료 온라인 이미지 도구</title>',
         '<title>About WooaImage – Free Online Image Tools</title>'),
        ('<meta name="description" content="WooaImage은 이미지 압축, 변환, 편집 등 모든 이미지 작업을 무료로 제공하는 온라인 도구 모음 서비스입니다.">',
         '<meta name="description" content="WooaImage is a free online image toolkit for compressing, converting, and editing images — all in your browser. No signup, files never uploaded.">'),
        ('<h1>서비스 소개</h1>', '<h1>About WooaImage</h1>'),
        ('<p class="subtitle">WooaImage에 대해 알아보세요</p>', '<p class="subtitle">Learn about WooaImage</p>'),
        ('<h2>🖼️ WooaImage이란?</h2>', '<h2>🖼️ What is WooaImage?</h2>'),
        ('WooaImage은 이미지 압축, 리사이즈, 형식 변환, 회전, 자르기, 워터마크 추가 등 다양한 이미지 작업을 브라우저에서 직접 처리하는 무료 온라인 도구 모음입니다.',
         'WooaImage is a free online image toolkit that handles compression, resizing, format conversion, rotation, cropping, watermarking, and more — all directly in your browser.'),
        ('회원가입 없이 바로 사용할 수 있으며, 업로드된 파일이 서버에 저장되지 않아 개인 정보와 이미지를 안전하게 보호합니다.',
         'No signup required. Files are never sent to a server, keeping your images and personal data safe.'),
        ('<h2>✅ 서비스 특징</h2>', '<h2>✅ Key Features</h2>'),
        ('모든 이미지 처리가 브라우저 내 Canvas API로 이루어져 파일이 서버에 전송되지 않음',
         'All image processing uses the browser Canvas API — files are never sent to a server'),
        ('회원가입 없이 즉시 사용 가능, 100% 무료',
         'Instant access, no signup, 100% free'),
        ('이미지 압축·리사이즈·변환·자르기·회전·워터마크·Base64 변환 등 11가지 도구',
         'Image compression, resize, convert, crop, rotate, watermark, Base64 encoding and more'),
        ('JPG, PNG, WebP, GIF 등 주요 이미지 형식 지원',
         'Supports JPG, PNG, WebP, GIF and other major formats'),
        ('PC·태블릿·스마트폰 모든 기기에서 편리하게 이용 가능',
         'Works on PC, tablet, and smartphone'),
        ('<h2>🛠️ 제공 도구</h2>', '<h2>🛠️ Available Tools</h2>'),
        ('이미지 압축 — JPG/PNG 파일 용량 줄이기', 'Image Compress — Reduce JPG/PNG file size'),
        ('이미지 리사이즈 — 픽셀 또는 비율로 크기 조정', 'Image Resize — Resize by pixel or percentage'),
        ('이미지 회전/뒤집기 — 90°/180°/270° 회전, 좌우/상하 반전', 'Rotate/Flip — 90°/180°/270° rotation, horizontal/vertical flip'),
        ('이미지 자르기 — 자유 크롭 또는 비율 크롭', 'Crop Image — Free crop or aspect ratio crop'),
        ('JPG → PNG / PNG → JPG 변환', 'JPG → PNG / PNG → JPG conversion'),
        ('이미지 → WebP 변환 — 용량 절감 최적화', 'Image → WebP — File size optimization'),
        ('WebP → JPG/PNG 변환', 'WebP → JPG/PNG conversion'),
        ('이미지 → Base64 인코딩', 'Image → Base64 encoding'),
        ('워터마크 추가 — 텍스트 워터마크 삽입', 'Add Watermark — Insert text watermark'),
        ('이미지 정보 확인 — 해상도, 파일 크기, 형식 등', 'Image Info — Resolution, file size, format and more'),
        ('<h2>🏠 WooaHouse 네트워크</h2>', '<h2>🏠 WooaHouse Network</h2>'),
        ('WooaImage은 WooaHouse가 운영하는 서비스 중 하나입니다. 현재 운영 중인 서비스:',
         'WooaImage is one of the services operated by WooaHouse. Currently available services:'),
        ('<h2>📬 문의</h2>', '<h2>📬 Contact</h2>'),
        ('도구 추가 요청, 오류 제보, 제휴 문의 등은 아래 이메일로 연락 주세요.',
         'For tool requests, bug reports, or partnership inquiries, please contact us at:'),
    ]
    PRIVACY_EXTRA = [
        ('<title>개인정보처리방침 | WooaImage</title>', '<title>Privacy Policy | WooaImage</title>'),
        ('<h1>개인정보처리방침</h1>', '<h1>Privacy Policy</h1>'),
        ('<h1 style="font-size:1.8rem;">개인정보처리방침</h1>', '<h1 style="font-size:1.8rem;">Privacy Policy</h1>'),
        ('WooaImage은 이미지 압축, 변환 등 다양한 이미지 작업을 무료로 제공하는 온라인 도구입니다. 파일은 서버에 저장되지 않으며 사용자의 개인정보를 수집하지 않습니다.',
         'WooaImage is a free online image tool for compression, conversion, and more. Files are never uploaded to servers and we do not collect personal information.'),
        ('<h2>1. 수집하는 정보</h2>', '<h2>1. Information We Collect</h2>'),
        ('<h2>2. 쿠키 및 광고</h2>', '<h2>2. Cookies &amp; Advertising</h2>'),
        ('<h2>3. 개인정보의 이용 목적</h2>', '<h2>3. Purpose of Data Use</h2>'),
        ('<h2>4. 개인정보의 제3자 제공</h2>', '<h2>4. Sharing with Third Parties</h2>'),
        ('<h2>5. 개인정보 보호 조치</h2>', '<h2>5. Privacy Protection Measures</h2>'),
        ('<h2>6. 사용자의 권리</h2>', '<h2>6. Your Rights</h2>'),
        ('<h2>7. 아동의 개인정보 보호</h2>', '<h2>7. Children\'s Privacy</h2>'),
        ('<h2>8. 개인정보처리방침의 변경</h2>', '<h2>8. Changes to This Policy</h2>'),
        ('<h2>9. 문의</h2>', '<h2>9. Contact</h2>'),
        ('WooaImage은 사용자의 개인정보 보호를 매우 중요하게 생각합니다.',
         'WooaImage takes your privacy seriously.'),
        ('모든 이미지 처리는 사용자의 브라우저에서만 이루어지며, 어떠한 파일도 서버로 전송되지 않습니다.',
         'All image processing happens only in your browser. No files are ever sent to a server.'),
        ('서비스명: WooaImage<br>', 'Service: WooaImage<br>'),
        ('이메일 문의는 서비스 내 문의 기능을 통해 주시기 바랍니다.',
         'Contact: linker@wooahouse.com'),
    ]

    for f in ['about.html', 'privacy.html']:
        src = os.path.join(BASE, f)
        dst = os.path.join(EN_DIR, f)
        if os.path.exists(src):
            with open(src, encoding='utf-8') as fp:
                html = fp.read()
            for ko, en in COMMON:
                html = html.replace(ko, en)
            html = html.replace('<html lang="ko">', '<html lang="en">')
            html = html.replace('content="ko_KR"', 'content="en_US"')
            extras = ABOUT_EXTRA if f == 'about.html' else PRIVACY_EXTRA
            for ko, en in extras:
                html = html.replace(ko, en)
            html = re.sub(r'<link rel="canonical" href="[^"]*"',
                          f'<link rel="canonical" href="https://imagekit.wooahouse.com/en/{f}"', html)
            html = re.sub(r'<meta property="og:url" content="[^"]*"',
                          f'<meta property="og:url" content="https://imagekit.wooahouse.com/en/{f}"', html)
            # lang switcher CSS
            if 'lang-switcher' not in html:
                if '  </style>' in html:
                    html = html.replace('  </style>', LANG_SWITCHER_CSS + '  </style>', 1)
                else:
                    html = html.replace('</head>', f'  <style>\n{LANG_SWITCHER_CSS}  </style>\n</head>', 1)
            # lang switcher HTML
            if 'lang-switcher' not in html:
                sw_html = (
                    f'    <div class="header-right">\n'
                    f'      <div class="lang-switcher">\n'
                    f'        <a href="../{f}">KO</a>\n'
                    f'        <span>|</span>\n'
                    f'        <a href="{f}" class="active">EN</a>\n'
                    f'      </div>\n'
                )
                html = html.replace('    <div class="header-right">', sw_html, 1)
            # 쿠팡 제거
            html = re.sub(r'\s*<script src="https://ads-partners\.coupang\.com/g\.js"></script>\n?', '', html)
            html = re.sub(r'<!-- Coupang Partners -->\s*<div[^>]*>.*?</div>', '', html, flags=re.DOTALL)
            html = re.sub(r'<script>\s*new PartnersCoupang\.G\([^)]*\);?\s*</script>', '', html)
            html = re.sub(r'<p class="coupang-notice">[^<]*</p>', '', html)
            with open(dst, 'w', encoding='utf-8') as fp:
                fp.write(html)
            print(f'  OK en/{f}')
        else:
            print(f'  SKIP {f} (not found)')

    print(f'\nDone! {len(PAGE_META) + 2} files generated in en/')
