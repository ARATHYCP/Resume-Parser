#!/bin/python

### How to use the program?

# $ python resume_parser.py ./Resume2/resume.txt
# Name: Arun
# Address:  Kalayatholil (H) Kadumeni PO Kozhikkode District, Kerala
# E-Mail: arunnithyanandkz124777@gmail.com
# Ph No:  7907284971,8086556705

import string
import re
import sys

class ResumeExtractor():
    '''
    Resume Extractor constructor
    '''
    def __init__(self,filename):
        self.filename = filename
        self.ph_regex = ["[C|c]ontact [N|n]o:(.+)", "Phone:(.+)"]
        self.load_resume()

    '''
    To load resume from the file passed via command-line argument
    '''
    def load_resume(self):
        with open(self.filename,'rb') as f:
            self.content = [line.decode('utf8').replace('\t', '').replace('\n', '') for line in f.readlines()]

    '''
    To return candidate name from the Resume
    '''
    def get_name(self):
        for item in self.content:
            name_match = re.match("[N|n]ame[\s|\t]*:[\s|\t]*(\w+)", item)
            if name_match:
                self.name = name_match.group(1)
                return self.name
        # Returning the header of resume as name if no matching found
        return self.content[0]

    '''
    To return candidate address from the Resume
    '''
    def get_address(self):
        for item in self.content:
            address_match = re.match(".*Address.*:(.+)", item)
            if address_match:
                self.address = address_match.group(1)
                return self.address
        return "Not Available"

    '''
    To return candidate email address from the Resume
    '''
    def get_email(self):
        for item in self.content:
            email_match = re.match("E[-]*mail[\s]*:[\s]*(.+)", item)
            if email_match:
                self.email = email_match.group(1)
                return self.email
        return "Not Available"

    '''
    To return candidate phone number from the Resume
    '''
    def get_ph(self):
        for item in self.content:
            for ph_regex in self.ph_regex:
                ph_match = re.match(ph_regex, item)
                if ph_match:
                    self.ph = ph_match.group(1)
                    return self.ph
        return "Not Available"

if __name__ == "__main__":
    file_name = sys.argv[1]
    resume = ResumeExtractor(filename = file_name)
    print("Name: {}".format(resume.get_name()))
    print("Address: {}".format(resume.get_address()))
    print("E-Mail: {}".format(resume.get_email()))
    print("Contact No: {}".format(resume.get_ph()))
