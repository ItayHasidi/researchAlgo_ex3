import re
import string


def not_sub_string(a, b):
    a_start = a[0]
    a_end = a[1]
    b_start = b[0]
    b_end = b[1]
    flag = True
    if (a_start >= b_start and a_end >= b_end) or (b_start >= a_start and a_end >= b_end):
        flag = False
    return flag


def find_email_in_txt(f_name: string):
    """
    Finds all valid email addresses in a file and prints them.
    Also finds all incorrect email addresses and prints them as well.
    """
    f = open(f_name, "r")
    valid_emails = []
    invalid_emails = []
    pattern = re.compile("(^\w| \w|	\w)(\w|-\w|\.\w)*@\w{1}(\w|-\w|\.\w\w)+\.\w(\w)+")
    invalid_pattern = re.compile("(^.| .|	.)(-|\.|\w|#)*@*(\w|-|\.|#)*")
    for line in f:
        x = pattern.search(line)
        y = invalid_pattern.search(line)
        while x is not None:
            if x.group()[0] == " " or x.group()[0] == "\t":
                valid_emails.append(x.group()[1:])
            else:
                valid_emails.append(x.group())
            if not_sub_string(y.span(), x.span()):
                invalid_emails.append(y.group())
            line = line[x.span()[1]+1:]
            x = pattern.search(line)
            y = invalid_pattern.search(line)
    print(valid_emails)
    print(invalid_emails)


if __name__ == '__main__':
    find_email_in_txt("email.txt")
