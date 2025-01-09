import matplotlib as py

x = [1,2,3,4,5]
y = [10,20,30,40,50]

py.figure(figsize=(10, 6))
py.plot(x)
py.plot(y)
py.xlabel("x",fontsize=12)
py.xlabel("y",fontsize=12)
py.grid(True,linestyle="--",alpha=0.7)
py.legend(loc="upper right")
py.bar(x,y,width=1,edgecolor="red",color="yellow",align="center")
py.title("Bar Chart")
py.show()