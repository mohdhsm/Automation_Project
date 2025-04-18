# GOAL:

1. KPI's AND REPORTS:App to connect to services such as pipedrive and excels and generate kPI's and connect to deepseek AI and generate reports and emails them to people.
2. App to connect to firefliy AI transcription services to download the transcript of meetings, store in database and connect to microsoft outlook and send it to partpicants via email.
3. Scheduled Reports: Every certain intervals it will connect to supabase and to microsoft email to send follow up report.  
4. Monitor some information in realtime (Streaming on one of my screen) (Needs to figure out how to do that)
5. It shoud be visually appealing so i will be using rich to enhance the visuals.
6. I will be using supabase for database, so it can be used on different PCs to avoid syncing problems. 
7. The main objective of this app is to provide with daily and weekly and even hourly updates. For now, I am not interested in monthly updates that any of my staff can do. It should keep me updated on daily basis on the main things in our work. 

## INFORMATION THAT REQUIRES DAILY UPDATES WITH

1. Pipedrive daily information:
    1. Deals that have moved through the stages.
    2. Deals added.
    3. Notes that have been added.
    4. Activities that have been done. 
    5. Short summary report about everyone doing in today.
2. Daily and weekly goals: Since the focus app on the short term.
    1. Daily and weekly sales and visit report (customer visit report).
    2. Daily and weekly report on followup tasks.
    3. Daily and weekly reminders on commitment that been said on a meeting. 
3. Streaming log that summarizes all the information:
    1. Running every 5 minutes.
    2. It should be a while loop that is kept running on different terminal (maybe different application overall).
    3. 

## TO START

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

There are three functional requirements: User manual adding and removing tasks, retrieving tasks from firefly ai, automated tasks followup. 

1. User should view, edit and list tasks.
    1. COMPLETED Tasks now have both a UUID and sequential ID (starting from 1)
    2. DONE Users can reference tasks using either ID type in commands
    3. DONE Sequential IDs increment and persist (don't reset when tasks are deleted)
    4. TODO The user should be able to filter tasks based on the employees assigned to. (So a command should display the tasks grouped by the person assigned to)
2. Retrieving tasks from filefly AI:
    1. User should enter a command, after the command is initiated, the app will connect to firefly ai through an api call.
    2. The app then will download the transcript from the firefly and load it to its memory, then will be sent to deepseek to get a list of tasks to follow up with the user.
    3. After retrieving the list of tasks, it will be viewed to the user and asks for confirmation then it will be commited to supabase database to be edited later.
3. Automated tasks followup:
    1. The user will enter a command and that command will initiate automated tasks followup.
    2. The app will connect to supabase database, and based on this it will send follow up to each employee by using the employee's email that is in the database. 

## GOALS

For goals, we have progress and employees who are involved in this goals. The app should follow up and send periodical reports for these goals. 

1. TODO User should be able to view, edit, create the goals. Each goal should have both UUID and sequential ID
2. TODO Implement same ID system for goals as tasks (sequential IDs starting from 1)
3. TODO Each interval the app will send a reminder to adjust the progress of the goals.

## PIPEDRIVE REPORTS AND AUTOMATION

The pipedrive reports and follow ups will highly depend on the PIPEDRIVE HTTP REQUEST, the most important reports are three: Summary report, salespeople indivual report, and stuck and stalling deals.

### GOAL OF THE REPORTS

So the main goals that we're trying to tackle with is to make sure that:

1. Sales people are proactive with their deals not leaving the deals without contacting the client.
2. Collection, we usually finish and complete the job, but we dont get paid until we get the client to sign Material Delivery paper which is referred to (MDD) and sign good recives (GR).
3. Remind sales people to update their pipedrive and follow their clients.

### REPORTS AND INFORMATION

1. Summary report from pipedrive: which has the goal to provide the overall performance, and then the second part of this summary report will be a list of all sales people and summary of their
    1. The firdt report will contain the following information.
        1. Number of total deals (to date).
        2. the total value of deals (to date) compared from total value (to one month ago)
        3. value of deals compared with value of deals with active deals. Active deals are with date of the update being less than 2 months ago.
        4. Total value of deals that are done and still didn't recieve the payment (to date) compared to the same thing (to one month ago). (Deals that are under the stage "Awaiting MDD: which indicates deals that have been delivered, but waiting from the client to sign the Material Delivery paper, deals that are under stage "AWAITING GR: which indicates that material delivered paper were signed, but now awaiting from the client sign Good Recieved paper).
    2. The second part of the report will have a list of sales people and with each sales people will have the following numbers in the summary:
        1. Current pipeline value.
        2. Number of stalled or stuck deals.(current) compared with same (to month ago) (deals not updated 2 months ago).
        3. Total number of activities.(week to date) compared with last week.
        4. Total number of deals that are under staged Awaiting MDD, and awaiting GR.(to date) compared with the same (to one month ago) 
        5. Number of deals moved stages compared to last month.
        6. Number of deals won. compared to last month
        7. Numbers of deals lost. compared to last month.
2. Sales people detailed reports for each sales person: this is a more detailed snapshot report for each sales person that is detailed.
    1. Sales won deals value, to his target. (Quarter to date)
    2. latest 5 deals that were added.
    3. List of the stalled deals, and with thier last note entry. (not updated since 1 month ago).
    4. List of the deals that are won.
    5. List of the deals that are under stages (Awaiting MDD, Awaiting GR) which indicates deals that were done and awaiting client to sign on the material delivery and good recieved.
    6. Top 5 deals in terms of value, and thier latest note.
    7. The whole things should be fed to deepseek api, to generate a summary text.

### AUTOMATION AND EMAILS AND FOLLOW UP

1. Emailing and generating the summary reports with KPI:
    1. The app using api pipedrive, grab the information.
    2. the App converts the information to HTML, and format it.
    3. Sending email to the designated people.

2. Weekly sales indivual report
    1. Every week, the app gather information through API HTTP call.
    2. format the indivual sales report, format HTML.
    3. connect to outlook API, and send it to email.

## MEETINGS AND SUMMARIES

For this meeting, the app will be grabbing the transcripts and other informatoin from firefly AI through an HTTP REQUEST API call, and then store it in supabase database and then based on those meeting, using deepseek AI, the app will make summaries, follow up and make certain conclusion.

1. Retrieving meetings and storing it:
    1. connect to the firefly api and retrieve the meetings from there.

## Connections First

1. Create the template files and file structure.
2. Connect Deepseek API sucesfully for AI integration.
3. Connect to Pipedrive using API.
4. Connect to microsoft API and access excel and email.
5. Connect to microsoft API and access teams.
6. Connect to fireflies ai api to retrieve the meetings and the meeting notes.

## 1 NEXT TODOS (THIS IS THE CURRENT TODO LIST TO BE UPDATED DAILY BASED ON PROGRESS SHOULD HAVE ONLY 5 TODOS AT ALL TIME).

1. TODO Create the goals models similiar to the tasks with added progress.
2. TODO Create the goals view and controller.
3. TODO Connect the goals to the main app via the CLI command.
4. TODO Test the goals modules if it works.
5. TODO Create the pipedrive service layer. (NO API JUST CONNECTION). 


## Database schemas that will be implemented.
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
