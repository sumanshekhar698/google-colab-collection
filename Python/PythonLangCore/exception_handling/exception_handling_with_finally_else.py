def process(value):
    try:
        res= 100/value
    except ZeroDivisionError:
        print("except Divison by 0")
    except TypeError as e:
        print(f"TypeError Msg: {e}")
    else:
        print(f"SUCCESS! res={res}")
    finally:
        print("finally block CLEANUP")

process(4)
process(0)
process("0")