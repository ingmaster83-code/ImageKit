# ImageKit 프로젝트 지침

## 프로젝트 개요
- **사이트명:** 이미지킷 (ImageKit)
- **URL:** https://imagekit.wooahouse.com
- **GitHub:** https://github.com/ingmaster83-code/ImageKit
- **배포:** GitHub Pages (main 브랜치 → root)
- **도메인 관리:** 호스팅케이알
- **DNS:** imagekit CNAME → ingmaster83-code.github.io

## 기술 스택
- 순수 HTML / CSS / JS (프레임워크 없음)
- 이미지 처리: 브라우저 Canvas API (서버 전송 없음)
- PWA: manifest.json + sw.js + js/pwa-install.js

## 서비스 목적
브라우저에서 직접 이미지를 압축·변환·편집하는 무료 도구 모음.
파일이 서버에 저장되지 않아 안전.

## 도구 목록 (17개)
### 기본 변환
- jpg-to-png.html, png-to-jpg.html, image-to-webp.html, webp-to-jpg.html
### 편집
- compress-image.html, resize-image.html, rotate-image.html, crop-image.html
- watermark-image.html, image-to-base64.html, image-info.html
### AI·변환 확장 (최근 추가)
- **bg-remove.html** — AI 배경 제거 (@imgly/background-removal ESM)
- **heic-to-jpg.html** — HEIC→JPG 변환 (heic2any + JSZip 일괄 다운로드)
- **make-gif.html** — GIF 만들기 (gif.js)
- **upscale-image.html** — 이미지 업스케일링 (Canvas 보간법)
### OCR (최근 추가)
- **ocr-image.html** — 이미지 텍스트 추출 (Tesseract.js v4, 한/영)
- **ocr-pdf.html** — PDF 텍스트 OCR (PDF.js + Tesseract.js, 스캔 PDF용)

## 작업 규칙
- 모든 이미지 처리는 Canvas API로 브라우저에서만 처리 (서버 전송 금지)
- 새 도구 추가 시 index.html 카드, sitemap.xml 업데이트 필수
- 다운로드 버튼은 id="downloadBtn" 사용
- bg-remove.html은 `<script type="module">` 필수 (@imgly ESM)
- SEO 키워드: 이미지 압축, 이미지 변환, 이미지 리사이즈, 배경 제거, 이미지 OCR
