import re


def soundex(txt) -> str:
	rem_list = 'aeiouyhw'
	rep_list = {
		'bfpv': '1',
		'cgjkqsxz': '2',
		'dt': '3',
		'l': '4',
		'mn': '5',
		'r': '6'
	}

	# steps
	txt = re.sub('(?!^)[{}]'.format(rem_list), '_', txt.capitalize())
	for pat, val in rep_list.items():
		txt = re.sub('[{}]'.format(pat), val, txt)
	txt = re.sub('(?P<n>[0-9])(?P=n)|\_', '\g<n>', txt)
	txt = ''.join(txt[i] if i < len(txt) else '0' for i in range(4))
	return txt


