# filesize_location_report
Python project that searches for directories that are larger than a specified size

This is a project that recursively searches for directories that are larger than a size specified in the currently unpolished GUI. I made this so I could quickly search and find what areas on a disk are taking up significant memory.

Occasionally the python's os library this program is using (or at least how I am using it) will run into a FileNotFoundError with files that the os had just confirmed to be there without a FileNotFoundError. If/when I find a solution for this, I will update this project accordingly.
