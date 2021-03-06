import tkinter as tk
import MySQLdb





# --- functions ---
def code(value):
    db = MySQLdb.connect(host="localhost",user="jgan",passwd="1234",db="EVM")

    # you must create a Cursor object. It will let you execute all the queries you need
    cur = db.cursor()

    # inform function to use external/global variable
    global pin


    if value == 'C':
        # remove last number from `pin`
        pin = pin[:-1]
        # remove all from `entry` and put new `pin`
        e.delete('0', 'end')
        e.insert('end', pin)

    elif value == 'E':
        # check pin
        try:
            cur.execute("Select Numpad from test Where Name='James Ganley'")
            for row in cur.fetchall():
            # print all the first cell of all the rows
                storedPin = (row[0])
                print(storedPin)
                print(pin)
                if pin == 'storedpin':
                    print("PIN OK")

                else:
                    print("PIN Error!")
                    # clear `pin`
                    pin = ''
                    # clear `entry`
                db.close()

                e.delete('0', 'end')
        except:
             print("PIN Except!")

    else:
        # add number to pin
        pin += value
        # add number to `entry`
        e.insert('end', value)

    print("Current:", pin)

# --- main ---

keys = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['(', '8', ')'],
    ['C', ',', 'E'],
]

# create global variable for pin
pin = ''  # empty string

root = tk.Tk()

# place to display pin
e = tk.Entry(root)
e.grid(row=0, column=0, columnspan=3, ipady=5)

# create buttons using `keys`
for y, row in enumerate(keys, 1):
    for x, key in enumerate(row):
        # `lambda` inside `for` has to use `val=key:code(val)`
        # instead of direct `code(key)`
        b = tk.Button(root, text=key, command=lambda val=key:code(val))
        b.grid(row=y, column=x, ipadx=10, ipady=10)



root.mainloop()