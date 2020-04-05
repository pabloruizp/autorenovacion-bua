# UA Share

**Name of the repository:** UAShare_ARA

**Members of the group:**

[Ignacio Encinas](https://github.com/IEncinas10)

[Ernesto Martínez](https://github.com/ecomaikgolf)

[Pablo Ruiz (coordinator)](https://github.com/pabloruizp)

**Group:** ARA
## 1. Description 

UA Share is a web application that lets students upload materials related to their university courses that they want to share with classmates. The idea is to provide a ‘Group’ that limits material’s visibility so that the students can share only with specific people. Those uploaded materials will be classified by degree and subject. Users will also have the option to mark some materials as favourite to track specially important materials. 

## 2. Public part 

* **Let the user login and register:** a non-registered user can login or create a new account in the frontpage
* **Show only public material:** a non-registered user can access materials listed public
* **Filter materials:** when a non-registered user wants to view public accessible materials, he/she can filter them by subject, course, etc.
* **Show subjects and degrees:** a non-registered user has access to a list of supported subjects and degrees of University of Alicante

## 3. Public EN List 

* **ENGroup:** Provide visibility to materials.
* **ENSubject:** Subjects of the different degrees
* **ENDegree:** Different degrees that the university offers
* **ENMaterial:** Different documents related with the subjects

## 4. Private part 

* **Upload materials:**  Users can upload materials 
* **Create groups:** Users can create groups to share materials among specific groups of people.
* **Add favorites:** Users can mark materials to track them
* **Score materials:** Users can provide feedback and score materials 
* **Modify user profile:** Users can provide a little description, add a profile photo and enroll groups.

## 5. Private EN List
* **ENStudent:** One student can upload documents, create groups, save documents as favorites
* **ENTeacher:** Teacher can be associated with uploaded materials
* **ENFavorites:** One student can have multiple documents as favorites 
* **ENGroup:** Provide visibility to materials.
* **ENSubject:** Subjects of the different degrees
* **ENDegree:** Different degrees that the university offers
* **ENMaterial:** Different documents related with the subjects

## 6.	Possible improvements

**Google ADS**  
Implement Google ADS in the webpage by creating a Google Ads API Key and linking the API Key to our Google Ads iframes.

**Scores**  
Let the students score materials.

**Multiple languages**  
Translate the webpage to different languages (Spanish, English, Catalonian) and implement a selector to choose the desired language.

**Server hosting**  
Host the web page and database on a server to be available through a public IP address. Perhaps managing the server to perform automatic backups, etc.

**Custom domain**  
Create a DNS A entry and expand it to popular DNS servers so the webpage can be accessed through a domain instead of a IP address.

**Basic security checks**  
Check user malformed input in forms to avoid common web vulnerabilities like SQL-Injection, etc.
