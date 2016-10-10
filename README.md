Info:-
  Web scraping of academic institutes to find out the current projects running or the areas of research under the profs to find   the desirable and suitable project for an Internship!
  The aim is to:- Automate the pain of finding your project(OR Academic Internship) of interest and returning you the correct Prof. details along with their Contact infos. or mail-id!

Links:-
  Website :- http://internfinder.herokuapp.com/
  
Future Prospects Of the Project:-
  The project has been done for Electrical Engineering Department and for now shows results sourced from IIT-Bombay,IIT-Delhi,IIT-Roorkee,IIT-Madras,IISC-Bangalore. Further the project can be extended to more universities/colleges both domestic and foreign universities meeting the demands of Students. And also the project can be extended for various other departments!
  
Dummy Inputs:-
    College                 Area                        Department
1)  IITD                    VLSI                        EE
2)  IITB                    Signal Processing           EE
3)  IITM                    Image Processing            EE
  
Microsoft Service Used:-
---BING TEXT ANALYSIS API---
  Location(File Name)- Intern-Finder/intern/api.py 
  use- To failsafe different inputs in the area field TEXT ANALYTICS is used which returns the key phrases from a string which has been further deployed to our search algorithm for a possible match!
  
BUGS:-
  1)The field of college should be exactly filled as follows:-
    any lower and upper case combinations of the string(Exact String)- "IITD","IITB","IITR","IITM","IISC"! 
