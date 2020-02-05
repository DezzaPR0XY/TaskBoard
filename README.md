# TaskBoard [Name TBD]
* [Wireframe](https://wireframe.cc/XxgW6y)

This is a solo Django project to create a task board that aims to be ***super clean, simple, flexible, manipulatable, and organized***, and users will have the capability of **inviting others to join a task board** that you are part of.
__________
__________
## Key Features

* Tasks and Task manipulation
* Multi-User Access for a Task List
* Task List View
* Task Board View - Optional
* Task Calendar View - Optional
* Login
  * Google OAUTH API - Optional
* Friends/Group - Optional
  * Friends/Group chat - Optional
* User Task List Perms - Optional
* Archive/Complete Tickets
* Detailed Tickets
* Filterable and Orderable - Optional (Shouldn't effect Priority when active)
__________
__________
## Brainstorm

* Radio Input Status (Done, Hold, To Do, In Prog)
* How to setup DB (Maybe use Fire Base)
* How to organize Priority
  * Ideas
   1. When onChange(), reassign the order for tickets *probably going with this one*
__________
__________
## To Do

* Update Wireframe
* Add new page for archived tasks
* Create HTML
* Create Routes
* Setup CSS
* Setup DB
 1. Tasks Table
 1. Tasks_Lists Table
 1. Task_Board Table
 1. Tags Table
 1. Status Table
 1. Users Table
 1. Users_to_Lists_Perms Table (many-to-many)
__________
__________
## Detailed Features

* Board View>Tags/List View>Tags are editable
* Details page has editable fields
* Can comment on ticket in editable page
* Invite other users to a task list
* Archive tickets (removes them from list)
* Complete tickets (doesn't remove tickets)
* Color Coordinated - Optional
* Created/Completed Date
* Assign Priority to Tasks when creating new tickets
* Tasks have assigned users
