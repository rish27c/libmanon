Libman Documentation – Rishabh, Kunal


### Overview

libman is a modular library management system designed for educational and small-scale use. It features user interaction, secure config handling, SQL database integration, and command-based automation.


### Components

Each file/module handles specific parts of the system:

 librr.py – Handles logging and debug messages
 libprocess.py – Handles basic encryption and compression of user credentials
 libdata.py – Manages reading and writing of configuration files
 liber.py – Processes user commands and controls advanced tools
 libman.py – Main program to start and manage the app
 libmanon.py – Standalone entry point to run the application (placed outside the main folder libset)


### Starting the Program

To start the application:

Run libmanon

### Authentication & Access

Some commands require authentication. If access is denied:

 Retry with:

  -p [password]
  ([password] is optional, system will ask for it, if [password] is not empty then it will directly pass through input)

 To change password even if authenticated:

  -cp [new_password]
  (Works same as "-p")

### Emergency Mode

Used when the config file is locked due to errors:

libman core:break->force [user]@[host]

This opens a restricted emergency shell.

 reset [flag]: Deletes and rebuilds the config
 update [field]: Updates fields (user, host, password, * (for all))

### Setup/Test Tools

Create/reset DB with test data:

  libman new-db-->on

Check DB connection:

  libman test

View hashed config info:


  libman conf_sec_rev [user|host|password|*]


### Core Privileges

Before using 'liber' or 'libql', run:

core [liber|libql] [argument]
Example: core liber check
(Only needed once per session.)

To view configuration or SQL table structures:

core show [config|sqldata]

#### Exiting & Restarting

Exit:

  exit / quit / bye / stop

Restart:

  relib

#### Help

liber libhelp


### `libql` Commands (Book & Student DB)

#### Reveal Data

libql reveal data [table_name]
(Default tables: libstudent, booklib)

#### Issue Book

libql issue [yyyy-mm-dd] [student_id] [book_name]
libql issue [student_id] [book_name]  # Uses previous date

#### Realign Book Counts

libql alignment check
libql alignment realign

#### Add Entry

libql add book [shelf] [book_name]
libql add student [id] [name]
(Leave arguments blank to enter interactively)

#### Remove (Transfer Record)

libql -tr student [id]
libql -tr book [name]

#### Search

libql search student (by name|book) [value]
libql search book booked [name|*]

Use '%' for wildcards, e.g. 'Ku%', '%ku'


### Developer Mode – `libql->inject`

Used only in dev/admin shell after authentication:

 Run SQL manually:

  curse SELECT * FROM booklib
  
 View logs:

  cat [index]
  kitty [index]  # Pretty display

### Notes

 Elevate authority using 'core' before restricted actions
 (liber and libql needs core elevation permit; Only once per session)
