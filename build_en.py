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
    # ── index.html: twitter meta ──
    ('<meta name="twitter:title" content="무료 온라인 이미지 도구 모음 | WooaImage">',
     '<meta name="twitter:title" content="Free Online Image Tools | WooaImage">'),
    ('<meta name="twitter:description" content="이미지 압축, 리사이즈, 변환, 배경 제거, HEIC 변환, GIF 만들기, 업스케일링, OCR 등 17가지 무료 이미지 도구">',
     '<meta name="twitter:description" content="17+ free online image tools: compress, resize, convert, background remove, HEIC, GIF, upscale, OCR and more.">'),
    # ── index.html: ld+json ItemList names ──
    ('"name":"JPG → PNG 변환"', '"name":"JPG to PNG Converter"'),
    ('"name":"PNG → JPG 변환"', '"name":"PNG to JPG Converter"'),
    ('"name":"이미지 → WebP 변환"', '"name":"Image to WebP Converter"'),
    ('"name":"WebP → JPG/PNG 변환"', '"name":"WebP to JPG/PNG Converter"'),
    ('"name":"이미지 압축"', '"name":"Image Compressor"'),
    ('"name":"이미지 리사이즈"', '"name":"Image Resizer"'),
    ('"name":"이미지 회전/뒤집기"', '"name":"Rotate & Flip Image"'),
    ('"name":"이미지 자르기"', '"name":"Crop Image"'),
    ('"name":"이미지 → Base64"', '"name":"Image to Base64"'),
    ('"name":"워터마크 추가"', '"name":"Add Watermark"'),
    ('"name":"이미지 정보 확인"', '"name":"Image Info"'),
    ('"name":"이미지 텍스트 추출 (OCR)"', '"name":"Image OCR – Text Extraction"'),
    ('"name":"PDF 텍스트 추출 (OCR)"', '"name":"PDF OCR – Text Extraction"'),
    ('"name":"HEIC → JPG 변환"', '"name":"HEIC to JPG Converter"'),
    ('"name":"GIF 만들기"', '"name":"Make GIF"'),
    ('"name":"이미지 업스케일링"', '"name":"Image Upscaler"'),
    ('"name":"이미지 필터"', '"name":"Image Filters"'),
    ('"name":"EXIF 데이터 제거"', '"name":"EXIF Data Remover"'),
    ('"name":"PNG → ICO 변환"', '"name":"PNG to ICO Converter"'),
    ('"name":"이미지 합치기"', '"name":"Merge Images"'),
    ('"name":"이미지 모자이크"', '"name":"Image Mosaic"'),
    ('"name":"이미지 텍스트 추가"', '"name":"Add Text to Image"'),
    ('"name":"이미지 둥근 모서리"', '"name":"Rounded Corners"'),
    ('"name":"이미지 분할"', '"name":"Split Image"'),
    ('"name":"이미지 도구 목록"', '"name":"Image Tools"'),
    ('"description": "이미지 압축, 리사이즈, 변환, 편집 등 무료 온라인 이미지 도구 모음"',
     '"description": "Free online image toolkit for compressing, resizing, converting and editing images"'),
    # ── index.html: hero section ──
    ('<h1>모든 이미지 작업 무료로, 한 곳에서</h1>', '<h1>All Image Tools, Free in One Place</h1>'),
    ('<p>압축·리사이즈·변환·편집까지 <strong style="color:#FFD700;">100% 무료</strong><br>회원가입 없이, 파일은 서버에 저장되지 않아요</p>',
     '<p>Compress, resize, convert, edit — <strong style="color:#FFD700;">100% FREE</strong><br>No signup, files never stored on a server</p>'),
    ('<span>PDF 작업도 필요하신가요?</span>', '<span>Need to work with PDFs too?</span>'),
    ('<a href="https://pdfkit.wooahouse.com/" target="_blank" rel="noopener">PDFKit에서 무료 PDF 도구 보기 →</a>',
     '<a href="https://pdfkit.wooahouse.com/" target="_blank" rel="noopener">See free PDF tools at WooaPDF →</a>'),
    # ── index.html: category sections ──
    ('<span class="category-title">변환</span>', '<span class="category-title">Convert</span>'),
    ('<p class="category-desc">이미지 포맷을 자유롭게 변환하는 도구</p>', '<p class="category-desc">Tools for converting image formats</p>'),
    ('<span class="category-title">편집</span>', '<span class="category-title">Edit</span>'),
    ('<p class="category-desc">이미지 크기 조정, 회전, 자르기 등 편집 도구</p>', '<p class="category-desc">Resize, rotate, crop and more editing tools</p>'),
    ('<span class="category-title">AI · 변환 확장</span>', '<span class="category-title">AI & Extended Conversions</span>'),
    ('<p class="category-desc">AI 배경 제거, HEIC 변환, GIF 생성, 업스케일링 등 확장 도구</p>',
     '<p class="category-desc">AI background removal, HEIC conversion, GIF maker, upscaling and more</p>'),
    ('<span class="category-title">유틸리티</span>', '<span class="category-title">Utilities</span>'),
    ('<p class="category-desc">이미지 관련 유용한 변환·분석 도구</p>', '<p class="category-desc">Useful image conversion and analysis tools</p>'),
    ('<span class="category-title">OCR · 텍스트 인식</span>', '<span class="category-title">OCR & Text Recognition</span>'),
    ('<p class="category-desc">이미지·PDF에서 텍스트를 인식하고 추출하는 도구</p>',
     '<p class="category-desc">Recognize and extract text from images and PDFs</p>'),
    # ── index.html: tool names ──
    ('<div class="tool-name">이미지 → WebP</div>', '<div class="tool-name">Image → WebP</div>'),
    ('<div class="tool-name">이미지 압축</div>', '<div class="tool-name">Image Compressor</div>'),
    ('<div class="tool-name">이미지 리사이즈</div>', '<div class="tool-name">Image Resizer</div>'),
    ('<div class="tool-name">회전/뒤집기</div>', '<div class="tool-name">Rotate / Flip</div>'),
    ('<div class="tool-name">이미지 자르기</div>', '<div class="tool-name">Crop Image</div>'),
    ('<div class="tool-name">이미지 필터</div>', '<div class="tool-name">Image Filters</div>'),
    ('<div class="tool-name">EXIF 제거</div>', '<div class="tool-name">EXIF Remover</div>'),
    ('<div class="tool-name">이미지 합치기</div>', '<div class="tool-name">Merge Images</div>'),
    ('<div class="tool-name">이미지 모자이크</div>', '<div class="tool-name">Image Mosaic</div>'),
    ('<div class="tool-name">이미지 텍스트 추가</div>', '<div class="tool-name">Add Text to Image</div>'),
    ('<div class="tool-name">이미지 둥근 모서리</div>', '<div class="tool-name">Rounded Corners</div>'),
    ('<div class="tool-name">이미지 분할</div>', '<div class="tool-name">Split Image</div>'),
    ('<div class="tool-name">콜라주 만들기</div>', '<div class="tool-name">Make Collage</div>'),
    ('<div class="tool-name">이미지 테두리 추가</div>', '<div class="tool-name">Image Border</div>'),
    ('<div class="tool-name">배경 제거 (AI)</div>', '<div class="tool-name">Background Remover (AI)</div>'),
    ('<div class="tool-name">GIF 만들기</div>', '<div class="tool-name">Make GIF</div>'),
    ('<div class="tool-name">이미지 업스케일링</div>', '<div class="tool-name">Image Upscaler</div>'),
    ('<div class="tool-name">이미지 → Base64</div>', '<div class="tool-name">Image → Base64</div>'),
    ('<div class="tool-name">워터마크 추가</div>', '<div class="tool-name">Add Watermark</div>'),
    ('<div class="tool-name">이미지 정보</div>', '<div class="tool-name">Image Info</div>'),
    ('<div class="tool-name">이미지 → 텍스트</div>', '<div class="tool-name">Image → Text (OCR)</div>'),
    ('<div class="tool-name">PDF → 텍스트 (OCR)</div>', '<div class="tool-name">PDF → Text (OCR)</div>'),
    # ── index.html: tool descriptions ──
    ('<div class="tool-desc">JPG를 투명 배경 PNG로 변환</div>', '<div class="tool-desc">Convert JPG to transparent-background PNG</div>'),
    ('<div class="tool-desc">PNG를 JPG로, 배경색 설정 가능</div>', '<div class="tool-desc">Convert PNG to JPG with custom background color</div>'),
    ('<div class="tool-desc">JPG/PNG를 WebP로 변환해 용량 절감</div>', '<div class="tool-desc">Convert JPG/PNG to WebP to reduce file size</div>'),
    ('<div class="tool-desc">WebP를 JPG 또는 PNG로 변환</div>', '<div class="tool-desc">Convert WebP to JPG or PNG</div>'),
    ('<div class="tool-desc">파비콘·아이콘용 ICO 파일 생성, 다중 크기 지원</div>',
     '<div class="tool-desc">Generate ICO for favicons/icons, multi-size support</div>'),
    ('<div class="tool-desc">벡터 SVG를 PNG/WebP/JPG로, 배율 지정 가능</div>',
     '<div class="tool-desc">Convert SVG vector to PNG/WebP/JPG at any scale</div>'),
    ('<div class="tool-desc">JPG/PNG 용량 줄이기, 품질 슬라이더</div>',
     '<div class="tool-desc">Compress JPG/PNG with quality slider</div>'),
    ('<div class="tool-desc">픽셀 또는 비율로 이미지 크기 조정</div>',
     '<div class="tool-desc">Resize by pixels or percentage</div>'),
    ('<div class="tool-desc">Pixels 또는 비율로 이미지 크기 조정</div>',
     '<div class="tool-desc">Resize by pixels or percentage</div>'),
    ('<div class="tool-desc">90°/180°/270° 회전, 좌우/상하 뒤집기</div>',
     '<div class="tool-desc">Rotate 90°/180°/270° or flip horizontally/vertically</div>'),
    ('<div class="tool-desc">자유 크롭 또는 비율 크롭</div>', '<div class="tool-desc">Free crop or fixed-ratio crop</div>'),
    ('<div class="tool-desc">밝기·대비·채도·흑백·세피아·블러 실시간 조정</div>',
     '<div class="tool-desc">Adjust brightness, contrast, saturation, grayscale, sepia, blur in real time</div>'),
    ('<div class="tool-desc">GPS 위치·촬영일시 등 개인정보 메타데이터 삭제</div>',
     '<div class="tool-desc">Remove GPS location, date and private metadata from photos</div>'),
    ('<div class="tool-desc">여러 사진을 가로·세로로 이어붙여 하나로 저장</div>',
     '<div class="tool-desc">Combine photos side by side or top/bottom into one image</div>'),
    ('<div class="tool-desc">전체 또는 영역 선택해 픽셀화·모자이크 효과 적용</div>',
     '<div class="tool-desc">Apply mosaic/pixelation to whole image or a selected area</div>'),
    ('<div class="tool-desc">전체 또는 영역 선택해 Pixels화·모자이크 효과 적용</div>',
     '<div class="tool-desc">Apply mosaic/pixelation to whole image or a selected area</div>'),
    ('<div class="tool-desc">사진에 글자 넣기, 폰트·색상·위치 자유 설정</div>',
     '<div class="tool-desc">Add text overlays with custom font, color, and position</div>'),
    ('<div class="tool-desc">모서리 둥글게 처리, 원형 이미지도 가능</div>',
     '<div class="tool-desc">Round corners or create circular images</div>'),
    ('<div class="tool-desc">격자로 나누어 여러 조각으로, ZIP 다운로드</div>',
     '<div class="tool-desc">Split into a grid of pieces, download as ZIP</div>'),
    ('<div class="tool-desc">여러 사진을 하나로 합치기, 레이아웃 선택</div>',
     '<div class="tool-desc">Combine multiple photos into one collage with layout options</div>'),
    ('<div class="tool-desc">색상·두께·모서리·그림자 설정 가능한 액자 효과</div>',
     '<div class="tool-desc">Add borders with custom color, width, corners and shadow</div>'),
    ('<div class="tool-desc">AI로 이미지 배경 자동 제거, 투명 PNG 저장</div>',
     '<div class="tool-desc">AI-powered background removal, saves as transparent PNG</div>'),
    ('<div class="tool-desc">아이폰 HEIC 파일을 JPG/PNG로 변환</div>',
     '<div class="tool-desc">Convert iPhone HEIC files to JPG or PNG</div>'),
    ('<div class="tool-desc">여러 이미지로 움직이는 GIF 생성</div>',
     '<div class="tool-desc">Create animated GIFs from multiple images</div>'),
    ('<div class="tool-desc">저화질 이미지를 최대 4배 고화질로 확대</div>',
     '<div class="tool-desc">Upscale low-res images up to 4× with quality enhancement</div>'),
    ('<div class="tool-desc">이미지를 Base64 인코딩 문자열로 변환</div>',
     '<div class="tool-desc">Convert image to Base64 encoded string</div>'),
    ('<div class="tool-desc">텍스트 워터마크를 이미지에 삽입</div>',
     '<div class="tool-desc">Insert text watermark into image</div>'),
    ('<div class="tool-desc">파일명, 크기, 해상도, EXIF 정보 확인</div>',
     '<div class="tool-desc">View file name, size, resolution, and EXIF info</div>'),
    ('<div class="tool-desc">사진·스크린샷에서 한국어·영어 텍스트 추출</div>',
     '<div class="tool-desc">Extract Korean and English text from photos or screenshots</div>'),
    ('<div class="tool-desc">스캔 PDF에서 페이지별 텍스트 추출</div>',
     '<div class="tool-desc">Extract text from scanned PDFs page by page</div>'),
    # ── index.html: features section ──
    ('<div class="feature-title">100% 안전</div>', '<div class="feature-title">100% Safe</div>'),
    ('<div class="feature-desc">파일이 서버로 전송되지 않습니다. 모든 처리가 브라우저 안에서 이루어집니다.</div>',
     '<div class="feature-desc">Files are never sent to a server. All processing happens in your browser.</div>'),
    ('<div class="feature-title">빠른 처리</div>', '<div class="feature-title">Fast Processing</div>'),
    ('<div class="feature-desc">업로드 없이 로컬에서 처리하므로 인터넷 속도와 무관하게 빠릅니다.</div>',
     '<div class="feature-desc">Local processing — no upload means speed is not limited by your internet connection.</div>'),
    ('<div class="feature-title">완전 무료</div>', '<div class="feature-title">Completely Free</div>'),
    ('<div class="feature-desc">회원가입 없이 모든 기능을 무제한 무료로 사용할 수 있습니다.</div>',
     '<div class="feature-desc">All features, unlimited and free — no signup required.</div>'),
    ('<div class="feature-title">모든 기기 지원</div>', '<div class="feature-title">Works on All Devices</div>'),
    ('<div class="feature-desc">PC, 태블릿, 스마트폰 어디서나 사용 가능한 반응형 디자인.</div>',
     '<div class="feature-desc">Responsive design — works on desktop, tablet, and smartphone.</div>'),
    # ── index.html: footer links ──
    ('<p>무료 온라인 이미지 도구 모음. 압축, 변환, 편집 등 모든 이미지 작업을 안전하게 처리하세요.</p>',
     '<p>Free online image toolkit. Compress, convert, and edit images safely in your browser.</p>'),
    ('<h4>이미지 변환</h4>', '<h4>Image Conversion</h4>'),
    ('<h4>이미지 편집</h4>', '<h4>Image Editing</h4>'),
    ('<h4>유틸리티 · OCR</h4>', '<h4>Utilities & OCR</h4>'),
    ('<a href="image-to-webp.html">이미지 → WebP</a>', '<a href="../image-to-webp.html">Image → WebP</a>'),
    ('<a href="compress-image.html">이미지 압축</a>', '<a href="../compress-image.html">Image Compressor</a>'),
    ('<a href="resize-image.html">이미지 리사이즈</a>', '<a href="../resize-image.html">Image Resizer</a>'),
    ('<a href="rotate-image.html">회전/뒤집기</a>', '<a href="../rotate-image.html">Rotate/Flip</a>'),
    ('<a href="crop-image.html">이미지 자르기</a>', '<a href="../crop-image.html">Crop Image</a>'),
    ('<a href="image-filter.html">이미지 필터</a>', '<a href="../image-filter.html">Image Filters</a>'),
    ('<a href="exif-remove.html">EXIF 제거</a>', '<a href="../exif-remove.html">EXIF Remover</a>'),
    ('<a href="merge-image.html">이미지 합치기</a>', '<a href="../merge-image.html">Merge Images</a>'),
    ('<a href="mosaic-image.html">이미지 모자이크</a>', '<a href="../mosaic-image.html">Image Mosaic</a>'),
    ('<a href="add-text-image.html">이미지 텍스트 추가</a>', '<a href="../add-text-image.html">Add Text to Image</a>'),
    ('<a href="round-corner.html">이미지 둥근 모서리</a>', '<a href="../round-corner.html">Rounded Corners</a>'),
    ('<a href="split-image.html">이미지 분할</a>', '<a href="../split-image.html">Split Image</a>'),
    ('<a href="image-to-base64.html">이미지 → Base64</a>', '<a href="../image-to-base64.html">Image → Base64</a>'),
    ('<a href="watermark-image.html">워터마크 추가</a>', '<a href="../watermark-image.html">Add Watermark</a>'),
    # cross-link banner spans
    ('<span>이미지 압축</span>', '<span>Image Compressor</span>'),
    ('<span>이미지 리사이즈</span>', '<span>Image Resizer</span>'),
    ('<span>이미지 회전</span>', '<span>Rotate Image</span>'),
    ('<span>이미지 자르기</span>', '<span>Crop Image</span>'),
    # free badge
    ('<span class="free-badge">무료</span>', '<span class="free-badge">FREE</span>'),
    # breadcrumb home
    ('>🏠 홈<', '>🏠 Home<'),
    # dropzone
    ('<h3>이미지 파일을 여기에 끌어다 놓으세요</h3>', '<h3>Drop your image file here</h3>'),
    ('<label for="fileInput" class="btn-select">이미지 파일 선택</label>', '<label for="fileInput" class="btn-select">Select Image File</label>'),
    ('<p>JPG, PNG 파일을 업로드하세요</p>', '<p>Upload JPG or PNG files</p>'),
    ('<p>JPG, PNG, WebP 파일을 업로드하세요</p>', '<p>Upload JPG, PNG, or WebP files</p>'),
    ('<p>JPG, PNG, WebP, GIF 등 모든 이미지 형식 가능</p>', '<p>Supports JPG, PNG, WebP, GIF and more</p>'),
    # file info panel
    ('<div class="file-list-title">선택된 파일</div>', '<div class="file-list-title">Selected File</div>'),
    ('<div class="file-list-title">선택된 파일 목록</div>', '<div class="file-list-title">Selected Files</div>'),
    # options titles
    ('<div class="options-title">변환 설정</div>', '<div class="options-title">Conversion Settings</div>'),
    ('<div class="options-title">편집 설정</div>', '<div class="options-title">Edit Settings</div>'),
    ('<div class="options-title">압축 설정</div>', '<div class="options-title">Compression Settings</div>'),
    ('<div class="options-title">리사이즈 설정</div>', '<div class="options-title">Resize Settings</div>'),
    ('<div class="options-title">배경 제거</div>', '<div class="options-title">Background Removal</div>'),
    ('<div class="options-title">텍스트 설정</div>', '<div class="options-title">Text Settings</div>'),
    ('<div class="options-title">테두리 설정</div>', '<div class="options-title">Border Settings</div>'),
    ('<div class="options-title">필터 설정</div>', '<div class="options-title">Filter Settings</div>'),
    ('<div class="options-title">GIF 설정</div>', '<div class="options-title">GIF Settings</div>'),
    ('<div class="options-title">분할 설정</div>', '<div class="options-title">Split Settings</div>'),
    ('<div class="options-title">합치기 설정</div>', '<div class="options-title">Merge Settings</div>'),
    ('<div class="options-title">콜라주 설정</div>', '<div class="options-title">Collage Settings</div>'),
    ('<div class="options-title">모자이크 설정</div>', '<div class="options-title">Mosaic Settings</div>'),
    ('<div class="options-title">업스케일 설정</div>', '<div class="options-title">Upscale Settings</div>'),
    # quality labels (with nested HTML)
    ('<span class="option-label">WebP 품질: <strong id="qualityVal">85</strong>%</span>',
     '<span class="option-label">WebP Quality: <strong id="qualityVal">85</strong>%</span>'),
    ('<span class="option-label">JPG 품질: <strong id="qualityVal">92</strong>%</span>',
     '<span class="option-label">JPG Quality: <strong id="qualityVal">92</strong>%</span>'),
    ('<span class="option-label">압축 품질: <strong id="qualityVal">80</strong>%</span>',
     '<span class="option-label">Compression Quality: <strong id="qualityVal">80</strong>%</span>'),
    # size compare labels
    ('<span style="color:var(--text-light);">원본 크기:</span>', '<span style="color:var(--text-light);">Original Size:</span>'),
    ('<span style="color:var(--text-light);">WebP 크기:</span>', '<span style="color:var(--text-light);">WebP Size:</span>'),
    ('<span style="color:var(--text-light);">절감율:</span>', '<span style="color:var(--text-light);">Reduction:</span>'),
    ('<span style="color:var(--text-light);">압축 후 크기:</span>', '<span style="color:var(--text-light);">Compressed Size:</span>'),
    ('<span style="color:var(--text-light);">변환 후 크기:</span>', '<span style="color:var(--text-light);">Converted Size:</span>'),
    # download buttons (page-specific)
    ('>⬇️ WebP로 다운로드<', '>⬇️ Download as WebP<'),
    ('>⬇️ 투명 PNG 다운로드<', '>⬇️ Download Transparent PNG<'),
    ('>🤖 배경 제거 시작<', '>🤖 Remove Background<'),
    ('>✍️ 텍스트 적용 & 저장 준비<', '>✍️ Apply Text & Prepare Download<'),
    # result titles
    ('<div class="result-title">텍스트 추가 완료!</div>', '<div class="result-title">Text Added!</div>'),
    ('<div class="result-title">배경 제거 완료!</div>', '<div class="result-title">Background Removed!</div>'),
    # bg-remove labels
    ('<h4>원본</h4>', '<h4>Original</h4>'),
    ('<h4>결과 (투명 배경)</h4>', '<h4>Result (Transparent)</h4>'),
    ('<img id="originalPreview" alt="원본 이미지">', '<img id="originalPreview" alt="Original Image">'),
    ('<img id="resultPreview" alt="배경 제거 결과" style="display:block;">', '<img id="resultPreview" alt="Background Removed" style="display:block;">'),
    # add-text options
    ('<span>작게</span>', '<span>Small</span>'),
    ('<span>크게</span>', '<span>Large</span>'),
    ('<span>투명</span>', '<span>Transparent</span>'),
    ('<span>불투명</span>', '<span>Opaque</span>'),
    ('<button class="align-btn active" id="alignLeft"   onclick="setAlign(\'left\')">← 왼쪽</button>',
     '<button class="align-btn active" id="alignLeft"   onclick="setAlign(\'left\')">← Left</button>'),
    ('<button class="align-btn"        id="alignCenter" onclick="setAlign(\'center\')">가운데</button>',
     '<button class="align-btn"        id="alignCenter" onclick="setAlign(\'center\')">Center</button>'),
    ('<button class="align-btn"        id="alignRight"  onclick="setAlign(\'right\')">오른쪽 →</button>',
     '<button class="align-btn"        id="alignRight"  onclick="setAlign(\'right\')">Right →</button>'),
    ('<span>왼쪽</span>', '<span>Left</span>'),
    ('<span>오른쪽</span>', '<span>Right</span>'),
    ('<span>위</span>', '<span>Top</span>'),
    ('<span>아래</span>', '<span>Bottom</span>'),
    # font options
    ('<option value="Impact, sans-serif">Impact (굵게)</option>', '<option value="Impact, sans-serif">Impact (Bold)</option>'),
    ('<option value="\'Malgun Gothic\', sans-serif">맑은 고딕</option>', '<option value="\'Malgun Gothic\', sans-serif">Malgun Gothic</option>'),
    ('<option value="\'Dotum\', sans-serif">돋움</option>', '<option value="\'Dotum\', sans-serif">Dotum</option>'),
    ('<option value="\'Batang\', serif">바탕</option>', '<option value="\'Batang\', serif">Batang</option>'),
    # OCR panel
    ('<div class="panel-title">언어 선택</div>', '<div class="panel-title">Language</div>'),
    ('<button class="lang-btn active" data-lang="kor">🇰🇷 한국어</button>', '<button class="lang-btn active" data-lang="kor">🇰🇷 Korean</button>'),
    ('<button class="lang-btn" data-lang="eng">🇺🇸 영어</button>', '<button class="lang-btn" data-lang="eng">🇺🇸 English</button>'),
    ('<button class="lang-btn" data-lang="kor+eng">🌐 한국어 + 영어</button>', '<button class="lang-btn" data-lang="kor+eng">🌐 Korean + English</button>'),
    ('<div class="progress-status" id="progressStatus">초기화 중...</div>', '<div class="progress-status" id="progressStatus">Initializing...</div>'),
    ('<button class="btn-convert" id="startBtn">🔍 텍스트 인식 시작</button>', '<button class="btn-convert" id="startBtn">🔍 Start OCR</button>'),
    ('<button class="btn-copy" id="copyBtn" onclick="copyResult()">📋 복사</button>', '<button class="btn-copy" id="copyBtn" onclick="copyResult()">📋 Copy</button>'),
    # OCR-specific start button re-recognition
    ("document.getElementById('startBtn').textContent = '🔍 다시 인식';", "document.getElementById('startBtn').textContent = '🔍 Re-run OCR';"),
    # share btn
    ('<button class="btn-share" id="shareBtn" style="display:none;">📤 공유하기</button>',
     '<button class="btn-share" id="shareBtn" style="display:none;">📤 Share</button>'),
    # footer nav links - text only (paths are already changed by href replacement above)
    ('>전체 도구 ›<', '>All Tools ›<'),
    ('>이미지 압축<', '>Image Compressor<'),
    ('>리사이즈<', '>Resize<'),
    ('>회전/뒤집기<', '>Rotate/Flip<'),
    ('>자르기<', '>Crop<'),
    ('>소개<', '>About<'),
    ('>이미지 압축 도구 →<', '>Image Compressor →<'),
    ('>이미지 리사이즈 →<', '>Image Resizer →<'),
    # JS error messages
    ("showError('이미지 파일만 업로드할 수 있습니다.');", "showError('Please select an image file.');"),
    ("showError('JPG 또는 PNG 파일만 업로드할 수 있습니다.');", "showError('Please select a JPG or PNG file.');"),
    ("if (!file.type.match(/^image\\//)) { showError('이미지 파일만 업로드할 수 있습니다.'); return; }",
     "if (!file.type.match(/^image\\//)) { showError('Please select an image file.'); return; }"),
    # JS share alert
    ("alert('공유에 실패했습니다.');", "alert('Share failed.');"),
    ("text: 'WooaImage를 통해 변환한 파일입니다.\\nhttps://imagekit.wooahouse.com/",
     "text: 'Converted with WooaImage\\nhttps://imagekit.wooahouse.com/"),
    # JS template literals
    ("`${pct}% 절감`", '`${pct}% smaller`'),
    ("`${Math.abs(pct)}% 증가`", '`${Math.abs(pct)}% larger`'),
    # JS progress & button states
    ("document.getElementById('progressText').textContent = '이미지 로딩 중...';",
     "document.getElementById('progressText').textContent = 'Loading image...';"),
    ("document.getElementById('progressText').textContent = '이미지 준비 중...';",
     "document.getElementById('progressText').textContent = 'Preparing image...';"),
    ("document.getElementById('progressText').textContent = '이미지 합치는 중...';",
     "document.getElementById('progressText').textContent = 'Merging images...';"),
    ("document.getElementById('progressText').textContent = '완료!';",
     "document.getElementById('progressText').textContent = 'Done!';"),
    ("progressText.textContent = '완료!';", "progressText.textContent = 'Done!';"),
    ("setProgress(100, '완료!');", "setProgress(100, 'Done!');"),
    ("btn.textContent = '처리 중...';", "btn.textContent = 'Processing...';"),
    ("btn.disabled = true; btn.textContent = '⏳ 변환 중...';", "btn.disabled = true; btn.textContent = '⏳ Converting...';"),
    ("btn.disabled = true; btn.textContent = '⏳ 처리 중...';", "btn.disabled = true; btn.textContent = '⏳ Processing...';"),
    ("btn.textContent = '✅ 복사됨';", "btn.textContent = '✅ Copied!';"),
    ("setTimeout(() => { btn.textContent = '📋 복사'; btn.classList.remove('copied'); }, 2000);",
     "setTimeout(() => { btn.textContent = '📋 Copy'; btn.classList.remove('copied'); }, 2000);"),
    # bg-remove JS
    ("progressStatus.textContent = 'AI 모델 다운로드 중...';", "progressStatus.textContent = 'Downloading AI model...';"),
    ("progressStatus.textContent = '배경 제거 처리 중...';", "progressStatus.textContent = 'Removing background...';"),
    ("progressStatus.textContent = '완료!';", "progressStatus.textContent = 'Done!';"),
    ("document.getElementById('resultSubtitle').textContent = `결과 크기: ${formatSize(blob.size)}`;",
     "document.getElementById('resultSubtitle').textContent = `Result Size: ${formatSize(blob.size)}`;"),
    # share comment
    ('// 공유하기', '// share'),
    ('// 드롭존', '// dropzone'),
    ('// 언어 버튼', '// language buttons'),
    ('// AI 라이브러리와 분리 — 파일 UI는 즉시 동작', '// AI lib is loaded separately — file UI works immediately'),
    ('// 버튼 클릭 시점에 동적으로 import', '// dynamically import on button click'),
    # about.html specific
    ('<meta property="og:title" content="서비스 소개 | WooaImage">',
     '<meta property="og:title" content="About WooaImage – Free Online Image Tools">'),
    ('<meta property="og:description" content="이미지 압축, 변환, 편집을 무료로 제공하는 WooaImage 서비스 소개입니다.">',
     '<meta property="og:description" content="WooaImage is a free online image toolkit for compressing, converting, and editing images in your browser.">'),
    ('<li>이미지 리사이즈 — Pixels 또는 비율로 크기 조정</li>', '<li>Image Resize — resize by pixels or percentage</li>'),
    ('<li>이미지 정보 확인 — Resolution, File Size, 형식 등</li>', '<li>Image Info — view resolution, file size, format, and more</li>'),
    # add-text apply button
    ('<button class="btn-convert" id="applyBtn">✍️ 텍스트 적용 &amp; 저장 준비</button>',
     '<button class="btn-convert" id="applyBtn">✍️ Apply Text &amp; Prepare Download</button>'),
    ('btn.disabled = false; btn.textContent = \'✍️ 텍스트 적용 & 저장 준비\';',
     'btn.disabled = false; btn.textContent = \'✍️ Apply Text & Prepare Download\';'),
    # bg-remove warning text
    ('⚠️ <strong>첫 실행 시 AI 모델 다운로드에 약 30초가 소요됩니다.</strong> 이후에는 캐시되어 빠르게 처리됩니다. 모든 처리는 브라우저에서 이루어지며 서버로 파일이 전송되지 않습니다.',
     '⚠️ <strong>The first run downloads the AI model (~30 seconds).</strong> After that it\'s cached for fast processing. All processing happens in your browser — files are never sent to a server.'),
    # output format for svg/png-to-ico
    ('<span class="option-label">출력 형식</span>', '<span class="option-label">Output Format</span>'),
    ('<span class="option-label">미리보기</span>', '<span class="option-label">Preview</span>'),
    ('<span class="option-label">배경색</span>', '<span class="option-label">Background Color</span>'),
    ('<span class="option-label">글자 색상</span>', '<span class="option-label">Text Color</span>'),
    # cross-link spans not already covered
    ('<span>이미지 → WebP<br>변환</span>', '<span>Image<br>→ WebP</span>'),
    # span size labels
    ('<span>원본</span>', '<span>Original</span>'),
    # result subtitle placeholder
    ("document.getElementById('resultSubtitle').textContent = `결과 크기:", "document.getElementById('resultSubtitle').textContent = `Result Size:"),
    # ── index.html: mixed partial-translation fixes ──
    ('<div class="tool-desc">여러 사진을 하나로 합치기, Select Layout</div>',
     '<div class="tool-desc">Combine multiple photos into one collage with layout options</div>'),
    ('<div class="tool-desc">File Name, 크기, Resolution, EXIF 정보 확인</div>',
     '<div class="tool-desc">View file name, size, resolution, and EXIF info</div>'),
    ('Files never sent to server. 모든 처리가 브라우저 안에서 이루어집니다.',
     'Files are never sent to a server. All processing happens in your browser.'),
    ('<a href="image-info.html">이미지 정보</a>', '<a href="../image-info.html">Image Info</a>'),
    ('<a href="ocr-image.html">이미지 텍스트 추출</a>', '<a href="../ocr-image.html">Image OCR</a>'),
    ('<a href="ocr-pdf.html">PDF 텍스트 추출</a>', '<a href="../ocr-pdf.html">PDF OCR</a>'),
    ('<h4>정보</h4>', '<h4>Info</h4>'),
    ('<a href="../about.html">서비스 소개</a>', '<a href="../about.html">About</a>'),
    ('<h4>WooaHouse 서비스</h4>', '<h4>WooaHouse Services</h4>'),
    # ── about.html ──
    ('>홈<', '>Home<'),
    # ── add-text-image.html ──
    ('<span class="option-label">텍스트 내용</span>', '<span class="option-label">Text Content</span>'),
    ('placeholder="여기에 입력하세요"', 'placeholder="Enter text here"'),
    ('<span class="option-label">폰트</span>', '<span class="option-label">Font</span>'),
    ('<span class="option-label">정렬</span>', '<span class="option-label">Alignment</span>'),
    ('<span class="option-label">수평 위치</span>', '<span class="option-label">Horizontal Position</span>'),
    ('<span class="option-label">수직 위치</span>', '<span class="option-label">Vertical Position</span>'),
    # ── bg-remove.html ──
    ("showError('배경 제거 중 오류가 발생했습니다: ' + err.message);", "showError('Background removal failed: ' + err.message);"),
    ("btn.textContent = '🤖 배경 제거 시작';", "btn.textContent = '🤖 Remove Background';"),
    # ── collage-image.html ──
    ('<span>좌우 2장</span>', '<span>2 Side by Side</span>'),
    ('<span>상하 2장</span>', '<span>2 Top/Bottom</span>'),
    ('<span>좌우 3장</span>', '<span>3 Side by Side</span>'),
    ('<span>상하 3장</span>', '<span>3 Top/Bottom</span>'),
    ('<span>2×2 격자</span>', '<span>2×2 Grid</span>'),
    ('<span>좌우 4장</span>', '<span>4 Side by Side</span>'),
    ('<div class="options-title" style="margin-top:16px;">이미지 슬롯</div>', '<div class="options-title" style="margin-top:16px;">Image Slots</div>'),
    ('<span class="option-label">캔버스 너비</span>', '<span class="option-label">Canvas Width</span>'),
    ('<span class="option-label">간격 (px)</span>', '<span class="option-label">Spacing (px)</span>'),
    ('>🎨 미리보기 생성<', '>🎨 Generate Preview<'),
    ('>⬇️ 콜라주 다운로드<', '>⬇️ Download Collage<'),
    ('클릭하여<br>이미지 추가', 'Click to<br>add image'),
    ("showError('최소 한 장 이상의 이미지를 추가해주세요.'); return;", "showError('Please add at least one image.'); return;"),
    ("ctx.fillText('이미지 없음',", "ctx.fillText('No Image',"),
    # ── compress-image.html ──
    ('alt="압축된 이미지 미리보기"', 'alt="Compressed Image Preview"'),
    ('`이미 최적화된 이미지입니다.`', '`Image is already optimized.`'),
    ("'이미 최적화된 이미지입니다.'", "'Image is already optimized.'"),
    ("`${ratio}% 감소`", '`${ratio}% smaller`'),
    # ── crop-image.html ──
    ('<div class="options-title">크롭 설정</div>', '<div class="options-title">Crop Settings</div>'),
    ('<p style="font-size:0.85rem; color:var(--text-light); margin-bottom:16px;">원본 이미지에서 자를 영역을 Pixels 좌표로 입력하세요.</p>',
     '<p style="font-size:0.85rem; color:var(--text-light); margin-bottom:16px;">Enter the area to crop from the original image in pixel coordinates.</p>'),
    ('<label>X 시작 (px)</label>', '<label>X Start (px)</label>'),
    ('<label>Y 시작 (px)</label>', '<label>Y Start (px)</label>'),
    ('<label>너비 (px)</label>', '<label>Width (px)</label>'),
    ('<label>높이 (px)</label>', '<label>Height (px)</label>'),
    ('>✂️ 자르기 실행<', '>✂️ Apply Crop<'),
    ('<div class="result-title">자르기 완료!</div>', '<div class="result-title">Cropped!</div>'),
    ('alt="잘라낸 이미지 미리보기"', 'alt="Cropped Image Preview"'),
    ("`크롭 영역: ${x}, ${y} ~ ${x+w}×${y+h} px`", '`Crop Area: ${x}, ${y} ~ ${x+w}×${y+h} px`'),
    ("showError('유효한 크롭 영역을 입력하세요.'); return;", "showError('Please enter a valid crop area.'); return;"),
    # ── exif-remove.html ──
    ('ℹ️ <strong>EXIF란?</strong> 스마트폰·카메라로 찍은 사진에 자동 저장되는 메타데이터입니다. GPS 위치, 촬영일시, 카메라 기종 등이 포함되어 있어 SNS 업로드 전 삭제를 권장합니다.',
     'ℹ️ <strong>What is EXIF?</strong> Metadata automatically saved in photos taken by smartphones and cameras. It includes GPS location, date/time, and camera model — recommended to remove before sharing on social media.'),
    ('<div style="font-weight:600; font-size:0.95rem; margin-bottom:8px;">📋 감지된 EXIF 정보</div>',
     '<div style="font-weight:600; font-size:0.95rem; margin-bottom:8px;">📋 Detected EXIF Data</div>'),
    ('>🔒 EXIF 제거 & 저장 준비<', '>🔒 Remove EXIF & Prepare Download<'),
    ('<div class="result-title">EXIF 제거 완료!</div>', '<div class="result-title">EXIF Removed!</div>'),
    ('alt="EXIF 제거된 이미지" style="max-width:100%;border-radius:8px;">', 'alt="Image with EXIF Removed" style="max-width:100%;border-radius:8px;">'),
    ('>⬇️ EXIF 제거된 이미지 다운로드<', '>⬇️ Download Image (EXIF Removed)<'),
    ("0x010F: '카메라 제조사', 0x0110: '카메라 기종', 0x0112: '방향',",
     "0x010F: 'Camera Make', 0x0110: 'Camera Model', 0x0112: 'Orientation',"),
    ("0x011A: 'X Resolution', 0x011B: 'Y Resolution', 0x0128: 'Resolution 단위',",
     "0x011A: 'X Resolution', 0x011B: 'Y Resolution', 0x0128: 'Resolution Unit',"),
    ("0x0131: '소프트웨어', 0x0132: '수정일시', 0x013B: '작가',",
     "0x0131: 'Software', 0x0132: 'Date Modified', 0x013B: 'Artist',"),
    ("0x8298: '저작권', 0x8769: 'EXIF IFD',",
     "0x8298: 'Copyright', 0x8769: 'EXIF IFD',"),
    ("0x9003: '원본 촬영일시', 0x9004: '디지털 변환일시',",
     "0x9003: 'Original Date', 0x9004: 'Digitized Date',"),
    ("0x9286: '사용자 설명', 0x9c9b: '제목',",
     "0x9286: 'User Comment', 0x9c9b: 'Title',"),
    ("0x0213: 'YCbCr 위치', 0xA005: 'Interop IFD'",
     "0x0213: 'YCbCr Positioning', 0xA005: 'Interop IFD'"),
    ("0: 'GPS 버전', 1: 'GPS 위도 방향', 2: 'GPS 위도',",
     "0: 'GPS Version', 1: 'GPS Latitude Ref', 2: 'GPS Latitude',"),
    ("3: 'GPS 경도 방향', 4: 'GPS 경도', 5: 'GPS 고도 기준',",
     "3: 'GPS Longitude Ref', 4: 'GPS Longitude', 5: 'GPS Altitude Ref',"),
    ("6: 'GPS 고도', 7: 'GPS 시간', 29: 'GPS 날짜'",
     "6: 'GPS Altitude', 7: 'GPS Time', 29: 'GPS Date'"),
    ("let val = '(포함됨)';", "let val = '(included)';"),
    ("if (gpsTagNames[gTag]) tags[gpsTagNames[gTag]] = '(포함됨)';",
     "if (gpsTagNames[gTag]) tags[gpsTagNames[gTag]] = '(included)';"),
    ("'✅ EXIF 정보가 감지되지 않았습니다. (PNG이거나 이미 제거된 파일)'",
     "'✅ No EXIF data detected. (PNG or already cleaned file)'"),
    # ── heic-to-jpg.html ──
    ('📱 아이폰/iPad에서 촬영한 HEIC(HEIF) 파일을 지원합니다. 여러 파일을 동시에 선택하여 일괄 변환이 가능합니다.',
     '📱 Supports HEIC/HEIF files from iPhone/iPad. Select multiple files for batch conversion.'),
    ('<p>.heic, .heif 파일을 업로드하세요 (여러 파일 가능)</p>', '<p>Upload .heic or .heif files (multiple files supported)</p>'),
    ('<div class="file-list-title">Selected File (<span id="fileCount">0</span>개)</div>',
     '<div class="file-list-title">Selected Files (<span id="fileCount">0</span>)</div>'),
    ('>⬇️ 모두 다운로드 (ZIP)<', '>⬇️ Download All (ZIP)<'),
    ("// label 클릭 시 이미 fileInput이 열리므로 dropZone 클릭 시 label/input 제외", '// label click already opens fileInput; exclude label/input from dropZone click'),
    ("fileInput.value = ''; // 같은 파일 재선택 가능하게 초기화", "fileInput.value = ''; // reset to allow re-selecting the same file"),
    ("// 중복 제거 (이름+크기 기준)", '// de-duplicate by name+size'),
    ("`${i+1}/${selectedFiles.length} 변환 중...`", '`${i+1}/${selectedFiles.length} converting...`'),
    ('<span class="converted-status status-done">완료</span>', '<span class="converted-status status-done">Done</span>'),
    ('<button class="btn-download-sm" onclick="downloadSingle(', '<button class="btn-download-sm" onclick="downloadSingle('),
    ("'다운로드'", "'Download'"),
    ("|| '변환 실패'", "|| 'Conversion failed'"),
    ('<span class="converted-status status-error">실패</span>', '<span class="converted-status status-error">Failed</span>'),
    ("`${successCount}/${selectedFiles.length}개 파일 변환 완료`", '`${successCount}/${selectedFiles.length} files converted`'),
    ("btn.textContent = 'ZIP 생성 중...';", "btn.textContent = 'Creating ZIP...';"),
    # ── image-border.html ──
    ("onclick=\"setBorderColor('#ffffff')\" style=\"padding:4px 10px; border:1px solid #d1d5db; border-radius:6px; backgr",
     "onclick=\"setBorderColor('#ffffff')\" style=\"padding:4px 10px; border:1px solid #d1d5db; border-radius:6px; backgr"),
    ('<span class="option-label">모서리 둥글기</span>', '<span class="option-label">Corner Radius</span>'),
    ('<span class="option-label">그림자 효과</span>', '<span class="option-label">Shadow Effect</span>'),
    ('<span>그림자 추가</span>', '<span>Add Shadow</span>'),
    ('<span class="option-label">그림자 색상</span>', '<span class="option-label">Shadow Color</span>'),
    ('<span class="option-label">그림자 강도</span>', '<span class="option-label">Shadow Intensity</span>'),
    ('<option value="image/png">PNG (투명 지원)</option>', '<option value="image/png">PNG (supports transparency)</option>'),
    ('>🎨 미리보기<', '>🎨 Preview<'),
    # ── image-filter.html ──
    ('<span>필터 설정</span>', '<span>Filter Settings</span>'),
    ('>↺ 초기화<', '>↺ Reset<'),
    ('<span class="filter-label">☀️ 밝기</span>', '<span class="filter-label">☀️ Brightness</span>'),
    ('<span class="filter-label">🌓 대비</span>', '<span class="filter-label">🌓 Contrast</span>'),
    ('<span class="filter-label">🌈 채도</span>', '<span class="filter-label">🌈 Saturation</span>'),
    ('<span class="filter-label">🎨 색조</span>', '<span class="filter-label">🎨 Hue</span>'),
    ('<span class="filter-label">⬛ 흑백</span>', '<span class="filter-label">⬛ Grayscale</span>'),
    ('<span class="filter-label">🟫 세피아</span>', '<span class="filter-label">🟫 Sepia</span>'),
    ('<span class="filter-label">💨 블러</span>', '<span class="filter-label">💨 Blur</span>'),
    ('<span class="filter-label">✨ 선명도</span>', '<span class="filter-label">✨ Sharpness</span>'),
    ('alt="원본 이미지">', 'alt="Original Image">'),
    ('<span>미리보기</span>', '<span>Preview</span>'),
    ('alt="필터 적용 미리보기">', 'alt="Filtered Preview">'),
    ('>🎨 필터 적용 & 저장 준비<', '>🎨 Apply Filter & Prepare Download<'),
    ('<div class="result-title">필터 적용 완료!</div>', '<div class="result-title">Filter Applied!</div>'),
    ('alt="필터 적용된 이미지">', 'alt="Filtered Image">'),
    ("btn.textContent = '🎨 필터 적용 & 저장 준비';", "btn.textContent = '🎨 Apply Filter & Prepare Download';"),
    # ── image-info.html ──
    ('<div class="options-title">이미지 정보</div>', '<div class="options-title">Image Information</div>'),
    ('alt="미리보기">', 'alt="Preview">'),
    (">✕ 초기화<", ">✕ Clear<"),
    ("const fmt = typeMap[file.type] || file.type || '알 수 없음';", "const fmt = typeMap[file.type] || file.type || 'Unknown';"),
    ("['📐 이미지 크기',", "['📐 Image Size',"),
    ("['📊 메가Pixels',", "['📊 Megapixels',"),
    ("['⬜ 가로세로 비율',", "['⬜ Aspect Ratio',"),
    ("['🏷️ MIME 타입',", "['🏷️ MIME Type',"),
    ("['📅 마지막 수정일',", "['📅 Last Modified',"),
    # ── image-to-base64.html ──
    ('<div class="options-title">변환 결과</div>', '<div class="options-title">Conversion Result</div>'),
    ('alt="미리보기" class="preview-img"', 'alt="Preview" class="preview-img"'),
    ('class="preview-img" alt="미리보기"', 'class="preview-img" alt="Preview"'),
    ('<span class="copy-success" id="copySuccess">✅ 복사됨!</span>', '<span class="copy-success" id="copySuccess">✅ Copied!</span>'),
    ("`<strong>원본 크기:</strong>", "`<strong>Original Size:</strong>"),
    ("`<strong>Data URL 길이:</strong> ${dataUrl.length.toLocaleString()} 자`",
     "`<strong>Data URL Length:</strong> ${dataUrl.length.toLocaleString()} chars`"),
    # ── jpg-to-png.html ──
    ('<p>JPG, JPEG 파일을 업로드하세요</p>', '<p>Upload a JPG or JPEG file</p>'),
    ('ℹ️ JPG는 투명도를 지원하지 않습니다. PNG로 변환하면 이후 편집에서 투명 영역을 활용할 수 있습니다.',
     'ℹ️ JPG does not support transparency. Converting to PNG lets you use transparent areas in future edits.'),
    ('>🔄 PNG로 변환<', '>🔄 Convert to PNG<'),
    ('alt="변환된 PNG 이미지 미리보기">', 'alt="Converted PNG Preview">'),
    ('>⬇️ PNG 다운로드<', '>⬇️ Download PNG<'),
    ('반대로 변환하고 싶으신가요? <a href="png-to-jpg.html">PNG → JPG 변환 →</a>',
     'Want to convert the other way? <a href="../png-to-jpg.html">PNG → JPG →</a>'),
    ("showError('JPG/JPEG 파일만 업로드할 수 있습니다.'); return;", "showError('Please select a JPG or JPEG file.'); return;"),
    ("btn.textContent = '🔄 PNG로 변환';", "btn.textContent = '🔄 Convert to PNG';"),
    # ── make-gif.html ──
    ('<p>JPG, PNG, WebP 파일 여러 장을 업로드하세요</p>', '<p>Upload multiple JPG, PNG, or WebP files</p>'),
    ('<div class="file-list-title">프레임 (<span id="frameCount">0</span>개) — 드래그하여 순서 변경</div>',
     '<div class="file-list-title">Frames (<span id="frameCount">0</span>) — drag to reorder</div>'),
    ('<span class="option-label">프레임 딜레이: <strong id="delayVal">500</strong>ms</span>',
     '<span class="option-label">Frame Delay: <strong id="delayVal">500</strong>ms</span>'),
    ('<label class="radio-item"><input type="radio" name="repeat" value="0" checked> 무한 Loop</label>',
     '<label class="radio-item"><input type="radio" name="repeat" value="0" checked> Infinite Loop</label>'),
    ('<label class="radio-item"><input type="radio" name="repeat" value="1"> 1회</label>',
     '<label class="radio-item"><input type="radio" name="repeat" value="1"> Once</label>'),
    ('<label class="radio-item"><input type="radio" name="repeat" value="custom"> 지정</label>',
     '<label class="radio-item"><input type="radio" name="repeat" value="custom"> Custom</label>'),
    ('<label class="radio-item"><input type="radio" name="sizeMode" value="original" checked> 원본 크기</label>',
     '<label class="radio-item"><input type="radio" name="sizeMode" value="original" checked> Original Size</label>'),
    ('<label class="radio-item"><input type="radio" name="sizeMode" value="custom"> 너비 지정</label>',
     '<label class="radio-item"><input type="radio" name="sizeMode" value="custom"> Custom Width</label>'),
    ('<span class="option-label">너비 (px)</span>', '<span class="option-label">Width (px)</span>'),
    ('>🎬 GIF 생성<', '>🎬 Generate GIF<'),
    ('<span id="progressText">GIF 생성 중...</span>', '<span id="progressText">Generating GIF...</span>'),
    ('<div class="result-title">GIF 생성 완료!</div>', '<div class="result-title">GIF Created!</div>'),
    ('alt="생성된 GIF">', 'alt="Generated GIF">'),
    ("title=\"삭제\"", 'title="Remove"'),
    # ── merge-image.html ──
    ('<p>JPG, PNG, WebP — 최대 10장</p>', '<p>JPG, PNG, WebP — up to 10 images</p>'),
    ('<span class="option-label">방향</span>', '<span class="option-label">Direction</span>'),
    (">↔️ 가로로 이어붙이기<", ">↔️ Horizontal<"),
    (">↕️ 세로로 이어붙이기<", ">↕️ Vertical<"),
    ('<span class="option-label">이미지 간격</span>', '<span class="option-label">Image Spacing</span>'),
    ('<span>없음</span>', '<span>None</span>'),
    ('<span>넓게</span>', '<span>Wide</span>'),
    ('<span style="font-size:0.88rem;color:var(--text-light);">간격 및 여백에 채울 배경색</span>',
     '<span style="font-size:0.88rem;color:var(--text-light);">Background color for spacing and margins</span>'),
    ('>🔗 이미지 합치기<', '>🔗 Merge Images<'),
    ('<span id="progressText">합치는 중...</span>', '<span id="progressText">Merging...</span>'),
    ('<div class="result-title">이미지 합치기 완료!</div>', '<div class="result-title">Merged!</div>'),
    ('alt="합쳐진 이미지 미리보기" style="max-width:100%;border-radius:8px;">', 'alt="Merged Image Preview" style="max-width:100%;border-radius:8px;">'),
    ('>⬇️ 합쳐진 이미지 다운로드<', '>⬇️ Download Merged Image<'),
    # ── mosaic-image.html ──
    ('<span class="option-label">적용 모드</span>', '<span class="option-label">Mode</span>'),
    (">🟫 전체 모자이크<", ">🟫 Full Image Mosaic<"),
    (">🖱️ 영역 선택 모자이크<", ">🖱️ Region Mosaic<"),
    ('<span>약함</span>', '<span>Light</span>'),
    ('<span>강함</span>', '<span>Strong</span>'),
    ('<span class="option-label">영역 선택</span>', '<span class="option-label">Select Region</span>'),
    ('<p class="canvas-hint">드래그하여 모자이크를 적용할 영역을 선택하세요</p>',
     '<p class="canvas-hint">Drag to select the region to apply mosaic</p>'),
    ('>✅ 선택 영역 Apply Mosaic<', '>✅ Apply Mosaic to Selection<'),
    ('>🟫 전체 Apply Mosaic<', '>🟫 Apply Mosaic to Entire Image<'),
    ('<div class="result-title">Apply Mosaic 완료!</div>', '<div class="result-title">Mosaic Applied!</div>'),
    ('alt="Apply Mosaic 이미지" style="max-width:100%;border-radius:8px;">', 'alt="Mosaic Applied Image" style="max-width:100%;border-radius:8px;">'),
    ('>⬇️ 모자이크 이미지 다운로드<', '>⬇️ Download Mosaic Image<'),
    ("'🟫 전체 Apply Mosaic'", "'🟫 Apply Full Mosaic'"),
    ("'🟫 Apply Mosaic'", "'🟫 Apply Mosaic'"),
    # ── ocr-image.html ──
    ('<p>사진, 스크린샷, 스캔 문서에서 텍스트를 인식하여 복사할 수 있게 추출합니다.<br>한국어, 영어, 한영 혼용을 지원합니다.</p>',
     '<p>Extract text from photos, screenshots, and scanned documents.<br>Supports Korean, English, and mixed text.</p>'),
    ('<p>JPG, PNG, WebP, BMP, GIF 파일 지원</p>', '<p>Supports JPG, PNG, WebP, BMP, GIF files</p>'),
    ('alt="선택된 이미지">', 'alt="Selected Image">'),
    ('<div class="panel-title">텍스트 인식 중…</div>', '<div class="panel-title">Recognizing text…</div>'),
    ('<div class="panel-title" style="margin-bottom:0;">인식 결과</div>', '<div class="panel-title" style="margin-bottom:0;">Recognition Result</div>'),
    ('placeholder="인식된 텍스트가 여기에 표시됩니다."', 'placeholder="Recognized text will appear here."'),
    ('<strong>⚠️ OCR 정확도 안내</strong>',
     '<strong>⚠️ OCR Accuracy Notes</strong>'),
    ('• 인쇄된 문자가 선명할수록 인식률이 높습니다', '• Cleaner printed text yields higher accuracy'),
    ('• 손글씨, 기울어진 텍스트, 복잡한 배경은 인식률이 낮을 수 있습니다',
     '• Handwriting, skewed text, and complex backgrounds may reduce accuracy'),
    ('• 첫 실행 시 언어 데이터를 다운로드하므로 잠시 기다려주세요 (한국어 약 10MB)',
     '• The first run downloads language data — please wait (~10MB for Korean)'),
    ('• 모든 처리는 브라우저에서 이루어지며 Files never sent to server',
     '• All processing happens in your browser — files are never sent to a server'),
    ('<div class="panel-title">잘 되는 경우 vs 어려운 경우</div>',
     '<div class="panel-title">Works Well vs. Difficult Cases</div>'),
    ('<div style="font-size:0.85rem; font-weight:700; color:#059669; margin-bottom:8px;">✅ 잘 인식되는 경우</div>',
     '<div style="font-size:0.85rem; font-weight:700; color:#059669; margin-bottom:8px;">✅ Works Well</div>'),
    ('<li>스크린샷 속 텍스트</li>', '<li>Text in screenshots</li>'),
    ('<li>선명하게 인쇄된 문서</li>', '<li>Clearly printed documents</li>'),
    ('<li>흰 배경의 검은 글씨</li>', '<li>Black text on white background</li>'),
    ('<li>명함, 영수증 (인쇄체)</li>', '<li>Business cards, receipts (printed)</li>'),
    ('<div style="font-size:0.85rem; font-weight:700; color:#DC2626; margin-bottom:8px;">❌ 어려운 경우</div>',
     '<div style="font-size:0.85rem; font-weight:700; color:#DC2626; margin-bottom:8px;">❌ Difficult Cases</div>'),
    ('<li>손글씨</li>', '<li>Handwriting</li>'),
    ('<li>기울어진 텍스트</li>', '<li>Skewed or rotated text</li>'),
    ('<li>복잡한 배경</li>', '<li>Complex backgrounds</li>'),
    ('<li>아주 작은 글씨</li>', '<li>Very small text</li>'),
    # ── ocr-pdf.html ──
    ('<a href="ocr-image.html">이미지 OCR</a>', '<a href="../ocr-image.html">Image OCR</a>'),
    ('<p>스캔된 PDF나 이미지로 된 PDF에서 텍스트를 인식하여 추출합니다.<br>한국어, 영어, 한영 혼용을 지원합니다.</p>',
     '<p>Extract text from scanned PDFs or image-based PDFs.<br>Supports Korean, English, and mixed text.</p>'),
    ('<strong>💡 일반 PDF vs 스캔 PDF</strong>',
     '<strong>💡 Regular PDF vs Scanned PDF</strong>'),
    ('• <strong>일반 PDF(텍스트 선택 가능)</strong>', '• <strong>Regular PDF (text selectable)</strong>'),
    ('• <strong>스캔 PDF(이미지로 구성된 PDF)</strong> → 이 도구가 OCR로 텍스트를 인식합니다',
     '• <strong>Scanned PDF (image-based)</strong> → This tool uses OCR to recognize text'),
    ('<p>스캔 PDF 또는 이미지로 구성된 PDF 파일</p>', '<p>Scanned PDF or image-based PDF file</p>'),
    ('<span id="pdfFileMeta">크기 · 페이지 수 로딩 중...</span>', '<span id="pdfFileMeta">Loading size & page count...</span>'),
    (">✕ 변경<", ">✕ Change<"),
    ('<div class="panel-title" id="progressTitle">PDF 분석 중…</div>',
     '<div class="panel-title" id="progressTitle">Analyzing PDF…</div>'),
    (">전체 결과<", ">Full Result<"),
    (">페이지별 결과<", ">By Page<"),
    ('<div class="panel-title" style="margin-bottom:0;">전체 텍스트</div>',
     '<div class="panel-title" style="margin-bottom:0;">Full Text</div>'),
    ('>⬇️ TXT 저장<', '>⬇️ Save as TXT<'),
    ('placeholder="인식된 전체 텍스트가 여기에 표시됩니다."',
     'placeholder="Full recognized text will appear here."'),
    ('<strong>⚠️ 안내</strong>', '<strong>⚠️ Notes</strong>'),
    # ── png-to-ico.html ──
    ('ℹ️ <strong>파비콘 팁:</strong> 웹사이트 파비콘은 <strong>16×16, 32×32</strong>를 기본으로 포함하는 것을 권장합니다. 정사각형 이미지일수록 최상의 결과를 얻을 수 있습니다.',
     'ℹ️ <strong>Favicon Tip:</strong> For website favicons, it is recommended to include <strong>16×16 and 32×32</strong> sizes. Square images give the best results.'),
    ('<p>PNG, JPG 파일을 업로드하세요 (정사각형 권장)</p>', '<p>Upload a PNG or JPG file (square recommended)</p>'),
    ('<div class="options-title">ICO 크기 설정</div>', '<div class="options-title">ICO Size Settings</div>'),
    ('<span class="option-label">포함할 크기 선택</span>', '<span class="option-label">Select Sizes to Include</span>'),
    ('>🏷️ ICO 변환 시작<', '>🏷️ Convert to ICO<'),
    ('<div class="result-title">ICO 변환 완료!</div>', '<div class="result-title">ICO Created!</div>'),
    ('>⬇️ ICO 파일 다운로드<', '>⬇️ Download ICO File<'),
    ("showError('크기를 하나 이상 선택해 주세요.'); return;", "showError('Please select at least one size.'); return;"),
    ("document.getElementById('progressText').textContent = 'ICO 파일 생성 중...';",
     "document.getElementById('progressText').textContent = 'Creating ICO file...';"),
    ("'px 크기 포함 · '", "'px sizes included · '"),
    ("`${sizes.join(', ')}px 크기 포함 · ${formatSize(icoBlob.size)}`",
     "`${sizes.join(', ')}px sizes included · ${formatSize(icoBlob.size)}`"),
    ("showError('변환 중 오류가 발생했습니다: ' + err.message);", "showError('Conversion error: ' + err.message);"),
    ("btn.textContent = '🏷️ ICO 변환 시작';", "btn.textContent = '🏷️ Convert to ICO';"),
    # ── png-to-jpg.html ──
    ('<p>PNG 파일을 업로드하세요 (다른 이미지 형식도 가능)</p>', '<p>Upload a PNG file (other image formats also accepted)</p>'),
    ('<span class="option-label">투명 배경색</span>', '<span class="option-label">Background Color for Transparency</span>'),
    ('>⬇️ JPG로 다운로드<', '>⬇️ Download as JPG<'),
    # ── resize-image.html ──
    ('<div class="options-title">크기 조정 설정</div>', '<div class="options-title">Resize Settings</div>'),
    ('<p class="orig-info" id="origInfo">원본: — × —</p>', '<p class="orig-info" id="origInfo">Original: — × —</p>'),
    ('<label>가로 (px)</label>', '<label>Width (px)</label>'),
    ('<input type="number" id="newWidth" min="1" placeholder="너비">', '<input type="number" id="newWidth" min="1" placeholder="width">'),
    ('<label>세로 (px)</label>', '<label>Height (px)</label>'),
    ('<input type="number" id="newHeight" min="1" placeholder="높이">', '<input type="number" id="newHeight" min="1" placeholder="height">'),
    ('<input type="number" id="scalePercent" min="1" max="500" value="50" placeholder="예: 50">',
     '<input type="number" id="scalePercent" min="1" max="500" value="50" placeholder="e.g. 50">'),
    ('>📐 크기 조정 시작<', '>📐 Resize<'),
    ('<div class="result-title">리사이즈 완료!</div>', '<div class="result-title">Resized!</div>'),
    ('alt="리사이즈된 이미지 미리보기">', 'alt="Resized Image Preview">'),
    ("`원본: ${origImg.naturalWidth} × ${origImg.naturalHeight} px`",
     '`Original: ${origImg.naturalWidth} × ${origImg.naturalHeight} px`'),
    ("showError('올바른 크기를 입력하세요.'); return;", "showError('Please enter a valid size.'); return;"),
    ("btn.textContent = '📐 크기 조정 시작';", "btn.textContent = '📐 Resize';"),
    # ── rotate-image.html ──
    (">↩️ 왼쪽 90°<", ">↩️ 90° Left<"),
    (">↪️ 오른쪽 90°<", ">↪️ 90° Right<"),
    (">↔️ 좌우 뒤집기<", ">↔️ Flip Horizontal<"),
    (">↕️ 상하 뒤집기<", ">↕️ Flip Vertical<"),
    # ── svg-to-png.html ──
    ('<p>SVG 파일을 업로드하세요</p>', '<p>Upload an SVG file</p>'),
    ('<span class="option-label">배율 (배수)</span>', '<span class="option-label">Scale (multiplier)</span>'),
    # ── upscale-image.html ──
    ('<span class="option-label">업스케일 배율</span>', '<span class="option-label">Upscale Factor</span>'),
    # ── watermark-image.html ──
    ('<p>워터마크를 넣을 이미지를 선택하세요</p>', '<p>Select the image to add a watermark to</p>'),
    # ── split-image.html ──
    ('<div class="options-title">분할 설정</div>', '<div class="options-title">Split Settings</div>'),
    # ── round-corner.html ──
    ('<div class="options-title">둥근 모서리 설정</div>', '<div class="options-title">Rounded Corner Settings</div>'),
    # ── privacy.html ──
    ('<meta name="description" content="WooaImage 개인정보처리방침입니다.">',
     '<meta name="description" content="Privacy policy for WooaImage – free online image tools.">'),
    ('<p class="updated">최종 업데이트: 2026년 3월 15일</p>', '<p class="updated">Last updated: March 15, 2026</p>'),
    ('<h2>1. 개인정보 수집 여부</h2>', '<h2>1. Collection of Personal Information</h2>'),
    ('WooaImage(imagekit.wooahouse.com)은 회원가입, 로그인 등의 기능이 없으며, 사용자의 개인정보를 직접 수집하지 않습니다. 본 서비스는 정적 웹사이트로 운영되며 서버 측에서 별도의 데이터',
     'WooaImage (imagekit.wooahouse.com) has no sign-up or login features and does not directly collect personal information. This service is a static website with no server-side data'),
    ('모든 이미지 처리는 사용자의 브라우저 내에서 Canvas API를 통해 이루어지며, 업로드된 이미지 파일은 서버에 전송되지 않습니다.',
     'All image processing is performed locally in your browser via the Canvas API. Uploaded image files are never sent to a server.'),
    ('<h2>2. 제3자 서비스</h2>', '<h2>2. Third-Party Services</h2>'),
    ('WooaImage은 아래 제3자 서비스를 사용하며, 각 서비스의 개인정보 처리방침이 적용됩니다.',
     'WooaImage uses the following third-party services, each governed by their own privacy policy.'),
    ('<li><strong>Google AdSense:</strong> 광고 게재를 위해 사용됩니다. Google은 쿠키를 통해 광고 관련 정보를 수집할 수 있습니다.</li>',
     '<li><strong>Google AdSense:</strong> Used for displaying advertisements. Google may collect ad-related information via cookies.</li>'),
    ('<li><strong>Google Analytics (해당 시):</strong> 익명화된 방문 통계 수집에 사용될 수 있습니다.</li>',
     '<li><strong>Google Analytics (if applicable):</strong> May be used to collect anonymized visit statistics.</li>'),
    ('<h2>3. 쿠키</h2>', '<h2>3. Cookies</h2>'),
    ('WooaImage은 자체적으로 쿠키를 사용하지 않습니다. 다만 Google AdSense 등 제3자 서비스에서 광고 목적으로 쿠키를 사용할 수 있습니다. 브라우저 설정에서 쿠키를 비활성화할 수 있습니다.',
     'WooaImage does not use cookies on its own. However, third-party services such as Google AdSense may use cookies for advertising purposes. You can disable cookies in your browser settings.'),
    ('<h2>4. 이미지 파일 처리</h2>', '<h2>4. Image File Processing</h2>'),
    ('WooaImage에서 처리되는 모든 이미지 파일은 사용자의 로컬 브라우저 내에서만 처리됩니다. 이미지 파일은 서버로 전송되지 않으며, 처리 완료 후 브라우저 메모리에서 삭제됩니다.',
     'All image files processed by WooaImage are handled locally in your browser. Files are never sent to a server and are cleared from browser memory after processing.'),
    ('<h2>5. 문의</h2>', '<h2>5. Contact</h2>'),
    ('<p>개인정보 처리방침 관련 문의는 아래 이메일로 연락 주세요.</p>',
     '<p>For privacy policy inquiries, please contact us at the email below.</p>'),
    # ── image-border.html ──
    ('; background:#fff; cursor:pointer;">흰색</button>', '; background:#fff; cursor:pointer;">White</button>'),
    ('; background:#000; color:#fff; cursor:pointer;">검정</button>', '; background:#000; color:#fff; cursor:pointer;">Black</button>'),
    ('; background:#e5e7eb; cursor:pointer;">회색</button>', '; background:#e5e7eb; cursor:pointer;">Gray</button>'),
    # ── resize-image.html ──
    ('title="비율 잠금"', 'title="Lock Ratio"'),
    # ── compress-image.html ──
    ("`${ratio}% 감소`", '`${ratio}% smaller`'),
    ("`: '이미 최적화된 이미지입니다.'", "`: 'Image is already optimized.'"),
    # ── upscale-image.html ──
    ('ℹ️ AI 업스케일링이 아닌 고품질 보간법(Bicubic)과 언샤프 마스크를 사용합니다. 최대 4배 확대를 지원합니다.',
     'ℹ️ Uses high-quality Bicubic interpolation and unsharp masking (not AI). Supports up to 4× upscaling.'),
    ('<div class="options-title">업스케일링 설정</div>', '<div class="options-title">Upscale Settings</div>'),
    ('<span class="option-label">확대 배율</span>', '<span class="option-label">Upscale Factor</span>'),
    ('<span class="option-label">샤프닝 강도: <strong id="sharpVal">50</strong>%</span>',
     '<span class="option-label">Sharpening: <strong id="sharpVal">50</strong>%</span>'),
    ('<div class="dim-label">원본 크기</div>', '<div class="dim-label">Original Size</div>'),
    ('<div class="dim-label">결과 크기</div>', '<div class="dim-label">Result Size</div>'),
    ('>🔍 업스케일링 시작<', '>🔍 Start Upscale<'),
    ('<div class="result-title">업스케일링 완료!</div>', '<div class="result-title">Upscaled!</div>'),
    ('<span class="split-label split-label-left">원본</span>', '<span class="split-label split-label-left">Before</span>'),
    ('<span class="split-label split-label-right">결과</span>', '<span class="split-label split-label-right">After</span>'),
    ('>⬇️ 업스케일 이미지 다운로드<', '>⬇️ Download Upscaled Image<'),
    ("`${ow}×${oh} → ${nw}×${nh} (${scale}x 확대)`", '`${ow}×${oh} → ${nw}×${nh} (${scale}× upscaled)`'),
    # ── split-image.html ──
    ('<span class="option-label">분할 격자</span>', '<span class="option-label">Split Grid</span>'),
    ('<label>가로</label>', '<label>Columns</label>'),
    ('<label>세로</label>', '<label>Rows</label>'),
    ("`= ${cols * rows} 조각`", '`= ${cols * rows} pieces`'),
    ('<span id="gridInfo" style="font-size:0.88rem;color:var(--text-light);">= 4 조각</span>',
     '<span id="gridInfo" style="font-size:0.88rem;color:var(--text-light);">= 4 pieces</span>'),
    ('<span class="option-label">저장 형식</span>', '<span class="option-label">Output Format</span>'),
    ('<option value="jpeg">JPEG (용량 작음)</option>', '<option value="jpeg">JPEG (smaller size)</option>'),
    ('<option value="png">PNG (투명 지원)</option>', '<option value="png">PNG (supports transparency)</option>'),
    ('>⊞ 이미지 분할 시작<', '>⊞ Split Image<'),
    ('<span id="progressText">분할 중...</span>', '<span id="progressText">Splitting...</span>'),
    ('<div class="result-title">이미지 분할 완료!</div>', '<div class="result-title">Split Complete!</div>'),
    ('>⬇️ 전체 ZIP으로 다운로드<', '>⬇️ Download All as ZIP<'),
    # ── round-corner.html ──
    ('<div class="options-title">모서리 설정</div>', '<div class="options-title">Corner Settings</div>'),
    ('<span class="option-label">둥글기</span>', '<span class="option-label">Roundness</span>'),
    ('<span>각지게</span>', '<span>Sharp</span>'),
    ('<span>원형</span>', '<span>Circle</span>'),
    ('<span class="option-label">배경</span>', '<span class="option-label">Background</span>'),
    ('<span style="font-size:0.9rem;">투명 (PNG)</span>', '<span style="font-size:0.9rem;">Transparent (PNG)</span>'),
    ('<span style="font-size:0.9rem;">단색 배경</span>', '<span style="font-size:0.9rem;">Solid Color</span>'),
    ('<span class="option-label">실시간 미리보기</span>', '<span class="option-label">Live Preview</span>'),
    ('<span>결과</span>', '<span>Result</span>'),
    ('>⬛ 모서리 둥글게 적용<', '>⬛ Apply Rounded Corners<'),
    ('<div class="result-title">둥근 모서리 적용 완료!</div>', '<div class="result-title">Rounded Corners Applied!</div>'),
    ('alt="둥근 모서리 이미지" style="max-width:100%;display:block;margin:0 auto;">', 'alt="Rounded Corners Image" style="max-width:100%;display:block;margin:0 auto;">'),
    # ── svg-to-png.html ──
    ('<p>.svg 파일을 업로드하세요</p>', '<p>Upload an .svg file</p>'),
    ('<span class="option-label">출력 배율</span>', '<span class="option-label">Output Scale</span>'),
    ('<option value="1">1× (원본 크기)</option>', '<option value="1">1× (original size)</option>'),
    ('<option value="2" selected>2× (권장)</option>', '<option value="2" selected>2× (recommended)</option>'),
    ('<option value="3">3× (고화질)</option>', '<option value="3">3× (high quality)</option>'),
    ('<option value="4">4× (초고화질)</option>', '<option value="4">4× (ultra quality)</option>'),
    ('<option value="image/png" selected>PNG (투명 배경 유지)</option>', '<option value="image/png" selected>PNG (preserves transparency)</option>'),
    ('<option value="image/jpeg">JPG (배경 흰색)</option>', '<option value="image/jpeg">JPG (white background)</option>'),
    ("`⬇️ ${extMap[fmt]} 다운로드`", '`⬇️ Download ${extMap[fmt]}`'),
    ("showError('SVG 파일만 업로드할 수 있습니다.'); return;", "showError('Please select an SVG file.'); return;"),
    ("`출력 Resolution: ${cw} × ${ch} px`", '`Output Resolution: ${cw} × ${ch} px`'),
    # ── exif-remove.html (remaining) ──
    ("'✅ EXIF 정보가 감지되지 않았습니다. (PNG이거나 이미 제거된 파일)'",
     "'✅ No EXIF data detected. (PNG or already cleaned file)'"),
    ("`⚠️ ${keys.length}개 EXIF 태그 감지${hasGPS ? ' (GPS 위치 포함!)' : ''}", "`⚠️ ${keys.length} EXIF tags detected${hasGPS ? ' (GPS location included!)' : ''}"),
    ("<th>항목</th><th>값</th>", "<th>Field</th><th>Value</th>"),
    ("document.getElementById('progressText').textContent = 'EXIF 제거 중...';",
     "document.getElementById('progressText').textContent = 'Removing EXIF...';"),
    ("· EXIF 완전 제거됨`", "· EXIF fully removed`"),
    ("btn.textContent = '🔒 EXIF 제거 & 저장 준비';", "btn.textContent = '🔒 Remove EXIF & Prepare Download';"),
    # ── merge-image.html (remaining) ──
    ('<span>이미지 목록 <span id="fileCount"', '<span>Images <span id="fileCount"'),
    ('>+ 추가<', '>+ Add<'),
    ("showError('최대 10장까지만 추가할 수 있습니다.');", "showError('You can add up to 10 images.');"),
    ("showError('이미지를 2장 이상 추가해 주세요.'); return;", "showError('Please add at least 2 images.'); return;"),
    ("btn.textContent = '🔗 이미지 합치기';", "btn.textContent = '🔗 Merge Images';"),
    # ── ocr-image.html (remaining) ──
    ('<li>배경이 복잡한 이미지</li>', '<li>Images with complex backgrounds</li>'),
    ('<li>심하게 기울어진 텍스트</li>', '<li>Heavily skewed text</li>'),
    ('<li>작은 글씨 (저Resolution)</li>', '<li>Small text (low resolution)</li>'),
    ("setProgress(0, '언어 데이터 로딩 중...');", "setProgress(0, 'Loading language data...');"),
    ("setProgress(5, '엔진 로딩 중...');", "setProgress(5, 'Loading engine...');"),
    ("setProgress(15, '엔진 초기화 중...');", "setProgress(15, 'Initializing engine...');"),
    ("setProgress(60, 'API 초기화 중...');", "setProgress(60, 'Initializing API...');"),
    ("`언어 데이터 다운로드 중... ${Math.round((m.progress||0)*100", "`Downloading language data... ${Math.round((m.progress||0)*100"),
    # ── ocr-pdf.html (remaining) ──
    ('• 페이지가 많을수록 처리 시간이 길어집니다 (1페이지당 약 5~30초)',
     '• More pages means longer processing time (~5–30 sec per page)'),
    ('• 첫 실행 시 언어 데이터를 다운로드합니다 (한국어 약 10MB)',
     '• The first run downloads language data (~10MB for Korean)'),
    ('• 모든 처리는 브라우저에서 이루어지며 PDF가 서버로 전송되지 않습니다',
     '• All processing happens in your browser — PDFs are never sent to a server'),
    ('• 텍스트 선택이 가능한 일반 PDF는', '• For regular PDFs where text is selectable, use'),
    ("showError('PDF 파일만 업로드할 수 있습니다.'); return;", "showError('Please select a PDF file.'); return;"),
    ("' · 페이지 수 로딩 중...'", "' · loading page count...'"),
    ("`${formatSize(file.size)} · ${pdfDoc.numPages}페이지`", '`${formatSize(file.size)} · ${pdfDoc.numPages} pages`'),
    ("showError('PDF 파일을 읽을 수 없습니다. 파일이 손상되었거나 암호화되어 있을 수 있습니다.');",
     "showError('Cannot read this PDF. It may be corrupted or password-protected.');"),
    ("// Tesseract worker 초기화", '// Initialize Tesseract worker'),
    ("setProgress(2, '언어 데이터 로딩 중...');", "setProgress(2, 'Loading language data...');"),
    ("`언어 데이터 다운로드 중... ${Math.round((m.progress||0) * 100)}%`",
     "`Downloading language data... ${Math.round((m.progress||0) * 100)}%`"),
    # ── image-filter.html (remaining) ──
    ('alt="필터 적용된 이미지 미리보기" style="max-width:100%;border-radius:8px;">', 'alt="Filtered Image Preview" style="max-width:100%;border-radius:8px;">'),
    ('>⬇️ 필터 이미지 다운로드<', '>⬇️ Download Filtered Image<'),
    ("showError('JPG, PNG, WebP 파일만 업로드할 수 있습니다.'); return;", "showError('Please select a JPG, PNG, or WebP file.'); return;"),
    ("document.getElementById('progressText').textContent = '필터 적용 중...';",
     "document.getElementById('progressText').textContent = 'Applying filter...';"),
    # ── watermark-image.html (remaining) ──
    ('<span class="option-label">글자 크기: <strong id="fontSizeVal">40</strong>px</span>',
     '<span class="option-label">Font Size: <strong id="fontSizeVal">40</strong>px</span>'),
    ('<span class="option-label">투명도: <strong id="opacityVal">70</strong>%</span>',
     '<span class="option-label">Opacity: <strong id="opacityVal">70</strong>%</span>'),
    ('<span class="option-label" style="padding-top:4px;">위치</span>', '<span class="option-label" style="padding-top:4px;">Position</span>'),
    ('data-pos="top-left" title="좌상"', 'data-pos="top-left" title="Top Left"'),
    ('data-pos="top-center" title="중상"', 'data-pos="top-center" title="Top Center"'),
    ('data-pos="top-right" title="우상"', 'data-pos="top-right" title="Top Right"'),
    ('data-pos="middle-left" title="좌중"', 'data-pos="middle-left" title="Middle Left"'),
    ('data-pos="center" title="중앙"', 'data-pos="center" title="Center"'),
    ('data-pos="middle-right" title="우중"', 'data-pos="middle-right" title="Middle Right"'),
    ('data-pos="bottom-left" title="좌하"', 'data-pos="bottom-left" title="Bottom Left"'),
    ('data-pos="bottom-center" title="중하"', 'data-pos="bottom-center" title="Bottom Center"'),
    ('data-pos="bottom-right" title="우하"', 'data-pos="bottom-right" title="Bottom Right"'),
    ('<span class="option-label">워터마크 미리보기</span>', '<span class="option-label">Watermark Preview</span>'),
    ("showError('이미지 파일만 업로드할 수 있습니다. 워터마크 텍스트를 입력하세요.');",
     "showError('Please select an image file and enter watermark text.');"),
    ("btn.textContent = '💧 워터마크 추가';", "btn.textContent = '💧 Add Watermark';"),
    # ── webp-to-jpg.html ──
    ('<p>WebP 파일을 업로드하세요 (다른 이미지 형식도 가능)</p>', '<p>Upload a WebP file (other image formats also accepted)</p>'),
    ("? '⬇️ JPG로 다운로드' : '⬇️ PNG로 다운로드'", "? '⬇️ Download as JPG' : '⬇️ Download as PNG'"),
    # ── make-gif.html (remaining) ──
    ('<span class="option-label">크기</span>', '<span class="option-label">Size</span>'),
    ('alt="프레임 ${i+1}"', 'alt="Frame ${i+1}"'),
    ('이미지 추가', 'Add Image'),
    ("btn.textContent = 'GIF 생성 중...';", "btn.textContent = 'Generating GIF...';"),
    ("progressText.textContent = 'GIF 인코딩 중...';", "progressText.textContent = 'Encoding GIF...';"),
    ("`${frames.length}프레임 · ", '`${frames.length} frames · '),
    ("btn.textContent = '🎬 GIF 생성';", "btn.textContent = '🎬 Generate GIF';"),
    # ── heic-to-jpg.html (remaining) ──
    (">다운로드<", ">Download<"),
    ("btn.textContent = '⬇️ 모두 다운로드 (ZIP)';", "btn.textContent = '⬇️ Download All (ZIP)';"),
    # ── index.html: comment ──
    ('<!-- 구조화 데이터 -->', '<!-- Structured Data -->'),
    # ── ocr-pdf / ocr-image: char count suffix (match before 'ko-KR' is replaced) ──
    ("toLocaleString('ko-KR')}자`", "toLocaleString('en-US')} chars`"),
    # ── ocr-pdf: page span (HTML) and backtick (JS template) ──
    ("<span>📄 ${i + 1}페이지</span>", "<span>📄 Page ${i + 1}</span>"),
    ("페이지`", "page`"),
    ("`📄 ${i + 1}페이지`", "`📄 Page ${i + 1}`"),
    ("// 페이지별 결과", "// results by page"),
    ("document.getElementById('progressTitle').textContent = 'PDF 분석 중…';",
     "document.getElementById('progressTitle').textContent = 'Analyzing PDF…';"),
    ("showError('텍스트 인식 중 오류가 발생했습니다. 다시 시도해보세요.');",
     "showError('OCR failed. Please try again.');"),
    # ocr-pdf: link in notes that still has Korean after partial replace
    ("style=\"color:var(--primary)\">WooaPDF에서 텍스트 추출 도구 보기 →</a>",
     "style=\"color:var(--primary)\">Extract text with WooaPDF →</a>"),
    ("으로 텍스트를 추출하세요", "to extract text"),
    # ── ocr-pdf: PDFKit link text in tip box ──
    ("PDFKit의 PDF→텍스트 변환</a>이 더 빠르고 정확합니다",
     "PDFKit PDF→Text</a> for faster, more accurate results"),
    # ── ocr-pdf: remaining suffix after partial translate ──
    ("PDFKit</a>을 이용하세요", "PDFKit</a> instead."),
    # ── privacy.html: leftover Korean after paragraph partial translate ──
    ("data를 저장하지 않습니다.", "data is not stored on the server."),
    # ── privacy.html: double n fix ──
    ("personal informationn.", "personal information."),
    # ── split-image.html: template literal inside JS ──
    ("${r+1}행 ${c+1}열 · ${sw}×${sh}", "Row ${r+1} · Col ${c+1} · ${sw}×${sh}"),
    # ── compress-image.html ──
    ("(${ratio}% 감소)`", "(${ratio}% smaller)`"),
    # ── exif-remove.html ──
    ("✅ EXIF 정보가 감지되지 않았습니다. (PNG이거나 이미 제거된 파일)", "✅ No EXIF data detected. (PNG or already cleaned file)"),
    ("개 EXIF 태그 감지${hasGPS ? ' (GPS 위치 포함!)' : ''}", " EXIF tags detected${hasGPS ? ' (GPS location included!)' : ''}"),
    # ── ocr-image.html ──
    ("`텍스트 인식 중... ${Math.round((m.", '`Recognizing text... ${Math.round((m.'),
    ("'ko-KR'", "'en-US'"),
    ("showError('텍스트 인식 중 오류가 발생했습니다. 다른 이미지로 시도해보세요.');",
     "showError('OCR failed. Please try a different image.');"),
    # ── ocr-pdf.html ──
    ("`총 ${totalPages}페이지 인식 시작...`", '`Starting OCR for ${totalPages} pages...`'),
    ("// 페이지별 렌더링 + OCR", '// render + OCR per page'),
    ("`${pageNum} / ${totalPages} 페이지 인식 중…`", '`Recognizing page ${pageNum} / ${totalPages}…`'),
    ("`${pageNum}페이지 렌더링 중...`", '`Rendering page ${pageNum}...`'),
    ("`${pageNum}페이지 텍스트 인식 중...`", '`Recognizing text on page ${pageNum}...`'),
    ("// 결과 표시", '// display results'),
    ("`[${i + 1}페이지]\\n${t}`", '`[Page ${i + 1}]\\n${t}`'),
    # ── round-corner.html ──
    (">⬇️ PNG 이미지 다운로드<", ">⬇️ Download PNG<"),
    ("btn.textContent = '⬛ 모서리 둥글게 적용';", "btn.textContent = '⬛ Apply Rounded Corners';"),
    # ── split-image.html ──
    ("btn.textContent = '⏳ 분할 중...';", "btn.textContent = '⏳ Splitting...';"),
    ("`${r+1}행 ${c+1}열 · ${sw}×${sh}`", '`Row ${r+1} Col ${c+1} · ${sw}×${sh}`'),
    ("⬇ 다운로드", "⬇ Download"),
    ("`분할 중... ${done}/${total}`", '`Splitting... ${done}/${total}`'),
    ("`${cols}열 × ${rows}행 = ${total}조각 · 각 ${tileW}×${tileH}px`", '`${cols} cols × ${rows} rows = ${total} pieces · each ${tileW}×${tileH}px`'),
    ("btn.textContent = '⊞ 이미지 분할 시작';", "btn.textContent = '⊞ Split Image';"),
    ("btn.textContent = '⏳ ZIP 생성 중...';", "btn.textContent = '⏳ Creating ZIP...';"),
    ("btn.textContent = '⬇️ 전체 ZIP으로 다운로드';", "btn.textContent = '⬇️ Download All as ZIP';"),
    # ── upscale-image.html ──
    ("btn.textContent = '🔍 업스케일링 시작';", "btn.textContent = '🔍 Start Upscale';"),
    # ── watermark-image.html ──
    (">⬇️ 워터마크 이미지 다운로드<", ">⬇️ Download Watermarked Image<"),
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
        _h1 = meta['h1']
        replaced = re.sub(r'<h1 id="toolTitle">[^<]*</h1>', lambda m: f'<h1 id="toolTitle">{_h1}</h1>', html)
        if replaced == html:
            replaced = re.sub(r'<h1>([^<]*)</h1>', lambda m: f'<h1>{_h1}</h1>', html, count=1)
        html = replaced
    if meta.get('tool_desc'):
        _td = meta['tool_desc']
        replaced = re.sub(r'<p id="toolDesc">[^<]*</p>', lambda m: f'<p>{_td}</p>', html)
        if replaced == html:
            # fallback: first <p> right after <h1> in tool-header div
            replaced = re.sub(
                r'(<div class="tool-header">.*?</h1>\s*)<p>([^<]+)</p>',
                lambda m: m.group(1) + f'<p>{_td}</p>',
                html, flags=re.DOTALL, count=1
            )
        html = replaced
    if meta.get('breadcrumb'):
        _bc = meta['breadcrumb']
        replaced = re.sub(r'<span id="breadcrumbTitle">[^<]*</span>', lambda m: f'<span>{_bc}</span>', html)
        if replaced == html:
            # fallback: last <span> in breadcrumb div (no id attribute)
            replaced = re.sub(
                r'(<div class="breadcrumb">.*?<span>›</span>\s*)<span>[^<]+</span>',
                lambda m: m.group(1) + f'<span>{_bc}</span>',
                html, flags=re.DOTALL, count=1
            )
        html = replaced

    # ── 공통 문자열 치환 ──
    for ko, en in COMMON:
        html = html.replace(ko, en)

    # ── 언어 선택기 CSS 삽입 ──
    if 'lang-switcher' not in html:
        html = html.replace('  </style>', LANG_SWITCHER_CSS + '  </style>', 1)
        if '  </style>' not in html:
            # </head> 바로 앞에 스타일 블록 삽입
            html = html.replace('</head>', f'  <style>\n{LANG_SWITCHER_CSS}  </style>\n</head>', 1)

    # ── 헤더에 언어 선택기 삽입 (기존 header-right 먼저 제거) ──
    # Remove any existing header-right (greedy .* finds the last </div> before </div></header>)
    html = re.sub(
        r'\s*<div class="header-right">.*</div>(?=\s*\n?\s*</div>\s*\n?</header>)',
        '',
        html, count=1, flags=re.DOTALL
    )
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
            # lang switcher HTML: remove existing header-right then insert EN version
            html = re.sub(
                r'\s*<div class="header-right">.*</div>(?=\s*\n?\s*</div>\s*\n?</header>)',
                '',
                html, count=1, flags=re.DOTALL
            )
            html = re.sub(
                r'(\s*</div>\s*</header>)',
                f'\n    <div class="header-right">\n'
                f'      <div class="lang-switcher">\n'
                f'        <a href="../{f}">KO</a>\n'
                f'        <span>|</span>\n'
                f'        <a href="{f}" class="active">EN</a>\n'
                f'      </div>\n'
                f'      <a href="../about.html" style="color:rgba(255,255,255,0.85); font-size:0.85rem; text-decoration:none; margin-left:8px;">About</a>\n'
                f'    </div>\n'
                f'  </div>\n'
                f'</header>',
                html, count=1
            )
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
