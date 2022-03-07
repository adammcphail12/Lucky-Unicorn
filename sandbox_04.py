
#this command prin ts the code in a different color (The 35m is the color code , the 0 in the rpeated code after restets the console color to white. note: this only works in the console, not the terminal)
print("\x1B[35m{}\x1B[0m".format("Hello"))