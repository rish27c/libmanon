Libman Documentation – Rishabh, Kunal

### Overview

libman is a modular library management system designed for educational and small-scale use. It features user interaction, secure config handling, SQL database integration, and command-based automation.
-> Run `libmanon.py` in libmanon folder

### Components

Each file/module handles specific parts of the system:

 `librr.py` – Handles logging and debug messages
 `libprocess.py` – Handles basic encryption and compression of user credentials
 `libdata.py` – Manages reading and writing of configuration files
 `liber.py` – Processes user commands and controls advanced tools
 `libman.py` – Main program to start and manage the app
 `libmanon.py` – Standalone entry point to run the application (placed outside the main folder libset)

### Authentication & Access

Some commands require authentication. If access is denied:

 Retry with:

  `-p [password]`
  ([password] is optional, system will ask for it, if [password] is not empty then it will directly pass through input)

 To change password even if authenticated:

  `-cp [new_password]`
  (Works same as "-p")

### Emergency Mode

Used when the config file is locked due to errors:

`libman core:break->force [user]@[host]`

(This opens a restricted emergency shell for error fixing. This info is purposely excluded from libman -help)

 `reset [flag]`: Deletes and rebuilds the config
 
 `update [field]`: Updates fields (user, host, password, * (for all))

### Setup/Test Tools

Create/reset DB with test data:

  `libman new-db-->on`

Check DB connection:

  `libman test`

View hashed config info:


  `libman conf_sec_rev [user|host|password|*]`


### Core Privileges

Before using 'liber' or 'libql', run:

`core [liber|libql] [argument]`
(Only needed once per session.)

To view configuration or SQL table structures:

`core show [config|sqldata]`

#### Exiting & Restarting

Exit:

  **exit / quit / bye / stop**

Restart:

  `relib`

#### Help (for LIBER)

`liber libhelp`


### `libql` Commands (Book & Student DB)

#### Reveal Data

`libql reveal data [table_name]`
(Default tables: libstudent, booklib)

#### Issue Book

`libql issue [yyyy-mm-dd] [student_id] [book_name]` #Date should be inside '[' and ']', example: *libql issue [2025-06-25] 1120012 Computer Science*
                       OR
`libql issue [student_id] [book_name]  # Uses previous date`

#### Realign Book Counts
Run this command after every change in database

`libql alignment check` #Checks mistmatch

`libql alignment realign` #Corrects mismatch

#### Add Entry

`libql add book [shelf] [book_name]`

`libql add student [id] [name]`

(Leave arguments blank to enter interactively)

#### Remove (Terminate Record)

`libql -tr student [id]`
`libql -tr book [name]`

(Unlike add, lacks interactive shell, it is an intentional design to prevent accdiental deletion of data)

#### Search

`libql search student (by name|book) [value]` #Value '*' in '(book)' displays name of all students with books while '(by name)' flag uses '%' for wide searches, e.g. 'Ku%' (For name starting with 'Ku'), '%ku' (For name ending with ku) [can also use '_' as placeholder]

`libql search book booked [name|*]` #Value '*' will show all the booked books(Make sure you use realign flag before search to prevent errors)


### Developer Mode – `libql->inject`

Used only in dev/admin shell after authentication:

 Run SQL manually:

 `curse [**arg]` #[**arg]: For sql argument injection
 
  eg: curse SELECT * FROM booklib
  (For fetching all booklib data)
  
 View logs:

  cat [index] #For raw display of output logs
  kitty [index]  # Pretty display (Only for fetched data)

### Notes

  **Elevate authority using 'core' before restricted actions**
  
 (*liber and libql needs core elevation permit; Only once per session*)
