import qrcode
from barcode import EAN13
from barcode.writer import ImageWriter
from pyzbar import pyzbar
import imutils
import cv2
import os
from easyocr import Reader

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

# -- BARCODES -- #

def make_dir_if_not_exists(d):
	if not os.path.isdir(f"{BASE_DIR}/{d}"):
		os.mkdir(f"{BASE_DIR}/{d}")

def generate_qr(name, data):
	png_path = f"qr_imgs/{name}.png"
	qr = qrcode.QRCode(version=1, box_size=10, border=0)
	qr.add_data(data)
	qr.make(fit=True)
	img = qr.make_image(fill="black", back_color="white")
	make_dir_if_not_exists("qr_imgs")
	img.save(png_path)
	return png_path

def generate_barcode(name, number):
	my_code = EAN13(str(number), writer=ImageWriter())
	make_dir_if_not_exists("barcode_imgs")
	my_code.save(f"barcode_imgs/{name}")

# Source: https://www.pyimagesearch.com/2018/05/21/an-opencv-barcode-and-qr-code-scanner-with-zbar/
def read_code(frame, render=False, code_type="ANY"):
	barcodes = pyzbar.decode(frame)
	vals = []
	for barcode in barcodes:
		if render:
			(x, y, w, h) = barcode.rect
			cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
		barcode_data = barcode.data.decode("utf-8")
		barcode_type = barcode.type
		print(barcode_data, barcode_type)
		if barcode_type == code_type or code_type == "ANY":
			vals.append(barcode_data)
		if render:
			text = "{} ({})".format(barcode_data, barcode_type)
			cv2.putText(frame, text, (x, y - 10),
				cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
	if render:
		cv2.imshow("Barcode Scanner", frame)
		key = cv2.waitKey(1) & 0xFF
	return vals

# read_qr = make_reader("QRCODE")
# read_barcode = make_reader("EAN13")
# read_any = make_reader("ANY")

def read_from_camera(vs, render=False, filter="ANY"):
	frame = vs.read()

	frame = imutils.resize(frame, width=400)
	return read_code(frame, render, filter)

# -- OCR -- #

def read_ocr(frame):
	reader = Reader(["en"], gpu=False)
	results = reader.readtext(frame, allowlist="0123456789")
	# print(results)
	# Get [1] entry of each tuple, combine with spaces
	return " ".join([x[1] for x in results])

def read_ocr_from_camera(vs, filter=""):
	frame = vs.read()
	frame = imutils.resize(frame, width=800)
	return read_ocr(frame)
