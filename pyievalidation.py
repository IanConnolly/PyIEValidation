# vim: set expandtab, tb=4, shiftwidth=4

"""
Collection of functions for validating Irish (Republic of Ireland) bank account numbers, PPSN, phone numbers, post codes etc.

Original idea and phone & post code regex taken from PHP lib "Validate_IE" by Ken Guest (ken@linux.ie) and David Coallier (davidc@php.net)
Link = http://pear.php.net/package/Validate_IE/docs/latest/Validate_IE/Validate_IE.html

@author = Ian Connolly
@email = connolim@tcd.ie
@license = MIT

"""

import re
import string

def validate_bank_acc(in_accno):
    """ Validates Bank Account No. format """
    
    if re.match("\d{8}", in_accno) is not None:
        return True
    else:
        return False

def validate_iban(in_iban):

    """ Validates IBAN numbers for Irish bank accounts """
    check_iban_less_bank = in_iban[8:] + "181400"
    bank = in_iban[4:8]
    bank_num = ""
    for char in bank:
        bank_num = bank_num + str(int(string.uppercase.index(char))+10)
    check_iban = bank_num + check_iban_less_bank 
    
    checksum = 98 - get_mod97_10(check_iban)
    if checksum < 10:
        checksum = "0" + str(checksum)
    else:
        checksum = str(checksum)

    if checksum == in_iban[2:4]:
        return True
    else:
        return False

def get_mod97_10(in_iban):
   
    checksum = int(in_iban[0])
    for char in in_iban[1:]
        checksum = checksum * 10
        checksum = checksum + int(char)
        checksum = checksum % 97
    return checksum


def validate_ppsn(in_ppsn):
    
    """ Validates Irish Personal Public Service Number or PPSN (Irish equivelant of Social Security no.)"""
    
    check = in_ppsn[-1]
    i = 8; sum = 0
    
    for char in in_ppsn[:-1]:
        sum = sum +  int(char)*i
        i = i - 1
    
    mod =  sum % 23
    
    if string.lowercase[mod-1] == check.lower():
        return True
    else:
        return False

#def validate_phone():

#def validate_post_code():

#def validate_passport():

#def validate_drivers_license():

#def validate_license_plate():

#def validate_vat_number():

def validate_cao_number(in_num):

    """ Validates CAO number format"""

    if re.match("\d{8}", in_num) is not None:
        return True
    else:
        return False
