import textwrap

string = input()
max_width = int(input())
print('\n'.join(textwrap.wrap(string, max_width)))