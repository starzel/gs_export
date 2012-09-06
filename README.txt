GS Export
=========

GS Export is a little helper that dumps your GenericSetup profile
to a given directory, and sends you a mail, if anything has changed
since it was last run.

GS Export uses git to store the change history, it simply sends the result
of a ``git status -q`` if there are any changes.
It is your responsabilility to commit the changes, else you will get the
same notification on the next run.

GS Export always sends a passwort with each request, it is POST encoded
but it is still there. This also means, it needs basic auth working on your
plone site. You might want to run GS Export only on the same machine
as the zope client.

GS Export needs to be configured, and it needs a lot of options.
Since GS Export might be needed for many sites on one host, it does not
look for a configuration file with a fixed name, but you must provide
a configuration file as the first argument to the script.
This is a sample configuration. All arguments are required::

  [gs_export]
  base_url = http://yoursite:8080/Plone/portal_setup
  user = youruser
  password = yourpass
  path = /absolute_path_to_dump_diretory_of_git
  mail_server = your.mailserver
  mail_port = 587
  mail_user = your_mail_user
  mail_password= your_mail_pass
  mail_from = your_email_adress
  mail_mode = TLS
  mail_recipient=your_receiving_email_adress
  ignore = structure
      workflow

- base_url must point to portal_setup
- the path must exist
- mail_mode accepts an empty string, TLS and SSL
- This tool only accepts one mail recipient. This could easily by changed though
- ignore accepts multiple parameters. Ignore means, after dumping the
  configuration, the ignore parts are deleted! It is a good idea to ignore
  structure. Multiple values can be added by adding one for each line
  and indenting the elements

GS Export is intended to be run by a cron job. 

Todo
----
- Allow for multiple recipients.