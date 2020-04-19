import cv2
import os
import imutils
import requests
import numpy as np
import pytesseract
import time
import json
from PIL import Image


def nano_api_call(url, image, result_file, b_dir):
	#start time measure
	start_measure = time.time()
	#nanoNets api
	data = {'file': open("./"+b_dir+"/"+image, 'rb')}
	response = requests.post(url, auth=requests.auth.HTTPBasicAuth('4gkPCEoZZEOAAusnXcPW3fkjKQZ6yzQ7', ''), files=data)
	y = json.loads(response.text)
	#prediction evaluation
	if not y['result']['prediction']:
		result = 0 # Nao Identificado
		result_file.write(image+';'+result)
	else:
		result = 1 # Identificado
		aux = image+';'+result
	result_file.write(';'+y['result']['prediction'][0]['score']+';'+';'++';'++';'++';'++';'++';'+)
	if result == 1 and y['result']['prediction'][0]['score'] >= 0.70 :
		
	#crop plate from image
	img = cv2.imread("./"+base_dir+"/"+image,cv2.IMREAD_COLOR)
	img = cv2.resize(img, (620,480) )
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #convert to grey scale
	gray = cv2.bilateralFilter(gray, 11, 17, 17) #Blur to reduce noise
	#cv2.drawContours(img, [screenCnt], -1, (0, 255, 0), 3)
	
	#start time measure
	end__measure = time.time()


def main ():
	url = 'https://app.nanonets.com/api/v2/ObjectDetection/Model/c78c3274-bb93-437e-8a13-d6580356f868/LabelFile/'
	base_dir = 'base_ufmg'
	arr = os.listdir("./"+base_dir)
	f = open("result_"+base_dir+".csv","w+")
	start_general = time.time()
	for x in arr:
		#id_no_ai(x, f, base_dir)
		nano_api_call(x, f, base_dir)
	end_general = time.time()
	print(end - start)
	f.close()
	

def id_no_ia(image, result, base_dir):
	print(image)
	img = cv2.imread("./"+base_dir+"/"+image,cv2.IMREAD_COLOR)
	img = cv2.resize(img, (620,480) )
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #convert to grey scale
	gray = cv2.bilateralFilter(gray, 11, 17, 17) #Blur to reduce noise
	edged = cv2.Canny(gray, 30, 200) #Perform Edge detection

	# find contours in the edged image, keep only the largest
	# ones, and initialize our screen contour
	cnts = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	cnts = imutils.grab_contours(cnts)
	cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:10]
	screenCnt = None

	# loop over our contours
	for c in cnts:
		# approximate the contour
		peri = cv2.arcLength(c, True)
		approx = cv2.approxPolyDP(c, 0.018 * peri, True)
	 
		# if our approximated contour has four points, then
		# we can assume that we have found our screen
		if len(approx) == 4:
			screenCnt = approx
			break



	if screenCnt is None:
		detected = 0
		print "No contour detected"
		#put in result array erro info
		cv2.imshow('image',img)
		result.write(image+";"+"0"+";0\n")
		return 0
	else:
		detected = 1

	if detected == 1:
		cv2.drawContours(img, [screenCnt], -1, (0, 255, 0), 3)

	# Masking the part other than the number plate
	mask = np.zeros(gray.shape,np.uint8)
	print(mask)
	new_image = cv2.drawContours(mask,[screenCnt],0,255,-1,)
	cv2.imshow('image',new_image)
	new_image = cv2.bitwise_and(img,img,mask=mask)
	cv2.imshow('image',new_image)

	# Now crop
	(x, y) = np.where(mask == 255)
	(topx, topy) = (np.min(x), np.min(y))
	(bottomx, bottomy) = (np.max(x), np.max(y))
	Cropped = gray[topx:bottomx+1, topy:bottomy+1]



	#Read the number plate
	text = pytesseract.image_to_string(Cropped, config='--psm 11')
	print("Detected Number is:",text)

	#cv2.imshow('image',img)
	#cv2.imshow('Cropped',Cropped)
	print(text)
	result.write(image+";"+str(text.encode('utf-8'))+";"+"1\n")
	cv2.waitKey(5)
	cv2.destroyAllWindows()


if __name__ == "__main__":
	main()
