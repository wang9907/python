
try:
    f = open("myfile.txt")
    s = f.readline();
    i = int(s.strip())
except OSError as err:
    print("OS error:{0}".format(err))
except ValueError:
    print("could't convert data to an integer")
    print("Unexpect error:")
    raise
except TypeError:
    print("typeRrror")
finally:
    print("run ")