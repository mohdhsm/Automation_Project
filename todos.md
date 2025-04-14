# GOAL:
1. KPI's AND REPORTS:App to connect to services such as pipedrive and excels and generate kPI's and connect to deepseek AI and generate reports and emails them to people.
2. App to connect to firefliy AI transcription services to download the transcript of meetings, store in database and connect to microsoft outlook and send it to partpicants via email.
3. Scheduled Reports: Every certain intervals it will connect to supabase and to microsoft email to send follow up report.  
3. Monitor some information in realtime (Streaming on one of my screen) (Needs to figure out how to do that)
4. It shoud be visually appealing so i will be using rich to enhance the visuals.
5. I will be using supabase for database, so it can be used on different PCs to avoid syncing problems. 
6. Tasks that will be

# TO START 
The beginning will be a very small application that can do small useful things as a starter. 

1. Keep following up with my tasks and projects, keep a database to keep track of progress and how many times it has been and deadline.
    1. Keep a database of delegated tasks, this should include created date, deadline date, and how many times follow up and progress note. 
    2. Create and maintain a database of overall organizational goals: this includes the overarching goals, it should include the names of the people involved, and progress, and next check up and deadline, and notes that contains progress report (Text entries that shows what kidn of progress happened)
2. Store meeting notes in it, so the meeting notes will be transcribed using external application and should be put in a file where it can read it.(Just a folder that I will be adding meeting notes on myself, the application has to read it and create progress reports add follow up tasks).
    1. There are two types of meeting, one to ones and group meeting.
    2. For one to ones, each employees would have his notes, and current progress, and current summary of what happened last meeting and it should read the previous meeting using deepseek API and come up with a small summary. IT should keep track of frequency of meeting with that person. 
    3. For group meeting, it should includes the names of the people in that meeting and thier emails do it may send the report to. 
    4. The meetings will be transcribed using OTTER.AI, and will be added as a text file in the app meeting folder. The app should be able to read that file. 
3. Connect to pipedrive, launch API calls, create KPI's, follow up with latest deals and activities, make summaries daily and weekly. 
    1. Most important is that be able to generate a daily report, that shows every sales person with the following: "Activities he completed today, deals that he has updated today, number of current deals under his name, number of stalled deals that havent been updated in one month" this with the comprasion of last month (Again, AI should generated this report in the form of a text file)
    2. Generate a weekly overall report that has the first part general information and then detailes for each sales person, it should have the following information:
        1. General report
4. Connect to pipedrive every 5 minutes, to stream data on it, any new deals or activities. There are two types of information, deals related and activity related.
    1. Check any API's that could connect, then set a loop to check any new information and compare it with the last date it checked.
    2. Display the new information on the screen.
        1. It should use colors and tabs using library rich. 
        2. It should stream it like a news list. whenever there is something new, it should just show underneath it. 
        3. The newer should be bottom, and the highest should be the older. 
        4. When it reaches more than 10, it should delete the oldest, so like a stack.
    3. Check the new deals that have done later than the date of last checked? (Is this technique correction?)
        1. It has to log the number of time checked and keep it somewhere (the last checked)
        2. Everytimes it connects, any old information shouldnt be displayed, and query on any activities or updates that are later the "last time checked".
5. Reminds employees about meeting, and send them what happened last time. (Connect to microsoft outlook API to send the emails and read the emails)
6. Connect to excel using microsoft API to read data from it, and update the excel sheet when needed, and create reports.
6. Generate weekly reports from this information (no need for graphs at the mean time, text will be suffice. 

# FUNCTIONAL REQUIREMENTS
## TASKS

## GOALS
## PIPEDRIVE REPORTS

## GOALS AND PROJECTS MANAGEMENT



# TODOS
## Connections First
1. Create the template files and file structure.
2. Connect Deepseek API sucesfully for AI integration. 
3. Connect to Pipedrive using API. 
4. Connect to microsoft API and access excel and email. 
5. Connect to microsoft API and access teams. 
6. Connect to fireflies ai api to retrieve the meetings and the meeting notes. 



# Database schemas that will be implemented.
These will be created using supabase.

== TASK TABLE ==
ID : UUD : Task ID
title(Text): Text title 
Description(Text) : Task title
Created_at(Timestamp) : Task creation date
deadline(timestamp): Time of the deadline of that task
assigned to(UIUD -->Foreign Key: employees.id): Who the task is assigned to
Follow_up_Count(Int): How many times we had to follow up with
Progress Note(UUID --> Foreign key: Notes.ID[]): Array of foreign id refering to the notes
Status(text): Shows the status of the task (pending, on progress, blocked or done)

== NOTE TABLE ==
ID: UUID (PK): Notes ID
Content(text): Content of the notes in text
Created_at(Timestamp): Date of creation
Task ID(UUID FK--> Task ID): To refer to the task ID
Goals ID(UUID FK --> Goals): To refer to the Goals ID

== GOALS ==
ID( UUID PK): This is the goal ID
title(Text): goal title
Description(text): The description of the goal
created_at(Timestamp): Creation date
deadling(timestamp): Deadline
Progress(int): the percentage of completion
Progress_summary(string): This contains the progress, to be overwritten
Next_Checkup(Datetime): The date of the next check up
Notes(UUID FK [] ): an array to refer to a list of notes. 
Contributors( UUID FK []): an array of ids refer to the employees.id

== EMPLOYEES == 
ID(UUID ): ID of the employee
Name(string): Name of the employees
Email (String): Email of the employee
Created_at(Datetime): Timestamp of when that employee was created. 


== MEETING TABLE ==
ID(UUID): The meeting ID
Meeting_Type(String): Either one on one or group
date(timestmap): Date of the meeting, should be inserted and not automated.
Summary(String): Should be the AI generated summary of the meeting
created_at(timestamp): automatically timestamped when the date was created.
meeting_partpicants(UUID FK of employees): This links the employees who were i

== apI sync log ==
This table keeps detailed information about the sync
ID (UUID): The id of the request
source(string): the source pipedrive, microsoft, fireflies ..etc
last_checked(datetime): when it was last checked


# FILE STRUCTURE
mycli_app/
│
├── main.py                         # Typer CLI entry point
├── config.py                       # Configuration constants & env vars
├── requirements.txt                # Python dependencies
├── .env                            # API keys, Supabase URL, etc.
│
├── cli/                            # CLI command groupings
│   ├── tasks.py                    # Commands related to tasks
│   ├── meetings.py                 # Commands related to meetings
│   ├── sales.py                    # Commands related to Pipedrive
│   └── reports.py                  # Generate daily/weekly reports
│
├── controllers/                   # Orchestrates between data & views
│   ├── task_controller.py
│   ├── meeting_controller.py
│   ├── sales_controller.py
│   └── report_controller.py
│
├── models/                         # Business logic models
│   ├── base.py                     # Shared base model (CRUD utils)
│   ├── task.py
│   ├── goal.py
│   ├── employee.py
│   ├── meeting.py
│   ├── sales.py
│   └── sync_log.py
│
├── views/                          # Rich renderers for CLI
│   ├── task_view.py
│   ├── meeting_view.py
│   ├── sales_view.py
│   └── streaming_view.py
│
├── services/                       # External service integration logic
│   ├── pipedrive_service.py
│   ├── outlook_service.py
│   ├── supabase_service.py
│   ├── deepseek_service.py
│   └── otterai_service.py
│
├── utils/                          # Utility functions
│   ├── file_loader.py              # Loads meeting transcripts
│   ├── time_utils.py
│   └── logger.py
│
└── data/                           # Local cache or meeting transcript folder
    └── meetings/





This an app to 