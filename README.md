# OWNHUSHED
Set permissions on program files
## Python 3.8
## Abstract
Different programs and files require different levels of security. Depending on their contents, this can range from a=x clearance all the way down to no access custom encrypted data. This project will set the permissions of any input file with possible securities as listed below.
## Securities
Unix-based OS's use custom permissions for different users. This can be modified with the `chmod` command. On top of that, if the clearance is such high priority, the root user should not have access to it, then the file should be encrypted with PGP. On top of that, a TOTP code can be added for even more protection.

| Permission | Description               |
| ---------- | :------------------------ |
| A          | rwx-rwx                   |
| R          | rwx-r--                   |
| P          | rwx----                   |
| S          | encrypted                 |
| T          | encrypted + TOTP required |
## Encryption Standard
- By default the algorithm employs GnuPG from the command line. You will have to have already created a keypair in order to specify it in the program.
- TOTP is specified by [RFC6238](https://tools.ietf.org/html/rfc6238)
## TODO
- Implement S and T security