filename = "first.txt"
text_file=open("first.txt", "a+")
text_file.write("Дозапис працює")
text_file.close()

filename = "second.txt"
text_file=open("second.txt", "a")
text_file.write("Дозапис працює")
text_file.close()
