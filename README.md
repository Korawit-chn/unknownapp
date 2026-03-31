# unknownapp
This is an unknown application written in Java

---- For Submission (you must fill in the information below) ----
### Use Case Diagram
<img width="711" height="716" alt="image" src="https://github.com/user-attachments/assets/0a63785b-56a2-42a9-b6d0-e8a1e821c39a" />
### Flowchart of the main workflow
```mermaid

    flowchart TD
    A[Start] --> B{"Switch (login)"}

    B -->|Case 1| C[Student]
    B -->|Case 2| D[Admin]
    B -->|Case 3| E[Exit]

    E --> Z[End]

    F{"Profile Exists?"}
    G{"Switch (Student Menu)"}

    S1[View Course]
    S2[Register Course]
    S3[Drop Course]
    S4[View Schedule]
    S5[Billing Summary]
    S6[Edit Profile]
    S7[Logout and Save]

    C --> F --> |Yes| G
    F --> |No| H[New Profile] --> G

    G --> |Case 1| S1 --> Z
    G --> |Case 2| S2 --> Z
    G --> |Case 3| S3 --> Z
    G --> |Case 4| S4 --> Z
    G --> |Case 5| S5 --> Z
    G --> |Case 6| S6 --> Z
    G --> |Case 7| S7 --> Z

    I{"Switch (Admin Menu)"}

    A1[View Course Catalog]
    A2[View Class Roster]
    A3[View All Students]
    A4[Add New Student]
    A5[Edit Student Profile]
    A6[Add New Course]
    A7[Edit Course]
    A8[View Student Schedule]
    A9[Billing Summary]
    A10[Logout and Save]

    D --> I

    I --> |Case 1| A1 --> Z
    I --> |Case 2| A2 --> Z
    I --> |Case 3| A3 --> Z
    I --> |Case 4| A4 --> Z
    I --> |Case 5| A5 --> Z
    I --> |Case 6| A6 --> Z
    I --> |Case 7| A7 --> Z
    I --> |Case 8| A8 --> Z
    I --> |Case 9| A9 --> Z
    I --> |Case 10| A10 --> Z
    
 ```
### Prompts
prompt 1:
 * message: base on Main.java recreate Login case that have the same option in python language. Put the Python program in a new folder called “python.”
 * attachment: Main.java
