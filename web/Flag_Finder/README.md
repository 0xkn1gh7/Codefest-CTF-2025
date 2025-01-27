# Flag Finder

> The challenge was authored by [savsch](https://iitbhucybersec.in/authors/savsch/)

Total Solves - 24

Final Points - 400

## Description
Made a simple utility for uploading files in a zip and storing on my server :)

Hopefully this will save some space on my local system.

## Attachment
- [server.zip](./attachment/server.zip)

## Writeup
The server unzips file into a directory served as static files. Also, the location of the unzipped file is known. The source code also hints at the flag being at /flag.txt. 

So a simple symlink (created using ln -s /flag.txt myfile.txt) zipped (using zip -y myfile.txt solve.zip) will do the job. Once this zip is uploaded, the flag is served at `GET /public/<md5sum_of_the_zip_just_uploaded>/myfile.txt`. 

There's a minor problem: the files don't stay for long (see the Singleton). But this too can be easily accounted for by issuing upload as well as get flag requests in quick succession.

## Flag
`CodefestCTF{symlinks_ftw_[a-zA-Z0-9]{8}}`