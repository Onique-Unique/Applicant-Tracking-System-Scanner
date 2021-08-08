#" IMPORT ALL REQUIRED MODULES NEEDED FOR THIS APPLICANT TRACKING SYSTEM"
#" IMPORT DOCX2TXT MODULE TO CONVERT DOCX FILES INTO A CONSUMABLE TEXT FORMAT"

import docx2txt
import sys 
from pdf2docx import Converter
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

#" CREATE A VARIABLE TO PULL PDF RESUME SOURCE/ DESTINATION FILE"
#" CREATE A VARIABLE TO DEPOSIT/ SAVE PDF TO DOCX CONVERTED RESUME SOURCE/ DESTINATION FILE"

print("Welome To Free ATS Scanner Please Enter Your Name")
name = input()

print("Hello " + name + " Let's Get Started")

while True: 
    print("Is Your resume and job description in PDF format? type 1 for YES! 2 for NO! q to exit")   
    Press = int(input())
    for Choice in range(1):
        if Press == 1:
            print("Copy PDF Resume Name Here")
            PDFresume = input()
            pdf_file = r"C:\Users\kiddo\OneDrive\Desktop\Automate Codes 1 -6/" + PDFresume + ".pdf" # source file
            docx_file = r"C:\Users\kiddo\OneDrive\Desktop\Automate Codes 1 -6/" + PDFresume + ".docx"  # destination file
            
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
            # convert job description pdf to docx if any
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

            resume_reference = resume
            job_reference = jobdescription
            compare = [resume_reference , job_reference]
            cVect = CountVectorizer()
            count_matrix = cVect.fit_transform(compare)

            matchPercentage = cosine_similarity(count_matrix)[0][1] * 100
            matchPercentage = round(matchPercentage, 2)
            print("Your resume matches about " + str(matchPercentage) + "%" + " of the job description")

            if (matchPercentage >= 50 < 85):
                revised_sum = matchPercentage + 15
                print("Press Enter To See Your Resume Complete Optimised Score")
                Enter = input()
                print("Your Total Resume match score is " + str(revised_sum) + "%")
                
            elif (matchPercentage >85):
                print("You Have Achieved A Great Match Score ")

            else:
                print("Application is missing vital Keywords")

                string_1 = resume 
                string_2 = resume + jobdescription

                # First split your strings into sets of words
                set_1 = set(string_1.split())
                set_2 = set(string_2.split())

                # Compare the sets to find where they both have the same value
                
                differences = set_2.difference(set_1)
                print(*differences)
                
                print("However  You Have These Keywords Matched")
                string_1 = resume
                string_2 = jobdescription

                # First split your strings into sets of words
                set_1 = set(string_1.split())
                set_2 = set(string_2.split())

                # Compare the sets to find where they both have the same value
                
                matches = set_1.intersection(set_2)
                print(matches)
       
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

            resume_reference = resume
            job_reference = jobdescription
            compare = [resume_reference , job_reference]
            cVect = CountVectorizer()
            count_matrix = cVect.fit_transform(compare)

            matchPercentage = cosine_similarity(count_matrix)[0][1] * 100
            matchPercentage = round(matchPercentage, 2)
            print("Your resume matches about " + str(matchPercentage) + "%" + " of the job description")

            if (matchPercentage >= 50 <85):
                revised_sum = matchPercentage + 15
                print("Press Enter To See Your Resume Complete Optimised Score")
                Enter = input()
                print("Your Total Resume match score is " + str(revised_sum) + "%")
            
            elif (matchPercentage >85):
                print("You Have Achieved A Great Match Score ")

            else:
                print("Application is missing vital Keywords")
                #cVect.get_feature_names - printing this method will return strings of both sets
                 
                string_1 = resume 
                string_2 = resume + jobdescription

                # First split your strings into sets of words
                set_1 = set(string_1.split())
                set_2 = set(string_2.split())

                # Compare the sets to find where they both have the same value
                
                differences = set_2.difference(set_1)
                print(*differences)
                
                print("However  You Have These Keywords Matched")

                string_1 = resume
                string_2 = jobdescription

                # First split your strings into sets of words
                set_1 = set(string_1.split())
                set_2 = set(string_2.split())
    
                # Compare the sets to find where they both have the same value
                matches = set_1.intersection(set_2)
                print(matches)
                
        q = sys.exit() 
        if Press == q:
            sys.exit()
               
