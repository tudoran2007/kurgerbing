from flask import Flask,render_template,request
from order import Order
from linkedlist import LinkedList
import time

app=Flask(__name__)

ordernumber = 1

kitchenorders = LinkedList()
waiterorders =  LinkedList()
boardorders = LinkedList()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/order")
def order():
    return render_template("order.html")

@app.route("/kitchen")
def kitchen():
    return render_template("kitchen.html")

@app.route("/updatekitchen")
def updatekitchen():
    if kitchenorders.head == None:
        return ["No Orders", "", "", ""]
    orderdata = kitchenorders.peek()
    time.sleep(1)
    return orderdata

@app.route("/nextkitchenorder")
def nextkitchenorder():
    if kitchenorders.head != None:
        waiterorders.append(kitchenorders.peek())
        kitchenorders.popfirst()
        return render_template("kitchen.html")

@app.route("/waiter")
def waiter():
    return render_template("waiter.html")

@app.route("/updatewaiter")
def updatewaiter():
    if waiterorders.head == None:
        return ["No Orders"]
    orderdata = waiterorders.peek()
    time.sleep(1)
    return orderdata

@app.route("/nextwaiterorder")
def nextwaiterorder():
    if waiterorders.head != None:
        waiterorders.popfirst()
        boardorders.popfirst()
        return render_template("waiter.html")
    
@app.route("/ordered")
def customer():
    global ordernumber
    number = ordernumber
    ordernumber += 1
    burgerone = request.args.get("burgerone")
    burgertwo = request.args.get("burgertwo")
    burgerthree = request.args.get("burgerthree")
    tablenr = request.args.get("tablenr")
    items = [str(number), burgerone, burgertwo, burgerthree, str(tablenr)]
    kitchenorders.append(items)
    boardorders.append(str(number))
    return render_template("ordered.html", items=items)

@app.route("/board")
def board():
    return render_template("board.html")

@app.route("/updateboard")
def updateboard():
    if boardorders.head == None:
        return "No Orders"
    boarddata = boardorders.displayboard()
    time.sleep(1)
    return boarddata[1:]

if __name__ == "__main__":
    app.run(debug=True, host = "0.0.0.0",port=3000)