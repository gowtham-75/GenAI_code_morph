user_stories = """
**Introduction and Role**:  
   - "You are a software engineering assistant with expertise in transforming legacy PL/SQL applications into modern,
     scalable Java microservices using Domain-Driven Design (DDD) principles. 
     I have a PL/SQL codebase composed of multiple files, each containing complex business logic implemented via PL/SQL procedures, functions, and triggers."

**TASK** : Analyze the entire PL/SQL code below and create **Different user stories** that capture the purpose, key operations, and intended outcomes of each distinct function,
 procedure, or trigger. Each user story should include specific details such as an ID, title, requirements, description, acceptance criteria, and validations.

**PL/SQL Code**:
``` {PLSQL_CODE} ```

  The output should be in JSON format with the following structure:
- **User Stories**: An array of user story objects, each containing the following fields:
- **id**: A unique identifier for each user story.
- **title**: A concise title summarizing the function or feature provided by each code component.
- **requirements**: Outline any dependencies or specific requirements for this function (e.g., input data types, permissions).
- **description**: A list of statements describing the primary purpose and high-level actions of the function or procedure (e.g., "Updates account balances", "Validates customer orders").
- **acceptance_criteria**: A list of specific conditions or rules the code enforces based on its logic (e.g., input validation rules, calculations, required conditions for successful execution).
- **validations**: A list of statements describing validation checks or constraints the code applies, ensuring accuracy, data integrity, and adherence to business rules.

Each user story should focus on a single component (e.g., function, procedure, trigger) of the PL/SQL code and should follow this JSON format:

```json Format:

  "id": "Generate Unique ID eg.(001,002)",
  "title": "<title describing the code component",
  "requirements": "<dependencies or prerequisites",
  "description": ["<description statement 1", "<description statement 2", ...],
  "acceptance_criteria": ["<criteria statement 1", "<criteria statement 2", ...],
  "validations": ["<validation statement 1", "<validation statement 2", ...] ```



   - Output should be in JSON format with the following keys: id, title,requirements, description, acceptance_criteria, validations.
   - Do not give any additional information other than the JSON ouput.
"""



extract_json = """
- Your task is to identify and extract JSON objects from the provided text.
- Extract all JSON objects from the provided text. 
- Combine all extracted JSON objects into a single list **User Stories** and return only the JSON data in the following format:

Text for extraction:
```{text}```

**output Formate**:
[
   <JSON object 1,
    <JSON object 2,
    ...
    <JSON object n
]
- Do not give any additional information other than the JSON ouput.

"""

code_gen = """


Generate complete Java Spring Boot microservice code for the following user stories. Each user story includes detailed requirements, acceptance criteria, and validations:
UserStories : {user_stories}

 - **Instructions:**
   - For each user story provided, create the necessary components of a microservice including:
     - **Model**: Define entity models with appropriate fields.
     - **Repository**: Create repository interfaces for CRUD operations based on the model.
     - **Service**: Implement service classes that handle business logic, validation, and database interactions.
     - **Controller**: Develop RESTful API endpoints that fulfill the user story requirements, with HTTP methods such as `GET`, `POST`, `PUT`, and `DELETE`.
     - **Exception Handling**: Implement global exception handling to manage errors and return relevant HTTP status codes based on the user stories’ acceptance criteria.
     - **DTOs** (Data Transfer Objects) if needed: For handling request and response objects.
   - **Database Configuration**: Include a basic configuration in `application.properties` for a MySQL database.
   - **API Documentation**: Provide sample API requests and responses for each endpoint, with success and error scenarios.


 - **Expected Output**:
   - End-to-end Java Spring Boot code that satisfies each user story’s requirements and acceptance criteria.
   - Classes for `Model`, `Repository`, `Service`, `Controller`, and `Exception Handler` as needed.
   **NOTE**: generate only java code. Do not give any additional information other than the Java code.
   
  **Output Formate**:
  usecase : Name of the usecase
  ```java
  <Java code>
  ```

"""

#  - **Instructions:**
#    - For each user story provided, create the necessary components of a microservice including:
#      - **Model**: Define entity models with appropriate fields.
#      - **Repository**: Create repository interfaces for CRUD operations based on the model.
#      - **Service**: Implement service classes that handle business logic, validation, and database interactions.
#      - **Controller**: Develop RESTful API endpoints that fulfill the user story requirements, with HTTP methods such as `GET`, `POST`, `PUT`, and `DELETE`.
#      - **Exception Handling**: Implement global exception handling to manage errors and return relevant HTTP status codes based on the user stories’ acceptance criteria.
#      - **DTOs** (Data Transfer Objects) if needed: For handling request and response objects.
#    - **Database Configuration**: Include a basic configuration in `application.properties` for a MySQL database.
#    - **API Documentation**: Provide sample API requests and responses for each endpoint, with success and error scenarios.


#  - **Expected Output**:
#    - End-to-end Java Spring Boot code that satisfies each user story’s requirements and acceptance criteria.
#    - Classes for `Model`, `Repository`, `Service`, `Controller`, and `Exception Handler` as needed.