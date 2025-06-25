This is documenttion on libman on, it is a software on library management

// logs and debugs are handled by librr
// data processing is handled by libprocess
// libdta bridges libprocess with user as the medium interface with config handler
// libman is the main program that is connects all other modules
// liber is the command handler

Commands:
  To exit: [Any related word]
    Example: Bye
  To restart: relib
  [main flag]: Calls main function from liber.py
    Flags: libman, liber, libql, core, slog
  If lib_auth_pkey_kk_login_varification fails, use "-p" as main flag for as reattempt
    Example: -p //(Then libman will ask for password)
      Example2: -p [password] //(Now the password will directly be passed into input)
  If you want to change password even though lib_auth_pkey_kk_login_varification check returns success then use "-cp" as main flag, it follow same format is "-p"
  In case of password typo in config, functions will lockdown and config is encrypted, then use emergency-mode
    Use: libman core:break->force [user]@[host] //replace [user] with user value like root and [host] with host value like localhost
      Example: libmn core:break->force root@localhost
    This will open emergency mode:
      [Flag]: update, reset
        rese [Any falg]: It will reset configuration
        update [sub-flag]: Updates specifig variable of coniguration //[sub-flag] includes 'user', 'host', 'password' and '*' for all, without quotes
  libman conf_sec_rev [sub-flag] //Same as above sub-flag
  Use: libman new-db-->on //For creating/overriding the tables(existing data) with test data

  Before useing liber or libql, use core to elevate authority
  Use: core [main flag] [argument]
    Example: core liber check
  //Only use it to unlock a function once, after the function has recieved elevated authority, it doesn't need core flag again
  You can also use: core show [flag] //[flag]: conf(or config), sql-data(or sqldata)

  libql reveal data [table_name] //Reveals table data, if use: 'libql reveal data' only then reveals libstudent and booklib table by default
  liql issue <[date](Optional)<Format:yyy-mm-dd>> [student id] [book name]
  //Example: libql issue [2005-06-28] 1120021 Atomic Habits
  //Example 2: libql issue 1120021 Atomic Habits //Doesn't change or update date value

  libql alignment [sub-flag] //[sub-flag]: check, realign
    check: checks for mismatch of data, use it to make sure that data is aligned
    realign: Auto realigns the data, (use it if you issue different book for a student) -> A student can only issue one book at a time
  libql add [sub-flag] [argument] //[sub-flag]: book, student
    [argument] can be left empty, the system will ask for data then
      OR [argument]: [book_shell/student_id] [book_name/ student_name]
  libql -tr [sub-flag] [argument] //[sub-flag]: student, book
    [argument]: [student_id/book_name]
  libql search [sub-flag] [category] [Value] //[sub-flag]: book, student
    For [sub-flag]=student; [category]: (by name), (book); [Value]: [student_name](If category is '(by name)'), [book_name](If category is '(book)'; If [book_name] is * then all students with books)
        //Ex:: Use: Ku% (in [student_name] to find a name starting from Ku or the string value in place of Ku); %ku for all names ending with ku or the string value in place of ku
    For [sub-flag]=book; [category]: (booked); Value: [book_name] (Same as above, but it finds books that are booked, * for all;;String value behaves same as above [Value])

  Use: liber libhelp //to use liber
  If you use libql->inject: //dev(admin) tool
    Use: curse [argument] //[argument]: Any; Like: Select * from booklib
    Use: cat [index] //To see output/logs, if [index] is empty then default value will be taken as -1
    Use: kitty [index] //Works same as cat but organizes table into neat display, may give cyptic output for normal logs
