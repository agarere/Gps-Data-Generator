import sys

FileName = sys.argv[1]

DateTime_Raw 	= "20190923"
DateTime_Hours  = 5
DateTime_Minute	= 0
DateTime_Sec	= 0

	
#################################

def TIME_getNextDateTime():
	date_time = ""
	
	global DateTime_Hours
	global DateTime_Minute
	global DateTime_Sec

	DateTime_Sec = DateTime_Sec + 5
	if DateTime_Sec > 59:
		DateTime_Sec = 0
		DateTime_Minute = DateTime_Minute + 1

	if DateTime_Minute > 59:
		DateTime_Minute = 0
		DateTime_Hours = DateTime_Hours + 1

	if DateTime_Hours > 23: 
		DateTime_Hours = 0

	date_time = date_time + DateTime_Raw
	date_time = date_time + "{:02d}".format(DateTime_Hours)
	date_time = date_time + "{:02d}".format(DateTime_Minute)
	date_time = date_time + "{:02d}".format(DateTime_Sec)
	#print("[ " + date_time + " ]")	
	
	return date_time

#################################

def TIME_getNextUTCTime():
	utc_time = "2"
	global DateTime_Minute
	global DateTime_Sec

	utc_time = utc_time + "{:02d}".format(DateTime_Minute)
	utc_time = utc_time + "{:02d}".format(DateTime_Sec)
	#print(utc_time)
	
	return utc_time

#################################

def GPSFILE_writeLine(gps_file, line):
	gps_file.write(line)
	gps_file.write("\n")

#################################

def GPSFILE_add(gps_file, coordinate):
	gps_dat = "<GPSDAT BUS_ID=\"04066\" "
	parsed_coordinate = coordinate.split(',')
	
	lat = float(parsed_coordinate[0])
	lon = float(parsed_coordinate[1])
	
	gps_dat = gps_dat + "DATE_TIME=" + "\"" + TIME_getNextDateTime() + "\" "
	gps_dat = gps_dat + "LATITUDE=" + "\"" + "{:010.6f}".format(lat) + "\" "
	gps_dat = gps_dat + "NSINDICATOR=\"\" "
	gps_dat = gps_dat + "LONGITUDE=" + "\"" + "{:010.6f}".format(lon) + "\" "
	gps_dat = gps_dat + "EWINDICATOR=\"\" "
	gps_dat = gps_dat + "ALTITUDE=\"12\" "
	gps_dat = gps_dat + "SPEED=\"36\" "
	gps_dat = gps_dat + "UTCTIME=" + "\"" + TIME_getNextUTCTime() + "\" "
	gps_dat = gps_dat + "HDOP=\"0\" "
	gps_dat = gps_dat + "SVCOUNT=\"13\" "
	gps_dat = gps_dat + "STATUS=\"1\""
	gps_dat = gps_dat + "/>"

	print(gps_dat)
	GPSFILE_writeLine(gps_file, gps_dat)
	

#################################

def main():
	CSV_File = open(FileName, "r")
	GPS_File = open("output.xml", "w")
	
	GPSFILE_writeLine(GPS_File, "<GPS>")
	
	#line = CSV_File.readline()
	for line in CSV_File:	
		GPSFILE_add(GPS_File, line)

	GPSFILE_writeLine(GPS_File, "</GPS>")

	CSV_File.close()
	GPS_File.close()
	

#################################

if __name__ == "__main__":
	main()

