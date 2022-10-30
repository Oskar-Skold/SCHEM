# SCHEM
This program is created to easily be able to share schedules in one central place. It is created to be used by the students of Chalmers University of Technology.

The goal of this program is to have a simple and easy interface where students can subscribe to different schedules that can be synced to their Google Calendar. The interface will also have a search function where students can search for schedules that they are interested in.

Another goal is to have a simple way for students to get recomendations of schedules that they might be interested in. This will be done by using data that the students' have already subscribed to.

Every student section will have their own page where students easily can see the schedules that are related to their section.

The data of the schedules will be stored in a database that will be easy to update and maintain. (Probably just a json file for each schedule)<<<<<<>>>>>>

The program is written in Python 3 and uses the following libraries:
* [Requests](https://pypi.org/project/requests/)
* [Numpy](https://pypi.org/project/numpy/)

Todo:
- [ ] Create a simple interface
- [ ] Add support for collecting iCal files
- [ ] Create an "standard" for the schedule files. All of the schedules should be able to be converted to this format.
- [ ] Create the ability to login with an Google account and syncronize the schedule with Google Calendar.
- [ ] Add support for collecting TimeEdit schedules
- [ ] Update the README.md file