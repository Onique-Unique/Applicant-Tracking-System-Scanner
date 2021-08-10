#" IMPORT ALL REQUIRED MODULES NEEDED FOR THIS APPLICANT TRACKING SYSTEM"
#" IMPORT DOCX2TXT MODULE TO CONVERT DOCX FILES INTO A CONSUMABLE TEXT FORMAT"

import docx2txt
import sys 
from pdf2docx import Converter
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

#" CREATE A VARIABLE TO PULL PDF RESUME SOURCE/ DESTINATION FILE"
#" CREATE A VARIABLE TO DEPOSIT/ SAVE PDF TO DOCX CONVERTED RESUME SOURCE/ DESTINATION FILE"

print("Welcome To Free ATS Scanner Please Enter Your Name")
name = input()

print("Hello " + name + " Let's Get Started")

while True: 
    print("Is Your resume and job description in PDF format? type 1 for YES! 2 for NO! 3 to exit")   
    Press = int(input())
    for Choice in range(1):
        
        if Press == 3:
            sys.exit()
            
        if Press == 1:
            print("Copy PDF Resume Name Here")
            PDFresume = input()
            pdf_file = r"C:\Users\kiddo\OneDrive\Desktop\Automate Codes 1 -6/" + PDFresume + ".pdf" # source file
            docx_file = r"C:\Users\kiddo\OneDrive\Desktop\Automate Codes 1 -6/" + PDFresume + ".docx"  # destination file
            
            #" Please note your C: drive/ file path information will be required to proceed"
            #" E.g \Users\name\location of file"
            
            print("Please Wait for Process PDF Converter To Complete")
            print("You Will be Prompt For Further Information")
           
            # convert resume pdf to docx
            cv = Converter(pdf_file)
            cv.convert(docx_file, start=0, end=None)
            cv.close()
           
            #" CREATE A VARIABLE TO PULL PDF JOB DESCRIPTION SOURCE/ DESTINATION FILE IF ANY"
            #" CREATE A VARIABLE TO DEPOSIT/ SAVE PDF TO DOCX CONVERTED JOB DESCRIPTION SOURCE/ DESTINATION FILE"
            print("Copy PDF Job Description Name Here")
            PDFJobDesc = input()
            pdf_file = r"C:\Users\kiddo\OneDrive\Desktop\Automate Codes 1 -6/" + PDFJobDesc + ".pdf" # source file
            docx_file = r"C:\Users\kiddo\OneDrive\Desktop\Automate Codes 1 -6/" + PDFJobDesc + ".docx"  # destination file

            print("Please Wait for Process PDF Converter To Complete")
            
            # convert job description pdf to docx
            cv = Converter(pdf_file)
            cv.convert(docx_file, start=0, end=None)
            cv.close()

            #" CREATE A VARIABLE TO PROCESS RESUME DOCX FILE INTO TEXT FORMAT"
            #" PRINT(RESUME) COULD NOT PROCEED"
            #" INSERTED .encode("cp1252", [-source of error] errors= "ignore") [-given instructions to ignore]
            
            resume = docx2txt.process(PDFresume + ".docx")
            print((resume).encode('cp1252', errors='ignore'))
            
            jobdescription = docx2txt.process(PDFJobDesc + ".docx")
            print((jobdescription).encode('cp1252', errors='ignore'))
            
            #" CV.FIT_TRANSFORM() TAKES ONLY ONE ARGUMENT"
            #" CREATE A VARIABLE TO HOLD CONVERTED RESUME & JOB DESCRIPTION DOCX TO TEXT PROCESS"
            
            text = [resume, jobdescription]

            cv = CountVectorizer()
            count_matrix = cv.fit_transform(text)

            print("\nSimilarity Scores:")
            print(cosine_similarity(count_matrix))

            #" CREATE A KEYWORD GRABBER TO COMPARE BETWEEN RESUME AND JOB DESCRIPTION"
            #" CREATE A VARIABLE TO HOLD DOCX TO TEXT CONVERTED FILES FOR COMPARING"
            #" CREATE A COMPARE VARIABLE FOR CONVERTED DOCX TO TEXT FILES"

            resume_reference = resume.lower()
            job_reference = jobdescription.lower()
            compare = [resume_reference , job_reference]
            cVect = CountVectorizer()
            count_matrix = cVect.fit_transform(compare)

            matchPercentage = cosine_similarity(count_matrix)[0][1] * 100
            matchPercentage = round(matchPercentage, 2)
            print("Your resume matches about " + str(matchPercentage) + "%" + " of the job description")

            if (matchPercentage >= 50 < 80):
                revised_sum = matchPercentage + 10
               
               #" If a match percentage is greater or equal to 50 but less than 80, an optimise score of 10 is added"
               
                print("Press Enter To See Your Resume Complete Optimised Score")
                Enter = input()
                print("Your Total Resume match score is " + str(revised_sum) + "%")
                print("You Are Missing These Keywords- Add Them For Better Results:")
                string_1 = resume 
                string_2 = resume + jobdescription

                # First split your strings into sets of words
                set_1 = set(string_1.split())
                set_2 = set(string_2.split())

                # Compare the sets to find where they both have the same value
                
                differences = set_2.difference(set_1)
                print(*differences)
                
                print("Your Resume is Optimised for these Industry")
                print("Each Industry is rated out of 10")
                
                if "quality" in resume_reference:
                    quality_score = resume_reference.count("quality")
                    print("Your Score for Quality Assurance is: " + str(quality_score))
                
                else:
                    print("Your Score for Quality Assurance is: 0")
                    
                if "operations" in resume_reference:
                    operations_score = resume_reference.count("operations")
                    print("Your Score for Operations is: " + str(operations_score))
                
                else:
                    print("Your Score for Operations is: 0")
                    
                if "inventory" in resume_reference:
                    supply_score = resume_reference.count("inventory")
                    print("Your Score for Supply Chain is: " + str(supply_score))
                
                else:
                    print("Your Score for Supply Chain is: 0")
                    
                if "administration" in resume_reference:
                    project_score = resume_reference.count("administration")
                    print("Your Score for Finance is: " + str(project_score))
                
                else:
                    print("Your Score for Finance is: 0")
                    
                if "programming" in resume_reference:
                    data_score = resume_reference.count("programming")
                    print("Your Score for Data Analytics is: " + str(data_score))
                
                else:
                    print("Your Score for Data Analytics is: 0")
                    
                if "health" in resume_reference:
                    health_score = resume_reference.count("health")
                    print("Your Score for Health Care is: " + str(health_score))
                
                else:
                    print("Your Score for Health Care is: 0")
                
            elif (matchPercentage >= 80):
                print("You Have Achieved A Great Match Score ")
                print("You Have These Keywords Matched:")
                string_1 = resume
                string_2 = jobdescription

                # First split your strings into sets of words
                set_1 = set(string_1.split())
                set_2 = set(string_2.split())

                # Compare the sets to find where they both have the same value
                
                matches = set_1.intersection(set_2)
                print(matches)
                
                print("Your Resume is Optimised for these Industry")
                print("Each Industry is rated out of 10")
                
                if "quality" in resume_reference:
                    quality_score = resume_reference.count("quality")
                    print("Your Score for Quality Assurance is: " + str(quality_score))
                
                else:
                    print("Your Score for Quality Assurance is: 0")
                    
                if "operations" in resume_reference:
                    operations_score = resume_reference.count("operations")
                    print("Your Score for Operations is: " + str(operations_score))
                
                else:
                    print("Your Score for Operations is: 0")
                    
                if "inventory" in resume_reference:
                    supply_score = resume_reference.count("inventory")
                    print("Your Score for Supply Chain is: " + str(supply_score))
                
                else:
                    print("Your Score for Supply Chain is: 0")
                    
                if "administration" in resume_reference:
                    project_score = resume_reference.count("administration")
                    print("Your Score for Finance is: " + str(project_score))
                
                else:
                    print("Your Score for Finance is: 0")
                    
                if "programming" in resume_reference:
                    data_score = resume_reference.count("programming")
                    print("Your Score for Data Analytics is: " + str(data_score))
                
                else:
                    print("Your Score for Data Analytics is: 0")
                    
                if "health" in resume_reference:
                    health_score = resume_reference.count("health")
                    print("Your Score for Health Care is: " + str(health_score))
                
                else:
                    print("Your Score for Health Care is: 0")
       
            else:
                print("Application is missing vital Keywords:")

                #" Create a variable to hold txt strings of both resume and job description"
                
                string_1 = resume 
                string_2 = resume + jobdescription

                # First split your strings into sets of words
                set_1 = set(string_1.split())
                set_2 = set(string_2.split())
                
                #" Compare sets to find where they both have the different value"
                #" Then print results to give User the ability to identify missing keywords for resume"
                
                differences = set_2.difference(set_1)
                print(*differences)
                
                #" Create a variable to hold txt strings of both resume and job description"
                
                print("However  You Have These Keywords Matched:")
                string_1 = resume
                string_2 = jobdescription

                # First split your strings into sets of words
                set_1 = set(string_1.split())
                set_2 = set(string_2.split())

                # Compare the sets to find where they both have the same value
                #" Then print results to give User the ability to identify common keywords from job description"
                
                matches = set_1.intersection(set_2)
                print(matches)
                
                print("Your Resume is Optimised for these Industry")
                print("Each Industry is rated out of 10")
                
                if "quality" in resume_reference:
                    quality_score = resume_reference.count("quality")
                    print("Your Score for Quality Assurance is: " + str(quality_score))
                
                else:
                    print("Your Score for Quality Assurance is: 0")
                    
                if "operations" in resume_reference:
                    operations_score = resume_reference.count("operations")
                    print("Your Score for Operations is: " + str(operations_score))
                
                else:
                    print("Your Score for Operations is: 0")
                    
                if "inventory" in resume_reference:
                    supply_score = resume_reference.count("inventory")
                    print("Your Score for Supply Chain is: " + str(supply_score))
                
                else:
                    print("Your Score for Supply Chain is: 0")
                    
                if "administration" in resume_reference:
                    project_score = resume_reference.count("administration")
                    print("Your Score for Finance is: " + str(project_score))
                
                else:
                    print("Your Score for Finance is: 0")
                    
                if "programming" in resume_reference:
                    data_score = resume_reference.count("programming")
                    print("Your Score for Data Analytics is: " + str(data_score))
                
                else:
                    print("Your Score for Data Analytics is: 0")
                    
                if "health" in resume_reference:
                    health_score = resume_reference.count("health")
                    print("Your Score for Health Care is: " + str(health_score))
                
                else:
                    print("Your Score for Health Care is: 0")
       
        #" This Section is the alternative if the User posses Docx files instead of PDF"
        
        if Press == 2:
            print("Copy Docx Resume Name Here")
            DocxResume = input()
            resume = docx2txt.process(DocxResume + ".docx")
            print((resume).encode('cp1252', errors='ignore'))

            #" CREATE A VARIABLE TO PROCESS JOBDESCRIPTION DOCX FILE INTO TEXT FORMAT"
            #" PRINT(JOBDESCRIPTION) COULD NOT PROCEED"
            #" INSERTED .encode("cp1252", [-source of error] errors= "ignore") [-given instructions to ignore]
            
            print("Copy Docx Job Description Name Here")
            DocxJobDesc = input()
            jobdescription = docx2txt.process(DocxJobDesc + ".docx")
            print((jobdescription).encode('cp1252', errors='ignore'))

            #" CV.FIT_TRANSFORM() TAKES ONLY ONE ARGUMENT"
            #" CREATE A VARIABLE TO HOLD CONVERTED RESUME & JOB DESCRIPTION DOCX TO TEXT PROCESS"
            text = [resume, jobdescription]

            cv = CountVectorizer()
            count_matrix = cv.fit_transform(text)

            print("\nSimilarity Scores:")
            print(cosine_similarity(count_matrix))

            #" CREATE A KEYWORD GRABBER TO COMPARE BETWEEN RESUME AND JOB DESCRIPTION"
            #" CREATE A VARIABLE TO HOLD DOCX TO TEXT CONVERTED FILES FOR COMPARING"
            #" CREATE A COMPARE VARIABLE FOR CONVERTED DOCX TO TEXT FILES"

            resume_reference = resume.lower()
            job_reference = jobdescription.lower()
            compare = [resume_reference , job_reference]
            cVect = CountVectorizer()
            count_matrix = cVect.fit_transform(compare)

            matchPercentage = cosine_similarity(count_matrix)[0][1] * 100
            matchPercentage = round(matchPercentage, 2)
            print("Your resume matches about " + str(matchPercentage) + "%" + " of the job description")

            if (matchPercentage >= 50 < 80):
                revised_sum = matchPercentage + 10
                print("Press Enter To See Your Resume Complete Optimised Score")
                Enter = input()
                print("Your Total Resume match score is " + str(revised_sum) + "%")
                print("You Are Missing These Keywords- Add Them For Better Results:")
                string_1 = resume 
                string_2 = resume + jobdescription

                # First split your strings into sets of words
                set_1 = set(string_1.split())
                set_2 = set(string_2.split())

                # Compare the sets to find where they both have the same value
                
                differences = set_2.difference(set_1)
                print(*differences)
                
                print("Your Resume is Optimised for these Industry")
                print("Each Industry is rated out of 10")
                
                if "quality" in resume_reference:
                    quality_score = resume_reference.count("quality")
                    print("Your Score for Quality Assurance is: " + str(quality_score))
                
                else:
                    print("Your Score for Quality Assurance is: 0")
                    
                if "operations" in resume_reference:
                    operations_score = resume_reference.count("operations")
                    print("Your Score for Operations is: " + str(operations_score))
                
                else:
                    print("Your Score for Operations is: 0")
                    
                if "inventory" in resume_reference:
                    supply_score = resume_reference.count("inventory")
                    print("Your Score for Supply Chain is: " + str(supply_score))
                
                else:
                    print("Your Score for Supply Chain is: 0")
                    
                if "administration" in resume_reference:
                    project_score = resume_reference.count("administration")
                    print("Your Score for Finance is: " + str(project_score))
                
                else:
                    print("Your Score for Finance is: 0")
                    
                if "programming" in resume_reference:
                    data_score = resume_reference.count("programming")
                    print("Your Score for Data Analytics is: " + str(data_score))
                
                else:
                    print("Your Score for Data Analytics is: 0")
                    
                if "health" in resume_reference:
                    health_score = resume_reference.count("health")
                    print("Your Score for Health Care is: " + str(health_score))
                
                else:
                    print("Your Score for Health Care is: 0")
            
            elif (matchPercentage >= 80):
                print("You Have Achieved A Great Match Score ")
                print("You Have These Keywords Matched:")
                string_1 = resume
                string_2 = jobdescription

                # First split your strings into sets of words
                set_1 = set(string_1.split())
                set_2 = set(string_2.split())

                # Compare the sets to find where they both have the same value
                
                matches = set_1.intersection(set_2)
                print(matches)
                
                print("Your Resume is Optimised for these Industry")
                print("Each Industry is rated out of 10")
                
                if "quality" in resume_reference:
                    quality_score = resume_reference.count("quality")
                    print("Your Score for Quality Assurance is: " + str(quality_score))
                
                else:
                    print("Your Score for Quality Assurance is: 0")
                    
                if "operations" in resume_reference:
                    operations_score = resume_reference.count("operations")
                    print("Your Score for Operations is: " + str(operations_score))
                
                else:
                    print("Your Score for Operations is: 0")
                    
                if "inventory" in resume_reference:
                    supply_score = resume_reference.count("inventory")
                    print("Your Score for Supply Chain is: " + str(supply_score))
                
                else:
                    print("Your Score for Supply Chain is: 0")
                    
                if "administration" in resume_reference:
                    project_score = resume_reference.count("administration")
                    print("Your Score for Finance is: " + str(project_score))
                
                else:
                    print("Your Score for Finance is: 0")
                    
                if "programming" in resume_reference:
                    data_score = resume_reference.count("programming")
                    print("Your Score for Data Analytics is: " + str(data_score))
                
                else:
                    print("Your Score for Data Analytics is: 0")
                    
                if "health" in resume_reference:
                    health_score = resume_reference.count("health")
                    print("Your Score for Health Care is: " + str(health_score))
                
                else:
                    print("Your Score for Health Care is: 0")
       
            else:
                print("Application is missing vital Keywords:")
                #cVect.get_feature_names - printing this method will return strings of both sets
                 
                string_1 = resume 
                string_2 = resume + jobdescription

                # First split your strings into sets of words
                set_1 = set(string_1.split())
                set_2 = set(string_2.split())

                # Compare the sets to find where they both have the same value
                
                differences = set_2.difference(set_1)
                print(*differences)
                
                print("However  You Have These Keywords Matched:")

                string_1 = resume
                string_2 = jobdescription

                # First split your strings into sets of words
                set_1 = set(string_1.split())
                set_2 = set(string_2.split())
    
                # Compare the sets to find where they both have the same value
                matches = set_1.intersection(set_2)
                print(matches)
                
                print("Your Resume is Optimised for these Industry")
                print("Each Industry is rated out of 10")
                
                if "quality" in resume_reference:
                    quality_score = resume_reference.count("quality")
                    print("Your Score for Quality Assurance is: " + str(quality_score))
                
                else:
                    print("Your Score for Quality Assurance is: 0")
                    
                if "operations" in resume_reference:
                    operations_score = resume_reference.count("operations")
                    print("Your Score for Operations is: " + str(operations_score))
                
                else:
                    print("Your Score for Operations is: 0")
                    
                if "inventory" in resume_reference:
                    supply_score = resume_reference.count("inventory")
                    print("Your Score for Supply Chain is: " + str(supply_score))
                
                else:
                    print("Your Score for Supply Chain is: 0")
                    
                if "administration" in resume_reference:
                    project_score = resume_reference.count("administration")
                    print("Your Score for Finance is: " + str(project_score))
                
                else:
                    print("Your Score for Finance is: 0")
                    
                if "programming" in resume_reference:
                    data_score = resume_reference.count("programming")
                    print("Your Score for Data Analytics is: " + str(data_score))
                
                else:
                    print("Your Score for Data Analytics is: 0")
                    
                if "health" in resume_reference:
                    health_score = resume_reference.count("health")
                    print("Your Score for Health Care is: " + str(health_score))
                
                else:
                    print("Your Score for Health Care is: 0")
                
