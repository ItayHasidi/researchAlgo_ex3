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
    f = open(f_name, "r")
    valid_emails = []
    invalid_emails = []
    pattern = re.compile("(^\w| \w|	\w)(\w|-\w|\.\w)*@\w{1}(\w|-\w|\.\w\w)+\.\w(\w)+")
    invalid_pattern = re.compile("(^.| .|	.)(-|\.|\w|#)*@*(\w|-|\.|#)*")
    for line in f:
        x = pattern.search(line)
        y = invalid_pattern.search(line)
        while x is not None:
            valid_emails.append(x.group()[1:])
            if not_sub_string(y.span(), x.span()):
                invalid_emails.append(y.group())
            line = line[x.span()[1]+1:]
            x = pattern.search(line)
            y = invalid_pattern.search(line)
    print(valid_emails)
    print(invalid_emails)


if __name__ == '__main__':
    find_email_in_txt("email.txt")
