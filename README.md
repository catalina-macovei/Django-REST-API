# Django-REST-API :rocket:
## Goal
Created a Rest API app to handle main activities in a hospital involving: Doctors, Patients, Assistants, and Treatments. The system should manage all those activities with the corresponding security in place. The ACL will contain 3 main roles: General Manager (has access to all activities), Doctor (has access to all his patients and can define new ones), and Assistant (has access to allocated patients, one patient can have multiple assistants).
Any management module, like Doctor Management, Patient Management ..., should have CRUD capabilities