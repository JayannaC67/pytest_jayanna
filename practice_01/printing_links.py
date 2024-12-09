from selenium import webdriver
from selenium.webdriver.common.by import By

class Print_links:

    def launch_the_application(self):

        global driver #making driver as global variable
        #driver = webdriver.Chrome()  #instanciating Chrome driver inside driver variable
        driver=webdriver.Edge()
        driver.get("http://qualitrix.com") # Using ".get" we can launch the URL.
        driver.maximize_window()

    def print_all_links(self):

        total_links_count = driver.find_elements(By.XPATH,"//a")
        # total_links_count = len(driver.find_elements(By.XPATH,"//a"))
        print(len(total_links_count))
        total_links_count = len(driver.find_elements(By.XPATH,"//a"))

        file = open("C:\\Users\LenT14G2ITL\\PycharmProjects\\jay_pythonbasic_learning\practice_01\\linktext.txt", "w")

        for i in range (1,total_links_count+1):

            xpath = '(//a)['+str(i)+']'
           # print(xpath)

            link_name=driver.find_element(By.XPATH,xpath).text
            print("when the value of i is :" + str(i) + " " + "the value of the text is : " + link_name)


            file.write("when the value of i is :" + str(i) + " " + "the value of the text is : " + link_name)
            file.write("\n")

        file.close()
        print("Data is written into the file.")


        driver.quit()

obj=Print_links()
obj.launch_the_application()
obj.print_all_links()


