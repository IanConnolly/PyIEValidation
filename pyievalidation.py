# vim: set expandtab, tb=4, shiftwidth=4

"""
Collection of functions for validating Irish (Republic of Ireland) bank account numbers, PPSN, phone numbers etc.

Original idea from PHP lib "Validate_IE" by Ken Guest (ken@linux.ie) and David Coallier (davidc@php.net)
Link = http://pear.php.net/package/Validate_IE/docs/latest/Validate_IE/Validate_IE.html

@author = Ian Connolly
@email = connolim@tcd.ie
@license = MIT

"""

import re
import string


def validate_bank_acc(in_accno):
    """ Validates Bank Account No. format """

    if re.match("\d{8}", in_accno) is not None:  # check if 8 digits
        return True
    else:
        return False


def validate_iban(in_iban):
    """ Validates IBAN numbers for Irish bank accounts """

    if re.match("[A-Z]{2}\d{2}[A-Z]{4}\d{14}", in_iban.upper()) is None:  # check format (low hanging fruit)
        return False

    check_iban_less_bank = in_iban[8:] + "181400"  # 181400 = conversion of "IE00"
    bank = in_iban[4:8]
    bank_num = ""
    for char in bank:
        bank_num = bank_num + str(int(string.uppercase.index(char)) + 10)  # convert letters to nums using conversion scheme
    check_iban = bank_num + check_iban_less_bank  # put string back together

    checksum = 98 - get_mod97_10(check_iban)  # get checksum
    if checksum < 10:  # add leading 0 if necessary
        checksum = "0" + str(checksum)
    else:
        checksum = str(checksum)

    if checksum == in_iban[2:4]:  # check the checksum
        return True
    else:
        return False


def get_mod97_10(in_iban):
    """ Get mod97-10 of the IBAN   """

    checksum = int(in_iban[0])
    for char in in_iban[1:]:
        checksum = checksum * 10
        checksum = checksum + int(char)
        checksum = checksum % 97
    return checksum


def validate_ppsn(in_ppsn):
    """ Validates Irish Personal Public Service Number or PPSN (Irish equivelant of Social Security no.)"""
    return check_MOD23(in_ppsn)


def validate_passport(in_pp):
    """ Validates Irish passport nums """

    if re.match("[A-Z]{2}\d{7}", in_pp.upper()) is not None:
        return True
    else:
        return False


def validate_drivers_license(in_dln):
    """ Validates Irish driver's licenses """

    if re.match("\d{9}", in_dln.replace("-", "").replace(" ", "")) is not None:
        return True
    else:
        return False


def validate_vat_number(in_vat):

    if re.match('IE\d{7}[a-z]', in_vat):
        return  check_MOD23(in_vat[2:])

    elif re.match('IE\d[a-z]\d{5}[a-z]', in_vat):
        d = in_vat[2:]
        new = "0" + d[2:7] + d[0] + d[7]
        return check_MOD23(new)
    else:
        return False


def check_MOD23(in_mod):
    i = 8
    sum = 0  # checking involves getting the sum of the result of multiplying each digit by appropriate num from  2-8

    for char in in_mod[:-1]:
        sum = sum + int(char) * i
        i = i - 1

    mod = sum % 23
    if string.lowercase[mod - 1] == in_mod[:-1].lower():
        return True
    else:
        return False


def validate_cao_number(in_num):
    """ Validates CAO number format"""

    if re.match("\d{8}", in_num) is not None:
        return True
    else:
        return False
