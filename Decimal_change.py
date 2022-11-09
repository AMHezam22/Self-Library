
def digits(digit):
	ans = ""
	if digit >= 4:
		ans += "1"
		digit -= 4
	else:
		ans += "0"
	if digit >= 2:
		ans += "1"
		digit -= 2
	else:
		ans += "0"
	if digit >= 1:
		ans += "1"
		digit -= 1
	else:
		ans += "0"
	return ans


def hex2bin(hexi: str):
	rev_hexi_dict = {
		'1': 1, '2': 2, '3': 3,
		'4': 4, '5': 5, '6': 6,
		'7': 7, '8': 8, '9': 9,
		'A': 10, 'B': 11, 'C': 12,
		'D': 13, 'E': 14, 'F': 15
	}
	ans = ""
	for digit in hexi:  # hex to binary
		digit = rev_hexi_dict[digit]
		if digit >= 8:
			ans += "1"
			digit -= 8
		else:
			ans += "0"
		ans += digits(digit)
	if ans[0] == "0":
		return ans[1:]
	return ans


def dec_to_any(num, base: int):
	hexi_dict = {
		1: "1", 2: "2", 3: "3",
		4: "4", 5: "5", 6: "6",
		7: "7", 8: "8", 9: "9",
		10: 'A', 11: 'B', 12: 'C',
		13: 'D', 14: 'E', 15: 'F'
	}
	ans = ""
	if base == 16:
		while num != 0:
			num, temp = divmod(num, base)
			ans += hexi_dict[temp]
	else:
		while num != 0:
			num, temp = divmod(num, base)
			ans += str(temp)
	return ans[::-1]


def oct2bin(octi, typ: type = str):
	ans = ""
	octi = str(octi)
	for digit in octi:
		digit = int(digit)
		ans += digits(digit)
	if typ is int:
		return int(ans)
	else:
		if ans[0] == "0":
			return ans[1:]
		return ans

