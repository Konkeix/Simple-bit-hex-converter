from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Converter")
root.resizable(False, False)
root.config(borderwidth=5,relief="ridge")

# Top Labels
bit0 = ttk.Label(root, text="Bit 7", padding=2)
bit0.grid(row=0, column=0, sticky="nesw")
bit1 = ttk.Label(root, text="Bit 6", padding=2).grid(row=0, column=1, sticky="nesw")
bit2 = ttk.Label(root, text="Bit 5", padding=2).grid(row=0, column=2, sticky="nesw")
bit3 = ttk.Label(root, text="Bit 4", padding=2).grid(row=0, column=3, sticky="nesw")
bit4 = ttk.Label(root, text="Bit 3", padding=2).grid(row=0, column=4, sticky="nesw")
bit5 = ttk.Label(root, text="Bit 2", padding=2).grid(row=0, column=5, sticky="nesw")
bit6 = ttk.Label(root, text="Bit 1", padding=2).grid(row=0, column=6, sticky="nesw")
bit7 = ttk.Label(root, text="Bit 0", padding=2).grid(row=0, column=7, sticky="nesw")

def update():
    """Update the binary labels and hex entry field."""
    binaryVal = []
    for x in bitxV:
        binaryVal.append(str(x.get()))
    for n in range(8):
        lblVal[n].set(binaryVal[n])

    ret = hex(int("".join(binaryVal),2))
    if len(ret) == 3:
        ret = list(ret)
        ret.insert(2,'0')
        ret = "".join(ret)
    
    ret = list(ret.upper())
    ret[1] = 'x'
    ret = "".join(ret)
    ret = "= " + ret
    entVar.set(ret)

def hextobin(event):
    entryStr = entVar.get()
    entryStr = entryStr.strip('=')
    entryStr = entryStr.strip()
    val = int(entryStr,0)
    binval = bin(val)
    print(binval)
    binval = binval.lstrip('0b')
    if len(binval) < 8:
        diff = 8 - len(binval)
        for n in range(diff):
            binval = '0' + binval
    
    n = 0
    for x in bitxV:
        x.set(binval[n])
        n += 1
        
    update()

def reset():
    """Reset duh"""
    for x in bitxV:
        x.set(0)
    for n in range(8):
        lblVal[n].set(bitxV[n].get())
        
    update()

# Input checkboxes
bitxV = []
checkFramex = []
checkButtonx = []
for n in range(8):
    bitxV.append(StringVar())
    checkFramex.append(Frame(root,width=20,height=20))
    checkFramex[n].grid(row=1, column=n)
    
    checkButtonx.append(ttk.Checkbutton(checkFramex[n], variable=bitxV[n], command=update).place(anchor=CENTER, relx=0.65, rely=0.5))
    bitxV[n].set(0)

lblBit = []
lblVal = []
lblFrames = []
for n in range(8):
    lblFrames.append(Frame(root))
    lblFrames[n].grid(row=2, column=n)
    
    lblVal.append(StringVar())
    lblVal[n].set(0)
    
    lblBit.append(ttk.Label(lblFrames[n], textvariable=lblVal[n], padding=2).grid(row=0, column=0, sticky="nesw"))

resetBut = ttk.Button(root, text="Reset", command=reset).grid(row=1, column=8, sticky="nesw")

# Hex Entry
entVar = StringVar()
entVar.set('= 0x00')
hexEntry = ttk.Entry(root, textvariable=entVar, width=8)
hexEntry.bind("<Return>", hextobin)
hexEntry.grid(row=2, column=8, sticky="nesw")

root.mainloop()