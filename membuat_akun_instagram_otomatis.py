print ("##############################################################################################################################")
print ("###############---------------------$$$$$$$$$$$$$$$$$-C O C O N U T-$$$$$$$$$$$$$$$$$$-----------------------#################")
print ("###############----------------------------------------------------------------------------------------------#################")
print ("      	###################               ###			                       ##################		      ")
print ("       	###################               ###				                   ##################     		  ")
print ("		###################               ###			                       ##################             ")
print ("		###             ###               ###                                  ###            ###		      ")
print ("		###             ###               ###                                  ###            ###		      ")
print ("		###      C      ###               ### #################                ###      C     ###		      ")
print ("        ###      O      ###               ### #################                ###      O     ###    		  ")
print ("		###      C      ###               ### #################                ###      C     ###		      ")
print ("		###      O      ###               ###               ###                ###      O     ### 		      ")
print ("		###      N      ###               ###               ###                ###      N     ### 		      ")
print ("		###      U      ###               ###               ###                ###      U     ###		      ")
print ("		###      T      ###               ###               ###                ###      T     ### 		      ")
print ("		###             ###               ###               ###                ###            ###		      ")
print ("		###             ###               ###               ###                ###            ###		      ")
print ("		###################               #####################                ##################		      ")
print ("		###################               #####################                ##################		      ")
print ("		###################               #####################                ##################		      ")
print ("###############----------------------------------------------------------------------------------------------#################")
print ("###############---------------------$$$$$$$$$$$$$$$$$-C O C O N U T-$$$$$$$$$$$$$$$$$$-----------------------#################")
print ("##############################################################################################################################")

print ("------------------------------------------------MEMBUAT AKUN INSTAGRAM--------------------------------------------------------")
print ("--------------------------------------------------------OTOMATIS--------------------------------------------------------------")

jawab = 'ya'
hitung = 0
while(True):
	hitung +1



# input untuk isi from
	emailOrPhone= raw_input("Masukkan Nomor Ponsel atau Email: ")
	fullName= raw_input("Masukkan Nama Lengkap: ")
	username= raw_input("Masukkan Nama Pengguna: ")
	password= raw_input("Masukkan Passwoard: ")
#confrmPass = raw_input("Masukkan Confirmasi Passwoard: ")
#confirmEmail = raw_input("Masukkan Confirmasi Email: ")

# Menampilkan output
#print "Silahkan Tunggu !!!"

# untuk menjalankan firefox
	from selenium import webdriver
#from selenium.webdriver.support.select import select
#from selenium.webdriver.support.ui import select
	import time
	firefox_options = webdriver.FirefoxOptions()
	firefox_options.add_argument("--private")
	browser = webdriver.Firefox(firefox_options=firefox_options)
	url = "https://www.instagram.com/accounts/login/?hl=id&source=auth_switcher"
	browser.get(url)
	time.sleep(5)
	linkElam = browser.find_element_by_link_text("Buat akun").click()
	time.sleep(10)
	browser.find_element_by_name("emailOrPhone").send_keys(emailOrPhone)
	time.sleep(5)
	browser.switch_to.default_content()
	time.sleep(5)
	browser.find_element_by_name("fullName").send_keys(fullName)
	time.sleep(50)
	browser.find_element_by_name("username").send_keys(username)
	time.sleep(20)
	browser.find_element_by_name("password").send_keys(password)
	time.sleep(50)
	browser.find_element_by_xpath("//button[@type='submit']").click()
	time.sleep(60)
	browser.find_element_by_xpath("//button[@type='button']").click()
	time.sleep(60)
	browser.find_element_by_xpath("(//button[@type='button'])[2]").click()
	time.sleep(20)
    #browser.find_element_by_xpath("(//button[@type='button'])[13]").click()
    #browser.find_element_by_type("button").click()
	browser.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[4]/a/img").click()
	time.sleep(20)
	browser.find_element_by_css(".wpO6b > .\_8-yf5").click()
	time.sleep(20)
	browser.find_element_by_xpath("//button[contains(.,'Keluar')]").click()	
	time.sleep(20)
	browser.close()

	jawab = raw_input('ingin menginput lagi ? ya/tidak ') 
	if jawab == "tidak" :
		break

	print "akun anda selesai"
